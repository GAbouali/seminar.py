"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число X
"""
import random
x=int(input('enter a number to search for: '))
n=int(input('enter the length of massiv: '))
my_list=[random.randint(0,10) for i in range (n)] 
print(my_list)
count_1=0
for i in range (n):
    if my_list[i]==x:
        count_1+=1
print(count_1)        


