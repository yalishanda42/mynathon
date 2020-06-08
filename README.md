# MYTHON

##  Примери
``` python
def factorial(number):
    if number < 0:
        raise ValueError("Е не може с отрицателно число")
    elif number == 0 or number == 1:
        return 1
    else:
        return factorial(number - 1) * number
```

``` mython
нека факториел(число):
    начи ако число < 0:
        маняк искаш да ме направиш ValueError("Е не може с отрицателно число")
    ако пък число == 0 или число == 1:
        готоо майна 1
    иначе:
        готоо майна факториел(число - 1) * число
```
