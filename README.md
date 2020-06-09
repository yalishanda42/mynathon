# Mynathon - Езикът за програмиране за майни и маняци.

![Build](https://github.com/allexks/mython/workflows/Python%20package/badge.svg)

## Ключови думи
* `True` => `трю`
* `False` => `бомбок`
* `and` => `и`
* `or` => `или`
* `not` => `не`
* `is` => `е`
* `None` => `нищо`
* `if` => `ако майна`
* `elif` => `ако пък`
* `else` => `иначе`
* `for` => `начи за`
* `in` => `пробягващо`
* `while` => `начи майна`
* `break` => `скандал`
* `continue` => `дайму още`
* `raise` => `маняк искаш да ме направиш`
* `assert` => `маняк ти ибеш ли са`
* `try` => `пробвай майна`
* `except` => `яба гръмна ми`
* `finally` => `кат цяло`
* `pass` => `пас`
* `class` => `клас`
* `def` => `нека`
* `return` => `готоо майна`
* `yield` => `метни му`
* `lambda` => `хаскелче`
* `from` => `от`
* `import` => `дай ми`
* `as` => `като`
* `with` => `праскай`
* `del` => `мани го тоа бе майна`
* `nonlocal` => `софия`
* `global` => `асеновград`
* `await` => `изчакай`
* `async` => `многонишково`

##  Примери
``` mynathon
нека факториел(число):
    ако майна число < 0:
        маняк искаш да ме направиш ValueError("Е не може с отрицателно число")
    ако пък число == 0 или число == 1:
        готоо майна 1
    иначе:
        готоо майна факториел(число - 1) * число

print(f"Факториелът на 3 е {факториел(3)}, а на нула е {факториел(0)}")

пробвай майна:
    променлива = факториел(-1)
яба гръмна ми Exception като нещо:
    print(нещо)
кат цяло:
    print("Готов си")
```
Кодът е еквивалентен на:
``` python
def factorial(number):
    if number < 0:
        raise ValueError("Е не може с отрицателно число")
    elif number == 0 or number == 1:
        return 1
    else:
        return factorial(number - 1) * number

print(f"Факториелът на 3 е {factorial(3)}, а на нула е {factorial(0)}")

try:
    var = factorial(-1)
except Exception e:
    print(e)
finally:
    print("Готов си")
```
