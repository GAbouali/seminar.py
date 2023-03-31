# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
#----------------------
"""

a=int(input('enter number A: '))
b=int(input('enter number B: '))

def rec_sum(a, b):
    a += 1
    b -= 1
    if b > 0:
        return rec_sum(a, b)
    else:
        return a
 
 
print (rec_sum(a, b))
"""

a=int(input('enter number A: '))
b=int(input('enter number B: '))

def rec_sum(a, b):
    if b == 0:
        return a
    else:
        return rec_sum(a + 1, b - 1)

print(rec_sum(a, b)) 