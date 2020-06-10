# Mynathon - Универсалният програмен език за майни и маняци.

![Build](https://github.com/allexks/mython/workflows/Python%20package/badge.svg)

![Моля](https://media.tenor.com/images/139208d8296e1e01a6e3fc41a14d624d/tenor.gif)

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
* `assert` => `маняк ти иеш ли са`
* `try` => `пробвай майна`
* `except` => `яба гръмна ми`
* `finally` => `кат цяло`
* `pass` => `пас`
* `class` => `клас`
* `def` => `нека`
* `return` => `готоо майна`
* `yield` => `метни му`
* `lambda` => `гърция`
* `from` => `от`
* `import` => `дай ми`
* `as` => `като`
* `with` => `праскай`
* `del` => `мани го тоа бе майна`
* `nonlocal` => `софия`
* `global` => `кичука`
* `await` => `изчакай`
* `async` => `многонишково`

##  Примери
### Пример 1
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
### Пример 2
``` mynathon
от math дай ми sqrt като корен

нека корените_на_квадратно_уравнение(a, b, c):
    ако майна a == 0:
        маняк искаш да ме направиш ValueError("Уравнението не е квадратно!")

    дискриминантата = b*b - 4*a*c
    корен_от_дискриминантата = корен(дискриминантата) ако майна дискриминантата >= 0 иначе корен(-дискриминантата)*1j

    корен1 = (-b - корен_от_дискриминантата) / (2 * a)
    корен2 = (-b + корен_от_дискриминантата) / (2 * a)

    готоо майна корен1, корен2

кор1 = корените_на_квадратно_уравнение(1, -3, 2)
print("x^2 - 3x + 2 = 0 <=> x1 == {0}; x2 == {1}".format(*кор1))

кор2 = корените_на_квадратно_уравнение(1, 2, 5)
print("x^2 + 2x + 5 = 0 <=> x1 == {0}; x2 == {1}".format(*кор2))
```
Кодът е еквивалентен на:
``` python
from math import sqrt as root

def quadratic_roots(a, b, c):
    if a == 0:
        raise ValueError("Уравнението не е квадратно!")

    discriminant = b*b = 4*a*c
    sqrt_discriminant = root(discriminant) if discriminant >= 0 else root(-discriminant)*1j

    root1 = (-b - sqrt_discriminant) / (2 * a)
    root2 = (-b + sqrt_discriminant) / (2 * a)

    return root1, root2

roots1 = quadratic_roots(1, -3, 2)
print("x^2 - 3x + 2 = 0 <=> x1 == {0}; x2 == {1}".format(*roots1))

roots2 = quadratic_roots(1, 2, 5)
print("x^2 + 2x + 5 = 0 <=> x1 == {0}; x2 == {1}".format(*roots2))
```
