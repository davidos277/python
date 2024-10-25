n=int(input("Введите число"))
def bliznech(n):
    for i in range(n,n*2):
        if i<=((n*2)-2):
            print(f'[{i},{i+2}]')
print(bliznech(n))
