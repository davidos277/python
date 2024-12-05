#Создаем матрицу
n=3
A=[]
for i in range(n):
    B=[]
    for i in range(n):
        B.append(int(input()))
    A.append(B)
#Выводим матрицу
print("Массив:")
for i in range (n):
    for j in range(n):
        print(A[i][j], end=" ")
    print()          
#Работа с матрицой
summ=0
number=0    
if A[0][1]>=0:
    summ=summ+A[0][1]
    number=number+1
if A[0][2]>=0:
    summ=summ+A[0][2]
    number=number+1   
if A[1][2]>=0:
    summ=summ+A[1][2]
    number=number+1
print("Сумма значений:",summ) 
print("Сумма чисел",number)