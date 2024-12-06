a=int(input("Введите a: "))
b=int(input("Введите b: "))
def division(a,b):
    if a<=b:
        return a  
    else:
        return division(a-b,b)
c=division(a,b)    
print("Остаток: ",c)    
    