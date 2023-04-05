

list1 = [-5, 9, 0, 3, -1, -2, 1,4, -2, 10, 2, 0, -9, 8, 10, -9,0, -5, -5, 7]
min_n = int(input('enter the min number: '))
max_n = int(input('enter the max number: '))
list2 = []
i = 0

while i < len(list1):
    if max_n >list1[i] >= min_n:
        list2.append(i)
        i += 1
    else:
        i += 1


print(list2)
