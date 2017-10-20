import os
import random


class Sentence_Generator():
    
    """ initalize sentence generator, """
    def __init__(self, iterable=None, tokens=0, types=0, phrase=True):
        self.tokens = tokens
        self.types = types
        self.sentence = ''
        self.word = ''
        if iterable and phrase == True:
            self.random_sentence(iterable)
        elif iterable and phrase == False:
            self.random_word(iterable)
                    

    def random_markov_word(self, markov_model):
        """  generate a word given a markov model """
        cumulative_prob = 0.0
        rand = random.uniform(0, 1)
        key_arr = list(markov_model.keys())
        types = len(markov_model)
        for idx in range(0, len(key_arr)):
            for key, val in markov_model[key_arr[idx]].items():
                cumulative_prob += float(val / types)
                # print(cumulative_prob, rand, types)
                if cumulative_prob > rand:
                    self.word = key_arr[idx]
                    return self.word

    
    def gen_markov_sentence(self, markov_model, length=10):
        """  generate markov sentence given a markov model """
        current_word = (self.random_markov_word(markov_model)).replace('[', '').replace(']', '').replace('\'', ' ')
        sentence = current_word + ' '
        for idx in range(0, length):
            next_word = self.random_markov_word(markov_model)
            next_word = next_word.replace('[', '').replace(']', '').replace('\'', ' ')
            sentence += str(next_word)
        return sentence


    def random_sentence(self, iterable, length=10):
        cumulative_prob = 0.0
        key_arr = list(iterable.keys())
        for i in range(length):
            rand = random.uniform(0, 1)
            for idx in range(0, self.types):
                cumulative_prob += iterable[key_arr[idx]]
                if cumulative_prob > rand:
                    self.sentence += key_arr[idx] + ' '
                    cumulative_prob = 0.0
                    break


    def random_word(self, iterable):
        cumulative_prob = 0.0
        rand = random.uniform(0, 1)
        key_arr = list(iterable.keys())
        for idx in range(0, self.types):
            cumulative_prob += iterable[key_arr[idx]]
            if cumulative_prob > rand:
                self.word = key_arr[idx]
                break


    def get_sentence(self):
        return self.sentence


    def get_word(self):
        return self.word





    