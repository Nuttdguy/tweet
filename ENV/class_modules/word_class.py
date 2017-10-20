import os
import random
from class_modules.dictogram_class import Dictogram # FOR PRODUCTION RELEASE
# from dictogram_class import Dictogram


class Word_Generator():
    """ initalize sentence generator, """

    def __init__(self, iterable=None, tokens=0, types=0, phrase=True, window=0):
        self.tokens = tokens
        self.types = types
        self.sentence = ''
        self.word = ''
        if iterable and phrase == False:
            self.random_word(iterable)
        # else:
        #     self.random_markov_word(iterable)
        # elif iterable and phrase == False:
        #     self.random_word(iterable)

    # TEST BELOW FOR MARKOV MODEL IMPLEMENTATION
    ### RETURNS A SINGLE WORD -- NO SEED, JUST CUMULATIVE UP TO RANDOM NUMBER
    def random_word(self, iterable):
        cumulative_prob = 0.0
        rand = random.uniform(0, 1)
        key_arr = list(iterable.keys())
        # print(self.types, self.tokens)

        for idx in range(0, self.types):    ### TYPES, DISTINCT WORDS
            print('cummulative: {}  ==  rand: {}'.format(cumulative_prob, rand))
            print('iterable {}  == self.tokens {} == index: {}'.format(iterable[key_arr[idx]], self.tokens, idx))
            cumulative_prob += float(iterable[key_arr[idx]] / self.tokens)  ### TOKEN, TOTAL ALL WORDS
            if cumulative_prob > rand:
                self.word = key_arr[idx]
                break

    def random_markov_word(self, iterable, word_to_match, window=0):
        cumulative_prob = 0.0
        rand = random.uniform(0, 1)
        key_arr = list(iterable.keys())
        total_tokens = 0

        if window == 1:
            for idx_1 in range(0, len(key_arr)):    ### TYPES, DISTINCT WORDS
                key_list = list(iterable.keys())
                current_key = ''.join(key_list[idx_1])

                # (1) MATCH THE WORD, WHEN MATCHED - 
                if current_key == word_to_match:
                    # print('WORD TO MATCH: {} == KEY: {}'.format(word_to_match, current_key))
                    ## (2) GET INNER KEYS OF NESTED DICTIONARY, CONVERT INTO LIST ENABLE LOOPING
                    inner_keys = list(iterable[key_list[idx_1]].keys())
                    # print('INNER KEYS: {}'.format(inner_keys))
                    # print('SHOULD BE COUNT: {}'.format(len(inner_keys)))
                    print('SHOULD BE COUNT: {}'.format(len(inner_keys)))

                    ### (3) GET TOTAL COUNT OF INNER KEYS
                    for key_idx in range(len(inner_keys)):
                        # print( iterable[key_list[idx_1]][inner_keys[key_idx]] )
                        total_tokens += iterable[key_list[idx_1]][inner_keys[key_idx]]

                    for idx_2 in range(len(inner_keys)):
                        # USE ORIGINAL KEY, GET THE VALUES OF IT (I.E. USE NOT CONVERTED TO STRING KEY)
                        # word_window = ''.join(key_list[idx_1]) + ' ' + ''.join(inner_keys[idx_2]) 
                        word_window = ''.join(inner_keys[idx_2]) 
                        print('WORD WINDOW: {} == CURRENT KEY: {}'.format(word_window, current_key))

                        cumulative_prob += float(iterable[key_list[idx_1]][inner_keys[idx_2]] / total_tokens)  ### TOKEN, TOTAL ALL WORDS
                        # print('cummulative: {} == tokens: {} ==  rand: {}'.format(cumulative_prob, total_tokens, rand))

                        # word_window = ''.join(key_list[idx_1]) + ' ' + ''.join(inner_keys[idx_2]) 
                        # print('WORD WINDOW: {} == CURRENT KEY: {}'.format(word_window, current_key))

                        # cumulative_prob += float(iterable[key_list[idx_1]][inner_keys[idx_2]] / total_tokens)  ### TOKEN, TOTAL ALL WORDS
                        # print('cummulative: {}  ==  rand: {}'.format(cumulative_prob, rand))

                        if cumulative_prob > rand:
                            print('WORD {}:'.format(word_window))
                            return word_window
        else:
            for idx in range(0, len(key_arr)):    ### TYPES, DISTINCT WORDS
                key_dict = iterable[key_arr[idx]] 
                key_list = list(iterable.keys())

                # count total tokens for the current iteration
                for count in range(len(key_list)):
                    total_tokens += key_dict[key_list[count]]

                for key, value in key_dict.items():
                    cumulative_prob += float(value / total_tokens)  ### TOKEN, TOTAL ALL WORDS
                    if cumulative_prob > rand:
                        print('PRE-KEY: {} == KEY: {} == Value: {}'.format(key_list[idx], key, value))
                        return key


    # def markov_random_seed(self, iterable, window):
    #     cumulative_prob = 0.0
    #     rand = random.uniform(0, 1)
    #     key_arr = list(iterable.keys())
    #     for idx in range(0, self.types):
    #         current_key = key_arr[idx] + ' ' + key_arr[idx + window]
    #         cumulative_prob += float(iterable[key_arr[idx]] / self.tokens)  ### TOKEN, TOTAL ALL WORDS
    #         # print('cummulative: {}  ==  rand: {}'.format(cumulative_prob, rand))
    #         # print('iterable {}  == self.tokens {}'.format(iterable[key_arr[idx]], self.tokens))
    #         if cumulative_prob > rand:
    #             print('Key: {}'.format(current_key))
    #             return str(current_key)
        

    def get_sentence(self):
        return self.sentence


    def get_word(self):
        return self.word




    # Get a Start Seed, append as first sentence
    # get any words, keys, following the seed word
    # Use HashTable and LinkedList to generate sentence

    # def gen_markov_sentence(self, markov_model, length=10):
    #     """  generate markov sentence given a markov model """
    #     current_word = (self.random_markov_word(markov_model)).replace('[', '').replace(']', '').replace('\'', '')
    #     sentence = current_word + ' '
    #     for idx in range(0, length):
    #         next_word = self.random_markov_word(markov_model)
    #         next_word = next_word;
    #         sentence += str(next_word)
    #     return sentence

    # def random_sentence(self, iterable, length=10):
    #     cumulative_prob = 0.0
    #     key_arr = list(iterable.keys())
    #     for i in range(length):
    #         rand = random.uniform(0, 1)
    #         for idx in range(0, self.types):
    #             cumulative_prob += iterable[key_arr[idx]]
    #             if cumulative_prob > rand:
    #                 self.sentence += key_arr[idx] + ' '
    #                 cumulative_prob = 0.0
    #                 break

    # def random_markov_word(self, markov_model):
    #     """  generate a word given a markov model """
    #     cumulative_prob = 0.0
    #     rand = random.uniform(0, 1)
    #     key_arr = list(markov_model.keys())
    #     types = len(markov_model)
    #     for idx in range(0, len(key_arr)):
    #         for key, val in markov_model.items():
    #             print('key: {} == value {}: '.format(key, val))
    #             cumulative_prob += float(val / types)
    #             # print(cumulative_prob, rand, types)
    #             if cumulative_prob > rand:
    #                 self.word = key
    #                 return self.word

    # def random_start(self, model):
    #     if 'END' in model:
    #         seed_word = 'END'
    #         while seed_word == 'END':
    #             seed_word = model['END'].random_word()
    #         return seed_word
    #     return random.choice(model.keys())




