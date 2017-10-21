import os
import random
from time import time

# Dictogram == updates token and type count
# Stochastic == weight the count, generates random sentence

class Stochastic():

    def __init__(self, types, iterable=None):
        self.types = types
        self.weight_dict = {}
        if iterable:
            self.weight_dictogram(iterable)
            
    # def weight_dictogram(self, iterable):
    #     """ Updates dict with sample """
    #     for key in iterable.keys():
    #         self.weight_dict[key] = (iterable[key] / self.types)
    
    def stochastic_result(self):
        return self.weight_dict

    def print_stochastic(self):
        print(self.weight_dict)


if __name__ == '__main__':
    dictionary = { 'word': 4, 'say': 5, 'limit': 10 }
    print(dictionary)
    s = Stochastic(dictionary)
    s.random_sentence()
    s.print_sentence()