import random
from sys import argv


# SOLUTION # 1
def random_word_generator(*args):

    word = ""
    for item in args:
        word = item[1::]
        random.shuffle(word)

    word_string = ""
    for w in word:
        word_string += w + ' '
    print(word_string)


# SOLUTION # 2
def random_generate(words):

    shuffled_words, shuffled_phrase = words[1:], ''
    random.shuffle(shuffled_words)

    for word in shuffled_words:
        shuffled_phrase += word + ' '

    return shuffled_words


# SOLUTION # 3
def random_slice(words):

    shuffled_arr = []
    copied_words = words[1:]
    for idx in range(len(copied_words)):
        idx = get_random(len(copied_words) - 1)
        shuffled_arr = (copied_words[idx::] + copied_words[0:idx])

    return shuffled_arr


# SOLUTION # 4
def random_slice_shuffle(words, of_times):

    del words[len(words) - 1]
    copied_words = words[1:]
    for idx in range(of_times):
        rand_idx = get_random(len(copied_words) - 1)
        shuffled_arr = copied_words[rand_idx::] + copied_words[0:rand_idx]
        # print(convert_to_sentence(shuffled_arr))
    return shuffled_arr


def get_random(number):
    return random.randint(0, number)


def convert_to_sentence(shuffled_arr):
    sentence = ''
    for word in shuffled_arr:
        sentence += word + ' '
    return sentence


if __name__ == '__main__':
    shuffle_times = int(argv[len(argv) - 1])
    # shuffled_words = random_generate(argv)
    shuffled_words = random_slice(argv)
    # following words, input a number to indicate amount of times to randomize words
    # shuffled_words = random_slice_shuffle(argv, shuffle_times)
    print(shuffled_words)


