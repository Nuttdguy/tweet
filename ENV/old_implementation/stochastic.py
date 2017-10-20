import os
import random
from time import time

from histogram import convert_to_dict
from histogram import normalize


def random_word(file):
    return file[random.randint(0, len(file) - 1)]


# accepting an array an input, this function creates a new dictionary with probability percent
# key = word, value = probability
def stochastic_count(word_arr):
    """ Returns dictionary with probability as value, word as key """
    total_sum = len(word_arr)
    stochastic_dict_with_probability = {}
    for key in word_arr:
        # formula s = (1 - (w/t)) / t)
        # w = word for probability, t = total unique word count
        stochastic_dict_with_probability[key] = float((1 - (word_arr[key] / total_sum)) / total_sum)

    return stochastic_dict_with_probability


# this function is used to verify the result of stochastic count function is correct
def verify_stochastic_count(stochastic_dict):
    """ Returns the percent of the sum of all probability values from dictionary """
    check_total_count = 0
    for i in stochastic_dict:
        check_total_count += stochastic_dict[i]
    print('%08f == checking word count percent / math' % check_total_count) # should not be greater than 1


# this function runs randomize n times,
# accepting an array as an input param, the word to analyze and times to run
def check_word_randomness(word_array, word, run_times):
    """ Returns the number of times a word was randomly chosen given a number of run-times """
    count = 0
    for idx in range(run_times):
        rw = random_word(word_array)
        if word == rw:
            count += 1
    return [word, count]


def construct_sentence(stochastic_dict_with_prob, sentence_length):
    """ Returns a sentence of random words given the desired length of sentence and dictionary with probabilities """
    sentence = ''
    for i in range(sentence_length):
        sentence += random_choice(stochastic_dict_with_prob) + ' '
    return sentence


def random_choice(stochastic_dict_with_prob):
    """ Returns a random word from a dictionary with word:probability pair """
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in stochastic_dict_with_prob.items():
        cumulative_probability += item_probability
        # print('%.04f random  <  %.08f prob factor ' % (x, cumulative_probability))
        if x < cumulative_probability:
            # print('%.04f random  <  %.08f prob factor ' % (x, cumulative_probability))
            return item
    return


if __name__ == '__main__':

    start = time()
    file = os.getcwd() + '/assets/time-machine.rtf'
    word_array = normalize(file)
    word = random_word(word_array)

    word_dict = convert_to_dict(word_array)
    # print(word_dict)
    print(len(word_dict))

    word_dict_with_prob = stochastic_count(word_dict)
    # verify_stochastic_count(word_dict_with_prob)
    # print_dict(word_dict_with_factor)

    # print(count_unique_words_in(word_dict))

    # check the number of times the search 'word' shows up given a run amount
    # search_word = 'hot'
    # run_times = 100000
    # print('The probability for "%s" is %.12f percent' % (search_word, word_dict_with_prob[search_word]))
    # sampling_result = check_word_randomness(word_array, search_word, run_times)

    sentence_length = 12
    random_sentence = construct_sentence(word_dict_with_prob, sentence_length)
    # random_sentence = random_choice(word_dict_with_prob, sentence_length)
    print(random_sentence)

    stop = time()
    run_time = (stop - start)
    print('The program took %.04f seconds to run.' % run_time)
    # print(sampling_result)

