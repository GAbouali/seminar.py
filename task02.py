# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
# ----------------------------

n = int(input('enter a number: '))
sum = 0
while (n != 0):
    sum = sum + n % 10
    n= n//10
print('the sume of digit number = ' , sum)
