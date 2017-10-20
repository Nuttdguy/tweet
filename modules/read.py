from sys import argv
from os import getcwd


""" Module for reading document and returning an array """

input_instruction = "Document to open?"
input_instruction_loc = "Please make sure the file is located in:\n" + getcwd() + '/assets/'


def source_input_prompt():
    """ Returns the path of the source document from input prompt """
    print(), print(input_instruction_loc), print(input_instruction)
    path = getcwd() + '/' + input()
    return path


def read_from(path, mode='r'):
    """ Returns an array of words from file input """
    document_array = []
    try:
        with open(path, mode=mode) as document:
            for line in document:
                document_array.append(line.replace('\n', '').split(' '))
        document.close()
    except OSError:
        return 'Cannot open file, was the extension added, e.g. .txt, .rtf, or in correct directory'

    return document_array


if __name__ == '__main__':
    doc = read_from(argv[1])
    print(doc)

