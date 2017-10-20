#!python
import random
import copy


class Dictogram(dict):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Dictogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable, ):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:  ## Linear time O(n)
            self.tokens += 1  ## Constant time O(1)
            if item in self:  ## Constant time O(1)
                self[item] += 1  ## Constant time O(1)
            else:
                self[item] = 1  ## Constant time O(1)
                self.types += 1  ## Constant time O(1)

    def count(self, key):
        """Return the count of the given key in this histogram, or 0"""
        if self[key] == KeyError:
            return 0
        return self[key]

    def random_word(self):
        key = random.sample(self, 1)
        return key[0]

    def get_dictionary_result(self):
        return self


# def test_histogram(text_list):
#     print('text list:', text_list)

#     hist_dict = Dictogram(text_list)
#     print('dictogram:', hist_dict)

#     hist_dict.weight_dictogram()
#     print(80*"=")
#     print(hist_dict.random_sentence())

if __name__ == '__main__':
    import sys
    arguments = sys.argv[1:]  # exclude script name in first argument

    if len(arguments) == 0:
        # test histogram on letters in a word
        word = 'abracadabra'
        test_histogram(word)
        print()

        # test histogram on words in a sentence
        # sentence = 'one fish two fish red fish blue fish '
        # word_list = sentence.split()
        filename = '../ENV/ghost_kings.rtf'
        word_list = open(filename).read().strip().split()
        test_histogram(word_list)

# def random_sentence(self, length=None):
#     sentence = ''
#     if length is None:
#         length = 10
#     for i in range(10):
#         sentence += self.weight_dictogram(self) + ' '
#     return sentence
