# Boolean Algebra

Projeto desenvolvido na disciplina Lógica para Ciência da Computação.

### Funcionamento

```python
from Sentence import Sentence

# alphabet that will be considered for the validation of sentences
alphabet = ["P", "Q", "R"]

# use white space in each sentence item
ex_1 = " ~ P  ^ ( P ^ Q ( Q <-> R ) )"
ex_2 = " ~ P  ^ ( P ^ Q ( Q <-> R ) "

sentence = Sentence(alphabet)

sentence.set_sentence(ex_1)
sentence.isValid() # True
sentence.length() # 9

sentence.set_sentence(ex_2)
sentence.isValid() # False
sentence.isValid() # 0
```

### Como executar?

```
git clone https://github.com/thenriquedb/boolean-algebra.git
cd boolean-algebra && python3 src/main.py
```
