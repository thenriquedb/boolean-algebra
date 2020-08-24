from Sentence import Sentence

if __name__ == "__main__":
    alphabet = ["P", "Q", "R"]
    sentence_1 = "( ~ P ^ ( Q <-> R ) "

    sentence = Sentence(alphabet, sentence_1)

    isValid = sentence.isValid()
    print(isValid)
