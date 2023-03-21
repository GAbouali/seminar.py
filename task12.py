
"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две 
подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
 
 x=?
 y=?
 sum_numbers=x+y
 product_numbers=x*y
 sum_nums= int(input('enter x+y = '))
 product_nums= int(input('enter x*y = '))
"""
# Define constants
x = 1
y = 1000
# Get sum and product from the patia
sum_nums = int(input('enter x+y = '))
product_nums = int(input('enter x*y = '))

# loop from 1 to 1000 to get x and y 
for i in range(x, y+1):
    j = sum_nums - i
    if i * j == product_nums:
        print("The x & y are:", i, "&", j)
        break
else:
    print("Sorry, we couldn't find the numbers.")
