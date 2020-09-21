from collections import Counter
import itertools
import pandas as pd
import numpy as np
import re
from distutils.util import strtobool

pd.set_option("display.max_rows", 1024)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)

"""
Convert "True" and "False" for boolean

Args:
    string

Returns:
    boolean or string
"""


def str_to_bool(string):
    try:
        string = bool(strtobool(string))
    except ValueError:
        pass
    return string


"""
 Recursively applies a map function to a list and all sublists.
 
 Args:
    func: function that will be applied
    data: list items
"""


def recursive_map(func, data):
    if isinstance(data, list):
        return [recursive_map(func, elem) for elem in data]
    else:
        return func(data)


class Sentence(object):
    def __init__(self, alphabet: list):
        self._alphabet = alphabet
        # Use logical equivalences
        # https://en.wikipedia.org/wiki/Logical_equivalence
        self._operators = {
            "!": (lambda p: not p),
            "^": (lambda p, q: p and q),
            "v": (lambda p, q: p or q),
            "->": (lambda p, q: not p or q),
            "<->": (lambda p, q: p == q),
        }

        self._symbols = ["(", ")"]
        self._sentence = []
        self._sentence_str = ""

    def set_sentence(self, sentence: str):
        self._sentence = self.__tokenize(sentence)
        self._sentence_str = sentence

    def get_sentence(self):
        return self._sentence

    """
    Return string from current sentence
    
    Returns:
        string 
    """

    def sentence_to_string(self):
        return self._sentence_str

    def get_alphabet(self):
        return self._alphabet

    """
    The length of a formula is obtained by counting the connectives and the 
    truth and propositional symbols, disregarding the punctuation symbol.
    
    Returns:
        length (int): sentence length
    """

    def length(self):
        if len(self._sentence) == 0:
            return 0

        length = 0
        for el in self._sentence:
            if el not in self._symbols:
                length = length + 1

        return length

    """
    Check if sentence is valid
    
    Returns:
        boolean
    """

    def isValid(self):
        if len(self._sentence) == 0:
            return False

        if not self.__check_logical_operators():
            return False

        if not self.__check_parentheses():
            return False

        return True

    def __tokenize(self, sentence: str):
        converted_sentence = []

        for el in sentence.split():
            if el in self._operators or el in self._alphabet or el in self._symbols:
                if el in self._operators:
                    converted_sentence.append(el)
                else:
                    converted_sentence.append(el.strip())
            else:
                return []

        return converted_sentence

    """
    Check if the formula's parentheses are correct
    
    Returns:
        boolean
    """

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

    """
    Checks if the sentence has a logical operator followed by another
    
    Returns:
        boolean
    """

    def __check_logical_operators(self):
        for i in range(len(self._sentence)):
            if i != len(self._sentence) - 1:
                if (
                    self._sentence[i] in self._operators
                    and self._sentence[i + 1] in self._operators
                ):
                    return False
        return True

    """
    Args:
        sentence (list): split sentence
    
    Returns:
        sentence: split sentence
    """

    def __sub_sentences(self, sentence):
        if isinstance(sentence, list):
            for operator in ["!"]:
                while operator in sentence:
                    index = sentence.index(operator)
                    sentence[index] = [
                        operator,
                        self.__sub_sentences(sentence[index + 1]),
                    ]
                    sentence.pop(index + 1)

            for operator in ["^"]:
                while operator in sentence:
                    index = sentence.index(operator)
                    sentence[index] = [
                        self.__sub_sentences(sentence[index - 1]),
                        operator,
                        self.__sub_sentences(sentence[index + 1]),
                    ]
                    sentence.pop(index + 1)
                    sentence.pop(index - 1)

            for operator in ["v"]:
                while operator in sentence:
                    index = sentence.index(operator)
                    sentence[index] = [
                        self.__sub_sentences(sentence[index - 1]),
                        operator,
                        self.__sub_sentences(sentence[index + 1]),
                    ]
                    sentence.pop(index + 1)
                    sentence.pop(index - 1)

            for operator in ["->"]:
                while operator in sentence:
                    index = sentence.index(operator)
                    sentence[index] = [
                        self.__sub_sentences(sentence[index - 1]),
                        operator,
                        self.__sub_sentences(sentence[index + 1]),
                    ]
                    sentence.pop(index + 1)
                    sentence.pop(index - 1)

            for operator in ["<->"]:
                while operator in sentence:
                    index = sentence.index(operator)
                    sentence[index] = [
                        self.__sub_sentences(sentence[index - 1]),
                        operator,
                        self.__sub_sentences(sentence[index + 1]),
                    ]
                    sentence.pop(index + 1)
                    sentence.pop(index - 1)

        return sentence

    """
    Recursively evaluates a logical sentence that has been grouped into
    sublists where each list is one operation.
    
    Args:
        sentence (bool or list)
    """

    def __solve_sentence(self, sentence):
        if isinstance(sentence, bool):
            return sentence
        if isinstance(sentence, list):
            # list with just a list in it
            if len(sentence) == 1:
                return self.__solve_sentence(sentence[0])
            # single operand operation
            if len(sentence) == 2:
                return self._operators[sentence[0]](self.__solve_sentence(sentence[1]))
            else:
                return self._operators[sentence[1]](
                    self.__solve_sentence(sentence[0]),
                    self.__solve_sentence(sentence[2]),
                )

    """
    Generate a table truth of sentence
    
    Returns:
        table: Pandas DataFrame
    
    """

    def truth_table(self):
        # save variables of sentencees
        variables = filter(lambda var: var in self._alphabet, self._sentence)
        variables = list(set(variables))

        n_rows = pow(2, len(variables))
        n_cols = len(variables) + 1

        # calculates all possible combinations between variables
        table = itertools.product([True, False], repeat=len(variables))
        table = pd.DataFrame(table)
        table[self._sentence_str] = [True] * n_rows

        table.columns = [*variables, self._sentence_str]

        # calculates the Boolean value for each row in the column
        for index, row in table.iterrows():
            replaced = self._sentence_str

            # replaces variables with corresponding Boolean values
            for variable in variables:
                replaced = re.sub("[" + variable + "]", str(row[variable]), replaced)

            # convert "True" and "False" for boolean
            replaced = replaced.split(" ")
            replaced = recursive_map(str_to_bool, replaced)

            sentence = self.__sub_sentences(replaced)

            resolved = self.__solve_sentence(sentence)
            table.at[index, self._sentence_str] = resolved

        return table
