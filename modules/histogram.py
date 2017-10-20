from sys import argv
from read import read_from
from normalize import cleanup_arr


def dict_histogram(source_tuple):
    """ Returns a dictionary histogram given a source tuple  """
    histogram = {}
    for word in source_tuple:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
    return histogram


# remove duplicate elements, keep count of elements deleted
def tuple_histogram(source_arr):
    arr_copy = sorted(source_arr)
    # TODO


def unique_word_in(histogram):
    """ Returns the number of unique words in a histogram """
    return len(histogram)


def print_dictionary(histogram):
    """ Prints the key and values from a histogram """
    for key, value in histogram.items():
        print(key, value)


def frequency_of(word, histogram):
    """ Returns the word frequency of a given word having a word:count pair"""
    return histogram.get(word)


def count_mean_of(histogram):
    """ Returns an inclusive mean of all words in given dictionary histogram """
    mean = 0
    for value in histogram:
        mean += histogram[value]
    return mean / len(histogram)


def extract_mode_of(histogram):
    """ Returns the most used word in a given dictionary histogram """
    mode = 0
    key_value = []
    for key in histogram:
        value = int(histogram[key])
        if value > mode:
            mode = value
            key_value = key, value
    return key_value


if __name__ == '__main__':
    source_arr = read_from(argv[1])
    source_items = cleanup_arr(source_arr) # Return an array of words
    histogram = dict_histogram(source_items)
    unique_words = unique_word_in(histogram)
    # print(source_items)
    print(tuple_histogram(source_items))



