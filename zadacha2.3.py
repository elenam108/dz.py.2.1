#Требуется найти наименьший натуральный делитель целого 
#числа N, отличный от 1.

n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0:
        print(i)
        flag = False
    i += 1