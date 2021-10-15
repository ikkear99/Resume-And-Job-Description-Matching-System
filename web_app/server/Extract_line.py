from Extract import *

class Extract_line(Extract):
    def __init__(self):
        super(Extract_line, self).__init__()

    def extract_line(self):
        """
        Extract all lines in the pdf cv file
        """

        lines = self.data.values.flat[:]
        text = ""
        for line in lines:
            text = text + "\n" + line

        # Remove the spaces have length > 1
        text = text.replace("  ", " ")
        new_lines = text.split("\n")
        new_lines = self.normal(new_lines)
        self.data = pandas.DataFrame(new_lines)
