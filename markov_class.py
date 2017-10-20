from ENV.dictogram_class import Dictogram
import random

class Markov_Model():

    def __init__(self, dictogram=None, depth=0):
        self.markov_model = dict()
        if dictogram and depth == 0:
            self.generate_markov(dictogram)
        else:
            self.nth_order_markov(dictogram, depth)


    def generate_markov(self, dictogram):
        """  Generate a Markov model given a dictogram """
        key_list = list(dictogram.keys())
        for idx in range(0, len(key_list) - 1):
            if key_list[idx] in self.markov_model:
                self.markov_model[key_list[idx]].update([key_list[idx]])
            else:
                self.markov_model[key_list[idx]] = Dictogram([key_list[idx+1]])


    def nth_order_markov(self, dictogram, depth ):
        """  Generate Markov with a view word depth, nth order  """
        key_list = list(dictogram.keys())
        for idx in range(0, len(key_list) - depth):
            word_view = str(key_list[idx: idx + depth])

            if word_view in self.markov_model:
                self.markov_model[word_view].update([key_list[idx + depth]])
            else:
                self.markov_model[word_view] = Dictogram([key_list[idx + depth]])


    def get_markov_model(self):
        return self.markov_model

            

