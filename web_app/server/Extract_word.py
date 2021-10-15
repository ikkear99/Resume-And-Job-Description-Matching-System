from Extract import *


class Extract_word(Extract):

    def __init__(self):
        super(Extract_word, self).__init__()

    def normal(self, words: list) -> list:
        """
        Normalize all sentence in sentence list
        Parameters:
            words: list: The list contain the words

        Returns: list
            The new list which normalized
        """

        new_words = []

        for word in words:
            word_normal = self.modify(word)
            if word_normal != None and word_normal != '':
                new_words.append(word_normal)

        return new_words

    def extract_word(self):
        """
        Extract all word from the pdf cv file
        """

        lines = self.data.values.flat[:]

        text = ""
        for line in lines:
            text = text + " " + line

        text = text.replace("\n", " ")
        words = text.split(" ")
        words = self.normal(words)
        self.data = words
