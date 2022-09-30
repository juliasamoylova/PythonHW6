# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math

def fact(n: int) -> list:
    li = [i for i in range(1, n+1)]
    fact = list(map(lambda x: math.factorial(x), li))
    return fact

print(fact(4))

