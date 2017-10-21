from sys import argv
import re


class Normalize():
    """ Default regular expression for class """
    # reg_expr = re.compile('[\W\S ^0-9]+', re.IGNORECASE)
    reg_expr = re.compile('(?<!\S)[A-Za-z]+(?!\S)')

    def __init__(self, source_file=None, reg_expr=reg_expr):
        self.normalized_list = []
        if source_file:
            self.cleanup_arr(source_file, reg_expr)


    def cleanup_arr(self, source_file, reg_expr):
        """ Returns a tuple of given items of an array with characters removed """
        for item in range(len(source_file) - 1):
            current_line = str(source_file[item]).split()
            for word in current_line:
                # word = re.sub(reg_expr, '', word)
                # word = str(self.remove_special_characters_from(word))
                self.normalized_list.append(word.strip('(?[]\\\\"\,\'\.<!\S)+(?!\S)').replace('  ', ' '))
                filter(None, self.normalized_list)


    def remove_special_characters_from(self, word):
        """ Returns the lowercase word with special characters removed  """
        return str(word)\
            .replace('[', '')\
            .replace(']', '')\
            .replace('\\', '')\
            .replace('\"', '')\
            .replace("\'", '')\
            .replace(',', '')

    def get_normalized_result(self):
        return self.normalized_list

    def print_normalized(self):
        return self.normalized_list


if __name__ == '__main__':
    source_arr = read_from(argv[1])
    cleaned_tuple = cleanup_arr(source_arr, reg_expr)
    print(cleaned_tuple)


