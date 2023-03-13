
n = input('enter 6 digit number: ')
a = int(n[0]+n[1]+n[2])
b = int(n[3]+n[4]+n[5])

sumA = 0
sumB = 0
while (a != 0):
    sumA = sumA + a % 10
    a = a//10
while (b != 0):
    sumB = sumB + b % 10
    b = b//10
if (sumA == sumB):
    print('yes')
else:
    print('no')
