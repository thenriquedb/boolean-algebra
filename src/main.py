from interface import Interface
from sentence import Sentence

# from truth_table import TruthTable

if __name__ == "__main__":
    alphabet = ["p", "q", "r", "s"]

    sentence = Sentence(alphabet)

    interface = Interface(alphabet)
    interface.setup()
