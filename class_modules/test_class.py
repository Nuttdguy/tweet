from read_class import Read
from normalize_class import Normalize
from dictogram_class import Dictogram
from stochastic_class import Stochastic
from word_class import Word_Generator
from markov_class import Markov_Model
import random
import os


# 'ARRAY' TYPE IS INPUT 
def gen_markov(word_arr, current_word, window=1):
    # MAKE AN EMPTY DICTIONARY, STORE THE CURRENT_WORD:VALUE PAIR 
    markov_model = dict()

    # BUILD A MARKOV MODEL WITH THE 'CURRENT WORD' AS THE KEY
    # FOR ALL VALUES THAT FOLLOW THE 'CURRENT WORD; 
    # #### RESULT IS APPENDED TO OUTPUT_TEST.TXT
    for i in range(0, len(word_arr) - window):
        if current_word in word_arr[i]:
            if current_word in markov_model:
                markov_model[current_word].update([word_arr[i+1]])
            else:
                markov_model[current_word] = Dictogram([word_arr[i+1]])
    # else:
    #     for i in range(0, len(word_arr) - window):
    #         if current_word in word_arr[i]:
    #             nth_order_word = word_arr[i] + ' ' + word_arr[i + 1] 
    #             if current_word in markov_model:
    #                 markov_model[current_word].update([ nth_order_word  ] )
    #             else:
    #                 markov_model[current_word] = Dictogram([ nth_order_word ])
    return markov_model

def write_result_test(output_doc, current_word, test_run, model, mode='a+'):
    output_file = open(output_doc, mode)
    writing = str(test_run) + '  ===== ' 

    # OUTPUT MODEL DICTOGRAM 
    for key, value in model.items():
        writing += 'Current word {}: == Key {}: == Value(s) {}:\r'.format(current_word, key, value)         
    
    output_file.write(writing)
    output_file.close()


if __name__ == '__main__':
    filepath = './../corpus.txt'

    # initialize Read
    document_arr = Read(filepath)

    # initialize Normalize
    word_list = Normalize(document_arr.get_document_arr())
    word_list = word_list.get_normalized_result()

    # initialize dictionary, given a list
    start_dictogram = Dictogram(word_list)
    start_dictogram = start_dictogram.get_dictionary_result()

    # TESTING MARKOV DICTIONARY >> DOES NOT WORK
    # (1) ARRAY IS INPUT 
    markov_dictogram1 = Dictogram(word_list)
    ## (2) DICTOGRAM IS OUTPUT {'WORD': 1}
    markov_dictogram2 = markov_dictogram1.get_dictionary_result()
    ### (3) DICTOGRAM IS INPUT {'WORD: 1}
    markov_dictogram3_word  = Word_Generator(markov_dictogram2, markov_dictogram2.tokens, markov_dictogram2.types, False)
    #### (4) WORD IS OUTPUT
    markov_word4 = markov_dictogram3_word.get_word()
    ##### (5) ARRAY (ORIGINAL), WORD & WINDOW-SIZE IS INPUT
    markov_dictogram5 = Markov_Model(word_list, markov_word4, 1)
    ###### (6) DICTOGRAM OF WINDOW-SIZE '2' IS RETURNED
    markov_dictogram6 = markov_dictogram5.get_markov_model()
    ####### (7) DICTOGRAM-WINDOW-SIZE-2, CURRENT WORD > PRECONDITION: INSTANCE OF WORD-GENERATOR
    markov_dictogram7 = markov_dictogram3_word.random_markov_word(markov_dictogram6, markov_word4, 1)


    # (1) GET A WORD
    # result = Word_Generator(start_dictogram, start_dictogram.tokens, start_dictogram.types, False)
    # current_word = result.get_word()
    # print('word {}: {}'.format(1, current_word)) ## RETURN THE FIRST TWO SEED WORDS, E.G. 'THE'

    # (2) SET THE NUM OF SENTENCES
    # sentence = current_word[0].capitalize() + current_word[1:] + ' '

    # sentence = result_markov.get_word() + ' '
    # print(current_word)

    # for i in range(14):

        ## (1) RETURN THE MARKOV MODEL, GIVEN THE CURRENT WORD AND
        ## ALL FOLLOWING WORDS, OF THE GIVEN KEY
        # model = gen_markov(word_list, current_word, 1)

        ## (2) SELECT A RANDOM WORD FROM 'NEW MODEL'
        # current_word = result.random_markov_word(model, current_word)
        
        ## (3) OUTPUT MODEL DICTOGRAM 
        # write_result_test('./output_test.txt', current_word, 1, model)  # OUTPUT THE RESULT
        
        ## (4) CHECK RESULT
        # print('word {}: {}'.format(i, current_word))
        # sentence += current_word + ' '

        # TESTING NTH ORDER MARKOV >> DOES NOT WORK
        # model_test = gen_markov(word_list, current_word, 2) 
        # current_word = result_markov.random_markov_word(model_test, current_word)
        # print(current_word)
        # write_result_test('./output_test.txt', current_word, 1, model_test)  # OUTPUT THE RESULT
        # sentence += current_word + ' '     

    # print(sentence)

