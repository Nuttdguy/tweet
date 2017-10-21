from sys import argv
from os import getcwd


class Read():
    """ Class for reading document and returning an array """

    input_instruction = "Document to open?"
    input_instruction_loc = "Please make sure the file is located in:\n" + getcwd() + '/assets/'

    def __init__(self, source_path=None, mode='r'):
        if source_path:
            self.read_from(source_path, mode)

    def source_input_prompt():
        """ Returns the path of the source document from input prompt """
        # print(), 
        # print(input_instruction_loc), 
        # print(input_instruction)
        path = getcwd() + '/' + input()
        return path


    def read_from(self, source_path, mode='r'):
        """ Returns an array of words from file input """
        self.document_array = []
        try:
            with open(source_path, mode=mode) as document:
                for line in document:
                    self.document_array.append(line.replace('\n', '').split(' '))
            document.close()
        except OSError:
            return 'Cannot open file, was the extension added, e.g. .txt, .rtf, or in correct directory'

    def get_document_arr(self):
        return self.document_array