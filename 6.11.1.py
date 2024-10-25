list=[]
max=0
for i in range(10):
    list.append(int(input()))
for y in range(len(list)):
    if list[y]%2==0:
        if list[y]>max:
            max=list[y]
print("Максимальное четное число: ",max)
