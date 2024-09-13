p='imiona.txt'
i=[]
with open(p,'r')as file:
    for j in file:
        i.append(j.strip())
    print(i)