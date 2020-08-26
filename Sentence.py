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

        self._symbols = ["(", ")"]
        self._sentence = self.__tokenize(sentence)

    def get_alphabet(self):
        return self._alphabet

    def __tokenize(self, sentence: str):
        converted_sentence = []

        for el in sentence.split():
            if el in self._operators or el in self._alphabet or el in self._symbols:
                if el in self._operators:
                    converted_sentence.append(" " + self._operators[el] + " ")
                else:
                    converted_sentence.append(" " + el + " ")
            else:
                return []

        return converted_sentence

    def __check_parentheses(self):
        parenthesis_count = Counter(self._sentence)
        if parenthesis_count["("] != parenthesis_count[")"]:
            return False

        reverse_sentence = self._sentence[::-1]

        for i, elm in enumerate(self._sentence):
            if elm == "(":
                startIndex = i

                for j, sub in enumerate(reverse_sentence):
                    if sub == ")":
                        # [1 , 2 , 3, 4] - [4, 3, 2, 1]
                        # i === (SENTENCE_SIZE - i) - 1
                        endIndex = (len(self._sentence) - 1) - j
                        content = self._sentence[startIndex:endIndex]

                        # Check if parentheses are empty
                        if len(content) == 1:
                            return False

                        break

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
            return 0

        length = 0

        for el in self._sentence:
            if el in self._alphabet or el in self._operators.values():
                length = length + 1

        return length

    def isValid(self):
        if len(self._sentence) == 0:
            return False

        if not self.__check_logical_operators():
            return False

        if not self.__check_parentheses():
            return False

        return True
