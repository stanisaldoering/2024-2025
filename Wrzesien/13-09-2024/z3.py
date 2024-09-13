o='owoce.txt'
lista=[]
with open(o,'r')as file:
    for i in file:
        lista.append(i.strip())

l2=[]
for j in lista:
    if j==j[::-1]:
        print(j)
    else:
        if j.count("a") >=2:
            print(j)