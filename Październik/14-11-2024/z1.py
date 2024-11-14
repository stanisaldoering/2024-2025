p="dane_systemy1.txt"
t1=[]
with open(p,'r') as file:
    for i in file:
        t1.append(i.strip())
    print(t1)

for j in t1:
    x=mi