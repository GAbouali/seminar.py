#                                                             З а д а ч а _  10: 
#На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведит
#-------------------------------------------------------------------------

from random import randint
total_monetok = int(input('enter the coins total:  '))
gerb_total=0
reshkoy_total=0
for _ in range (total_monetok):

    current_monetok=randint(0,1)
    print(current_monetok, end=' ')
    if current_monetok==0:
        gerb_total+=1
    if current_monetok==1:
        reshkoy_total+=1
print(f'\ngerb = ',gerb_total, '--- reshkoy = ',reshkoy_total)            
if gerb_total<total_monetok/2:
         res=gerb_total
elif reshkoy_total<total_monetok/2:
         res=reshkoy_total
elif gerb_total==reshkoy_total:
      res=('gerb total = reshkoy total')
    
print(f'\ntotal coins need to be turned over = ',res)



