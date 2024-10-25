massive=[]
other_massive=[]
for i in range(10):
    massive.append(int(input()))
for y in range(len(massive)):
    if massive[y]%2==0:
        if massive[y]<10:
            other_massive.append(massive[y])
if other_massive==[]:
    print("Здесь нет таких чисел")
other_massive.sort()
print(other_massive)
