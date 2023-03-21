"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

n=int(input('enter number: '))
res=1
i=0
while res < n:
    res=res*2
    i=i+1
    if res<n:
        print(res, end=' ')

