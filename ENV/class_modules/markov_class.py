import random
from class_modules.dictogram_class import Dictogram
# from dictogram_class import Dictogram


class Markov_Model(Dictogram):

    def __init__(self, iterable=None, word=None, window=0):
        self.markov_model = dict()
        if iterable and window == 0:
            self.generate_markov(iterable, word)
        else:
            self.nth_order_markov(iterable, word, window)


    def generate_markov(self, iterable, word):
        """  Generate a Markov model given a iterable """
        # key_list = list(iterable.keys())
        for idx in range(0, len(iterable) - 1):
            if word in self.markov_model:
                self.markov_model[word].update([iterable[idx+1]])
            else:
                self.markov_model[word] = Dictogram([iterable[idx+1]])


    def nth_order_markov(self, iterable, word, window):
        """  Generate Markov with a view word depth, nth order  """
        # key_list = list(iterable.keys())
        for idx in range(0, len(iterable) - (1 + window) ):
            word_view = tuple(iterable[idx: idx + window])

            if word in self.markov_model:
                self.markov_model[word_view].update([iterable[idx + 1] + ' ' + iterable[idx + 2]])
            else:
                self.markov_model[word_view] = Dictogram([iterable[idx + 1] + ' ' + iterable[idx + 2]])


    def get_markov_model(self):
        return self.markov_model

            

