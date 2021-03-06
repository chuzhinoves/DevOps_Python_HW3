"""
Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""

def my_func(x, y):
    if y>=0:
        raise ValueError("степень должна быть отрицательна")
    P=1
    for i in range(-y):
        P *= x
    return 1/P
        