
from flask import Flask, render_template, request
from os import getcwd
from class_modules.read_class import Read
from class_modules.normalize_class import Normalize
from class_modules.word_class import Word_Generator
from class_modules.markov_class import Markov_Model
from class_modules.dictogram_class import Dictogram
import random

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    sentence = generate_sentence(length=10)
    return render_template('home_view.html', sentence=sentence)


@app.route('/refresh', methods=['POST'])
def generate():
    sentence = generate_sentence(int(request.form['length']))
    return render_template('home_view.html', sentence=sentence)


def gen_markov(word_arr, current_word, window=1):

    markov_model = dict()
    for i in range(0, len(word_arr) - window):
        if current_word in word_arr[i]:
            if current_word in markov_model:
                markov_model[current_word].update([word_arr[i+1]])
            else:
                markov_model[current_word] = Dictogram([word_arr[i+1]])
    return markov_model


def write_result_test(output_doc, current_word, test_run, model, mode='a+'):
    output_file = open(output_doc, mode)
    writing = str(test_run) + '  ===== ' 

    # OUTPUT MODEL DICTOGRAM 
    for key, value in model.items():
        writing += 'Current word {}: == Key {}: == Value(s) {}:\r'.format(current_word, key, value) 
    output_file.write(writing)
    output_file.close()


def write_sentence(current_sentence, mode='a+'):

    output_file = open('./ENV/generated_sentences.txt', mode) # heroku file path
    # output_file = open('../ENV/generated_sentences.txt', mode)
    writing = str(current_sentence)

    # OUTPUT SENTENCE
    output_file.write(current_sentence)
    output_file.close()


def generate_sentence(length):
    filepath = './ENV/corpus_copy.txt' # heroku file path
    # filepath = '../ENV/corpus_copy.txt' # production file path
    print(filepath)
    document_arr = Read(filepath)
    print(document_arr)

    # initialize Read
    document_arr = Read(filepath)

    # initialize Normalize
    word_list = Normalize(document_arr.get_document_arr())
    word_list = word_list.get_normalized_result()

    # initialize dictionary, given a list
    start_dictogram = Dictogram(word_list)
    start_dictogram = start_dictogram.get_dictionary_result()

    # (1) ARRAY IS INPUT 
    markov_dictogram1 = Dictogram(word_list)
    ## (2) DICTOGRAM IS OUTPUT {'WORD': 1}
    markov_dictogram2 = markov_dictogram1.get_dictionary_result()
    ### (3) DICTOGRAM IS INPUT {'WORD: 1} >> WORD IS SET, NOTHING IS RETURNED
    markov_dictogram3 = Word_Generator(markov_dictogram2, markov_dictogram2.tokens, markov_dictogram2.types, False)
    #### (4) WORD IS OUTPUT
    markov_word = markov_dictogram3.get_word()

    ######## (8) SET THE NUM OF SENTENCES
    sentence = ''
    if markov_word is not None:
        sentence = markov_word[0].capitalize() + markov_word[1:] + ' '

    for idx in range(0, length):
        # RETURN THE MARKOV MODEL, GIVEN THE CURRENT WORD AND
        # ALL FOLLOWING WORDS, OF THE GIVEN KEY
        ##### (5) ARRAY (ORIGINAL), WORD & WINDOW-SIZE IS INPUT >> NOTHING IS RETURNED, OBJECT IS UPDATED
        markov_dictogram5 = Markov_Model(word_list, markov_word, 1)

        ###### (6) MARKOV-MODEL DICTOGRAM WITH A WINDOW-SIZE '2' IS RETURNED
        markov_dictogram = markov_dictogram5.get_markov_model()

        ####### (7) DICTOGRAM-WINDOW-SIZE-2, CURRENT WORD > PRECONDITION: INSTANCE OF WORD-GENERATOR
        markov_word = markov_dictogram3.random_markov_word(markov_dictogram, markov_word, 1)
        
        # (3) OUTPUT MODEL DICTOGRAM 
        # write_result_test('/app/ENV/output_test.txt', markov_word, 1, markov_dictogram)  # OUTPUT THE RESULT
        
        # (4) CHECK RESULT
        if markov_word is not None:
            sentence = sentence.strip() + ' ' + markov_word.strip() + ' '

        # print('word {}: {}'.format(i, markov_word))
        word_arr = markov_word.split()
        # print(len(word_arr))
        if len(word_arr) == 2:
            markov_word = word_arr[1]
        elif len(word_arr) == 1:
            markov_word = word_arr[0]

    sentence = sentence.strip() + '.\r'

    # # (4) OUTPUT SENTENCE TO TXT FILE
    write_sentence(sentence, mode='a+')
    return sentence


if __name__ == '__main__':
    app.run()


