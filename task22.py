# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
import random

n = int(input("enter the 1st list length:  "))
m = int(input("enter the 2nd list length:  "))
list_n = [random.randint(1, 10) for i in range(n)]
list_m = [random.randint(1, 10) for i in range(m)]
print('list_n =', list_n,)
print('list_m =', list_m)
list_total=list_m+list_n
print('list n+m =',list_total)
list_n=set(list_total)
print('the set of elements in n+m in sorted way =',sorted(list_total))




