from sys import argv
from re import sub
from re import compile
from re import IGNORECASE
from read import read_from

""" Default regular expression for module """
reg_expr = compile('[\W\s ^0-9]+', IGNORECASE)


def cleanup_arr(source, reg_expr=reg_expr):
    """ Returns a tuple of given items of an array with characters removed """
    done = []
    for item in range(len(source) - 1):
        current_line = str(source[item]).split(' ')
        for word in current_line:
            word = str(remove_special_characters_from(word))
            done.append(sub(reg_expr, '', word))
    tuple(done)
    return done


def remove_special_characters_from(item):
    """ Returns the lowercase word with special characters removed  """
    return str(item).lower()\
        .replace('[', '')\
        .replace(']', '')\
        .replace('\\', '')\
        .replace("\\\\", '')\
        .replace("_", '')


if __name__ == '__main__':
    source_arr = read_from(argv[1])
    cleaned_tuple = cleanup_arr(source_arr, reg_expr)
    print(cleaned_tuple)


