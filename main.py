from Sentence import Sentence

if __name__ == "__main__":
    alphabet = ["P", "Q", "R"]
    sentence_1 = " ~ P  ^ (P ^ Q ( Q <-> R ) )"

    sentence = Sentence(alphabet, sentence_1)
    print(sentence._sentence)

    isValid = sentence.isValid()
    print(isValid)
    print(sentence.length())
