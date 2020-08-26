# Boolean Algebra

Projeto desenvolvido na disciplina Lógica para Ciência da Computação.

#### Iniciando

```python
from Sentence import Sentence

# alphabet that will be considered for the validation of sentences
alphabet = ["P", "Q", "R"]

# use white space in each sentence item
ex_1 = " ~ P  ^ ( P ^ Q ( Q <-> R ) )"
ex_2 = " ~ P  ^ ( P ^ Q ( Q <-> R ) "

sentence_1 = Sentence(alphabet, ex_1)
sentence_2 = Sentence(alphabet, ex_2)

sentence_1.isValid() # True
sentence_1.length() # 9

sentence_2.isValid() # False
sentence_2.isValid() # 0
```
