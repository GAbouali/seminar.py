# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
# с помощью рекурсии.

# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
import math
# --------------------------
"""
"""

a = int(input('enter number A: '))
b = int(input('enter number B: '))
def find_power(a, b):
    i = 0
    res = 1
    while i < b:
        res *= a
        i += 1
    return res

print(find_power(a,b))