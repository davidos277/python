text=input("Введите предложение: ")
number_n=0
max=0
for i in text:
    if i=="н":
        number_n=number_n+1
    else:
        if number_n>max:
            max=number_n
            number_n=0
if number_n>max:
    max=number_n
text1=text.replace("!",".")
print(text1)
print(max)
