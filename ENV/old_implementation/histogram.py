import time
import re


# A histogram() function which takes a source_text argument (can be either a filename or
# the contents of the file as a string, your choice) and return a histogram data structure
# that stores each unique word along with the number of times the word appears in the source text.

def normalize(source_text):
    """ Returns an array with following characters removed """
    normalized_file = open(source_text).read()\
        .replace('|', '') \
        .replace('[', '') \
        .replace(']', '') \
        .replace('{', '')\
        .replace('}', '')\
        .replace('(', '')\
        .replace(')', '')\
        .replace(',', '')\
        .replace('_', '')\
        .replace(";", '')\
        .replace('\"', '')\
        .replace('#', '')\
        .replace('$', '')\
        .replace('&', '')\
        .replace('?', '')\
        .replace("\\", '')\
        .replace('--', ' ')\
        .replace('-', ' ')\
        .replace('-+', '')\
        .replace('*', '')\
        .replace("'", '')\
        .replace(':', '')\
        .replace('+', '')\
        .lower().split()

    return normalized_file

# A unique_words() function that takes a histogram argument and returns the total count of
# unique words in the histogram. For example, when given the histogram for The Adventures
# of Sherlock Holmes, it returns the integer 8475.


def convert_to_dict(word_array):
    """ Returns a dictionary of key:value pairs;
    the number of unique occurrences of words and the count
    :param word_array:
    :return: dictionary {word:count}
    """
    dictionary = {}
    for word in range(len(word_array)):
        format_word = re.sub('[^a-zA-Z\-]+', '', word_array[word])
        if word_array[word] not in dictionary:
            dictionary[format_word] = 1
        else:
            dictionary[format_word] += 1
    return dictionary


def count_unique_words_in(word_dict):
    """ Returns the number of unique word occurrences from sorted dictionary """
    return len(word_dict)


def print_dict(word_dict):
    """ Prints out each dictionary key and value """
    for key in word_dict:
        print(key, word_dict[key])


# A frequency() function that takes a word and histogram argument and returns the
# number of times that word appears in a text. For example, when given the word "mystery"
# and the Holmes histogram, it will return the integer 20.


def frequency_of(word, hist):
    """ Returns the word frequency of word from dictionary having a word:count pair"""
    return hist.get(word)


def count_mean(word_dict):
    """ Returns the mean from all words, average count """
    mean = 0
    for num in word_dict:
        mean += word_dict[num]
    return mean / len(word_dict)


def extract_mode(word_dict):
    """ Returns the mode, most used word """
    mode = 0
    key_value = []
    for key in word_dict:
        value = int(word_dict[key])
        if value > mode:
            mode = value
            key_value = key, value
    return key_value


if __name__ == '__main__':
    # file = '../assets/voyage.txt'
    source_text = '../assets/ghost_kings.rtf'
    start = time.time()
    normalize_file = normalize(source_text)

    word_dict = convert_to_dict(normalize_file) # convert array into dictionary with count occurrence

    search_word = 'the'
    frequency = frequency_of(search_word, word_dict)
    print('The word "%s" occurs %d times.' % (search_word, frequency))

    unique_word_count = count_unique_words_in(word_dict) # the total unique words in dict
    print('There are a total of %d unique words.' % unique_word_count)

    mean = count_mean(word_dict)
    print('The mean (average) is %d.' % mean)

    # dict = {'runny': 9, 'sunny': 5, 'sally': 3, 'ugly': 5, 'worm': 4, 'tree': 10}
    mode = extract_mode(word_dict)
    print('The mode is %d and key is "%s".' % (mode[1], mode[0]))

    end = time.time()
    print(end - start)


# def unique_words_in(hist):
#     counted_arr = collections.Counter(hist)
#     count = 0
#     for _ in counted_arr:
#         count += 1
#     return count
