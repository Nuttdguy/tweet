import random
import os
import time
from sys import argv


# SOLUTION # 1
def get_filename_from_input():
    """ Returns the file from user input """
    current_dir = os.getcwd() + '/assets/'
    file_dir = input('What file would you like to open\n')
    return current_dir + file_dir


def get_items_from(file_content, item_qty):
    """ Returns a random sequence of words; the sentence is the length of item_qty"""
    sentence = ''
    for item in range(len(file_content)):
        if item < item_qty:
            extract_idx = random_generate(len(file_content))
            sentence += file_content[extract_idx] + ' '
        else:
            break
    return sentence


# read the file contents and returns result into an array
def read_file(file, mode):
    """ Returns an array of words from file input """
    file_content = []
    with open(file, mode=mode) as dictionary:
        for line in dictionary:
            file_content.append(line.replace('\n', ''))
    dictionary.close()

    return file_content


def random_generate(max_scale):
    """ Returns a random int up to max_scale """
    return random.randint(0, max_scale)


if __name__ == '__main__':
    item_qty = int(argv[len(argv) - 1])
    file_name = get_filename_from_input().lower()
    print('====== Begin timer =====\n')
    start = time.time()

    random_sentence = get_items_from(read_file(file_name, 'r'), item_qty)
    print(random_sentence)

    end = time.time()
    print('\n====== Finished in ' + str(end - start) + ' seconds =====\n')

