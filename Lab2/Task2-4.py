import re


class Text:
    def __init__(self, file):
        try:
            self._file = file
        except(EOFError, IOError, FileExistsError, FileNotFoundError):
            raise Exception("The file does not exist")

    def characters_counting(self):
        try:
            text = open(self._file, 'r')
        except(EOFError, IOError, FileExistsError, FileNotFoundError):
            raise Exception("The file can't be opened")
        count = sum(len(line) for line in text)
        text.close()
        return count

    def words_counting(self):
        text = open(self._file, 'r')
        count = sum(len(list(filter(lambda x: x, re.split(r'[, \n]+', line)))) for line in text)
        text.close()
        return count

    def sentence_counting(self):
        try:
            text = open(self._file, 'r')
        except(EOFError, IOError, FileExistsError, FileNotFoundError):
            raise Exception("The file can't be opened")
        help_list = list(line.replace('!?', '.').replace('?!', '.').replace('...', '.').replace('?\n', '?').replace('.\n', '.') for line in text)
        count = sum(len(list(filter(lambda x: x != '', re.split(r'[.!?]', line)))) for line in help_list)
        text.close()
        return count

    def __str__(self):
        return f'Characters: {text.characters_counting()}, Words: {text.words_counting()}, Sentences: {text.sentence_counting()}'


try:
    text = Text('Task_2.txt')
    print(text)
except UnboundLocalError:
    raise Exception("The file does not exist")
