# MYTHON

![Build](https://github.com/allexks/mython/workflows/Python%20package/badge.svg)

## Ключови думи
* `True` => `трю`
* `False` => `бомбок`
* `and` => `и`
* `or` => `или`
* `not` => `не`
* `is` => `е`
* `None` => `нищо`
* `if` => `начи ако`
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
* `del` => `мани го тоа е майна`
* `nonlocal` => `софия`
* `global` => `асеновград`
* `await` => `изчакай`
* `async` => `многонишково`

##  Примери
``` mython
нека факториел(число):
    начи ако число < 0:
        маняк искаш да ме направиш ValueError("Е не може с отрицателно число")
    ако пък число == 0 или число == 1:
        готоо майна 1
    иначе:
        готоо майна факториел(число - 1) * число
```

``` python
def factorial(number):
    if number < 0:
        raise ValueError("Е не може с отрицателно число")
    elif number == 0 or number == 1:
        return 1
    else:
        return factorial(number - 1) * number
```
