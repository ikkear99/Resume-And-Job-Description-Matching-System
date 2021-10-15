import spacy
import pandas

nlp = spacy.load("en_core_web_lg")


class Extract:
    def __init__(self):
        # The dataframe to make input for model classification
        self.data = pandas.DataFrame([])

    def init_data(self, data: pandas.DataFrame):
        self.data = data

    def remove_sign(self, char: str) -> str:
        """
        Remove the sign of character into english format
        Parameters:
            char: str: The character need to remove sign
        """
        diction = {
            'a': 'àáạảãâầấậẩẫăằắặẳẵ',
            'A': 'ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ',
            'e': 'èéẹẻẽêềếệểễ',
            'E': 'ÈÉẸẺẼÊỀẾỆỂỄ',
            'o': 'òóọỏõôồốộổỗơờớợởỡ',
            'O': 'ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ',
            'i': 'ìíịỉĩ',
            'I': 'ÌÍỊỈĨ',
            'u': 'ùúụủũưừứựửữ',
            'U': 'ƯỪỨỰỬỮÙÚỤỦŨ',
            'y': 'ỳýỵỷỹ',
            'Y': 'ỲÝỴỶỸ',
            'd': 'đ',
            'D': 'Đ'
        }

        if char in diction['a']:
            return 'a'
        elif char in diction['A']:
            return 'A'
        elif char in diction['e']:
            return 'e'
        elif char in diction['E']:
            return 'E'
        elif char in diction['o']:
            return 'o'
        elif char in diction['O']:
            return 'O'
        elif char in diction['i']:
            return 'i'
        elif char in diction['I']:
            return 'I'
        elif char in diction['u']:
            return 'u'
        elif char in diction['U']:
            return 'U'
        elif char in diction['y']:
            return 'y'
        elif char in diction['Y']:
            return 'Y'
        elif char in diction['d']:
            return 'd'
        elif char in diction['D']:
            return 'D'
        else:
            return char

    def modify(self, sentence: str) -> str:
        """
        Delete special character and normal word
        Parameters:
            sentence: str: The sentence need to modify
        """
        try:
            # types_not_delete = ['PRON', 'ADJ']
            # symbols = """~'`!#$%^&*)(_-–=}{][|\:;",.<>? •▪©  """
            char_set = """qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM@ """
            sub_stop_words = ['etc', 'trang 1/', 'trang 2/', 'trang 3/', 'trang 4/', 'trang 5/', \
                              'trang 6/', 'trang 7/', 'trang 8/', 'trang 9/', 'topcvvn', 'male', \
                              'user', 'language', 'a', 'an', 'the', 'at', 'in', 'on', 'out', \
                              'next', 'and', 'of', 'before', 'after', 'i', 'my', 'from', 'to', 'for', \
                              'with', 'is', 'are', 'am', 'was', 'were', 'as', 'it', 'have', 'has', \
                              'etc', 'mycvvn', 'such', 'about', 'like', 'so', 'they', 'them', 'me', \
                              'how', 'who', 'when', 'which', 'by', 'as well as', 'sex']
            not_stop_words = ['front', 'back']
            mod_sentence = ''

            for char in sentence:
                char = self.remove_sign(char)
                if (char in char_set):
                    mod_sentence += char.lower()

            words = mod_sentence.split(" ")
            for i in range(len(words)):
                word = words[i]
                docx = nlp(word)

                if (len(word) == 0 or docx[0].is_stop or (docx[0].text in sub_stop_words)):
                    words[i] = ""
                else:
                    words[i] = docx[0].lemma_

            modified_sentence = " ".join(words)
            return modified_sentence.strip()
        except:
            return None  # to handle the odd case of characters like 'x02', etc.

    def normal(self, sentences: list) -> list:
        """
        return new list which normalized all sentence in sentence list

        Parameters:
            sentences: list: The list contain the sentences
        Returns:
            The new list which normalized
        """

        new_sentences = []
        for sentence in sentences:
            sentence_normal = self.modify(sentence)
            if sentence_normal != None and sentence_normal != '':
                new_sentences.append([sentence_normal])

        return new_sentences
