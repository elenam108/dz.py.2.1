#На столе лежат n монеток. Некоторые из них лежат вверх 
#решкой, а некоторые – гербом. Определите минимальное 
#число монеток, которые нужно перевернуть, чтобы все 
#монетки были повернуты вверх одной и той же стороной.


from random import randint

gerb = 0
resh = 0
list1 = list()
for i in range(5):
    list1.append(randint(0,1))

print(list1)
for i in list1:
    if i == 0:
        gerb += 1
    else:
        resh += 1

print(min(gerb, resh))