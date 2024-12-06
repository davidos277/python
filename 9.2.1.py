def find():
    num=int(input("Введите числа: "))
    if num==0:
         return 0
    else:
        max_num=find()
        if max_num>num:
            return max_num
        else:
            return num

c=find()
print("Максимально число равно: ",c) 
