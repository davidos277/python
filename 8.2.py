#Создаем матрицу
n=3
B=[]
print("Введите массив")
for i in range(n):
    A=[]
    for i in range(n):
        A.append(int(input()))
    B.append(A)
#Выводим матрицу
print("Исходный массив:")
for i in range (n):
    for j in range(n):
        print(B[i][j], end=" ")
    print()        
#Работа с матрицой
maximum1=B[0][0]
minimum1=B[0][0]
maximum2=B[1][0]
minimum2=B[1][0]
maximum3=B[2][0]
minimum3=B[2][0]
for i in range(n):
    for j in range(n):
        if maximum1<B[0][j]:
            maximum1=B[0][j]
        if minimum1>B[0][j]:
            minimum1=B[0][j]
        if maximum2<B[1][j]:
            maximum2=B[1][j]    
        if minimum2>B[1][j]:
            minimum2=B[1][j]    
        if maximum3<B[2][j]:
            maximum3=B[2][j]
        if minimum3>B[2][j]:
            minimum3=B[2][j]
B[0][0]=maximum1
B[0][2]=minimum1
B[1][0]=maximum2
B[1][2]=minimum2
B[2][0]=maximum3
B[2][2]=minimum3
#Вывод изменненой матрицы
print("Измененный массив")
for i in range (n):
    for j in range(n):
        print(B[i][j], end=" ")
    print()        