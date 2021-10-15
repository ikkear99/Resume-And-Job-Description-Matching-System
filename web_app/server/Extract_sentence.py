from Extract import *

class Extract_sentence(Extract):
    def __init__(self):
        super(Extract_sentence, self).__init__()
        # All lines in the cv file
        self.lines = []

    def normalize(self):
        """
        Remove special character and replace it by a space line
        """

        # The valid start character set
        charset = '''1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'''

        self.lines = self.data.values.flat[:]
        new_lines = []

        for line in self.lines:
            if line != "\n":
                line = line.strip()
                if len(line) == 0:
                    new_lines.append("\n")
                elif line[0] not in charset:
                    line = line[1:].strip()
                    new_lines.append("\n" + line + "\n")
                else:
                    new_lines.append(line + "\n")
            else:
                new_lines.append(line)

        self.data = pandas.DataFrame(new_lines)
        self.lines = new_lines

    def clusterSentence(self):
        """
        Cluster the near lines or spaced 1 space line
        """

        length = len(self.lines)
        new_lines = []

        for i in range(length - 1):
            if (self.lines[i] != "\n"):
                new_lines.append(self.lines[i])
            elif self.lines[i + 1] == "\n":
                new_lines.append("\n")

        self.data = pandas.DataFrame(new_lines)
        self.lines = new_lines

    def extractSentence(self):
        """
        Extract all sentences from the pdf cv file

        """
        text = ""
        for line in self.lines:
            text = text + line

        # Remove the redundant space line
        while "\n\n\n" in self.lines:
            text = text.replace("\n\n\n", "\n\n")

        # Extract the sentence
        sentences = text.split("\n\n")
        for i in range(len(sentences)):
            sentences[i] = sentences[i].replace("\n", " ")
        sentences = self.normal(sentences)
        self.data = pandas.DataFrame(sentences)