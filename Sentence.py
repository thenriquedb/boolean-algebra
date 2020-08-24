from collections import Counter


class Sentence(object):
    def __init__(self, alphabet, sentence):
        self._alphabet = alphabet
        self._operators = {
            "~": "NOT",
            "^": "AND",
            "v": "OR",
            "->": "IMPLY",
            "<->": "XNOR",
        }

        self.symbols = ["(", ")"]
        self._sentence = self.__convert(sentence)

    def get_alphabet(self):
        return self._alphabet

    def __convert(self, sentence: str):
        converted_sentence = []

        for el in sentence.split():
            if el in self._operators or el in self._alphabet or el in self.symbols:
                if el in self._operators:
                    converted_sentence.append(self._operators[el])
                else:
                    converted_sentence.append(el)
            else:
                return []

        return converted_sentence

    def __check_parenthesis(self):
        all_parenthesis = []

        for el in self._sentence:
            if el in self.symbols:
                all_parenthesis.append(el)

        parenthesis_count = Counter(all_parenthesis)
        if parenthesis_count["("] != parenthesis_count[")"]:
            return False

        # Checks open and close parenthesis
        for i in range(len(self._sentence)):
            if i != len(self._sentence) - 1:
                if (
                    self._sentence[i] in self.symbols
                    and self._sentence[i + 1] in self.symbols
                ):
                    return False

        # Check parenthesis content TODO
        return True

    # Checks if the sentence has a logical operator followed by another
    def __check_logical_operators(self):
        for i in range(len(self._sentence)):
            if i != len(self._sentence) - 1:
                if (
                    self._sentence[i] in self._operators.values()
                    and self._sentence[i + 1] in self._operators.values()
                ):
                    return False
        return True

    def length(self):
        if len(self._sentence) == 0:
            return None

        length = 0

        for el in self._sentence.split():
            if el in self._alphabet or el in self._operators:
                length = length + 1

        return length

    def isValid(self):
        # Check sentence length
        if len(self._sentence) == 0 or len(self._sentence) > 12:
            return False

        if not self.__check_parenthesis():
            return False

        if not self.__check_logical_operators():
            return False

        return True
