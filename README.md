# Boolean Algebra

Projeto desenvolvido na disciplina Lógica para Ciência da Computação.

### Funcionamento

```python
from Sentence import Sentence

# alphabet that will be considered for the validation of sentences
alphabet = ["P", "Q", "R"]

# use white space in each sentence item
ex_1 = " ! P  ^ ( P ^ Q ( Q <-> R ) )"
ex_2 = " ! P  ^ ( P ^ Q ( Q <-> R ) "

sentence = Sentence(alphabet)

sentence.set_sentence(ex_1)
sentence.isValid() # True
sentence.length() # 9

sentence.set_sentence(ex_2)
sentence.isValid() # False
sentence.isValid() # 0

# Truth table
sentence.set_sentence("p ^ q v s")
print(sentence.truth_table())
#        q      s      p  p ^ q v s
# 0   True   True   True       True
# 1   True   True  False       True
# 2   True  False   True       True
# 3   True  False  False      False
# 4  False   True   True       True
# 5  False   True  False       True
# 6  False  False   True      False
# 7  False  False  False      False
```

### Todo

- [ ] Validar paretênses quando for resolver a sentença

### Como executar?

```
git clone https://github.com/thenriquedb/boolean-algebra.git
cd boolean-algebra && python3 src/main.py
```

### Créditos

Foi utilizados trechos de código do projeto **[truth-table-generator](https://github.com/chicolucio/truth-table-generator)** do usuário **[chicolucio](https://github.com/chicolucio)**.
