from sentence import Sentence
import os


class Interface(object):
    def __init__(self, alphabet):
        self._alphabet = alphabet
        self._sentence = Sentence(alphabet)
        self._sentence.set_sentence("( P ^ Q ) -> R ")

    def __how_to_use(self):
        print("Alfabeto disponível")
        print(self._alphabet, "\n")

        print("     Operadores disponìveis       ")
        print("| Simbolo |       Operador       |")
        print("|    ^    |      E               |")
        print("|    v    |      OU              |")
        print("|    ->   |      Implicação      |")
        print("|    ->   |      Bi implicação   |")

        print("\nNão se esqueça de saltar um espaço após cada simbolo.")
        print("Exemplo: ( P ^ Q -> R )\n")

        input("Digite ENTER para continuar...")
        os.system("cls||clear")

    def __new_sentence(self):
        sentence_is_valid = False

        sentence = input("Digite a nova sentença: ")
        sentence_is_valid = self._sentence.set_sentence(sentence)

    def __check_if_sentence_is_valid(self):
        print(self._sentence.isValid())
        print(
            "A sentença {} {}.".format(
                self._sentence.sentence_to_string(),
                "é valída" if self._sentence.isValid() else "não é valída",
            )
        )

        input("Digite ENTER para continuar...")
        os.system("cls||clear")

    def __get_sentence_length(self):
        print("[H]: {}".format(self._sentence.length()))

        input("Digite ENTER para continuar...")
        os.system("cls||clear")

    def setup(self):
        print("\nLogíca para Ciência da Computação | IFMG Campus Formiga\n")

        # self.__how_to_use()

        option = 3
        while option != "5":
            print("MENU\n")
            print("1. Nova sentença")
            print("2. Tamanho da sentença")
            print("3. Verificar se sentença valida")
            print("4. Como usar?")
            print("5. Sair")

            print("\nSentença atual: " + self._sentence.sentence_to_string())

            option = input("\nDigite a opção: ")

            os.system("cls||clear")
            if option == "1":
                self.__new_sentence()
            elif option == "2":
                self.__get_sentence_length()
            elif option == "3":
                self.__check_if_sentence_is_valid()
            elif option == "4":
                self.__how_to_use()
