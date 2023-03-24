"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    6
    -> 5
"""
import random

N = int(input("enter the list length:  "))
list = [random.randint(1, 10) for i in range(N)]
print(list)
x = int(input("enter number to search for:  "))
element_inx = 0
min_element = abs(x - list[0])#             store the minimum value from x-each element.
for i in range(1, N):
    current_element = abs(x -list[i])#     store the value from x-curent element.
    if current_element < min_element:
        min_element = current_element
        element_inx = i #                  store the index of the closest element

print(f"The closest element to the given number =  {list[element_inx]}")




   
       

    


        












