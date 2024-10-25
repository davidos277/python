a=int(input('Введите целое значение переменной A:'))
b=int(input('Введите целое значение переменной B:'))
if a>b:
    for i in range(b,a+1):
        print(i,end=";")
elif a<b:
    for i in range(a,b+1):
        print(i,end=";")

