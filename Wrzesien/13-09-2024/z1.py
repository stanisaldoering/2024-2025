# dane z pliku
plik='dane.txt'
l=[]
with open(plik, 'r') as file:
    for line in file:
        l.append(int(line))
    print((l))
    print(line)

p='imiona.txt'
i=[]
with open(p,'r')as file:
    for j in file:
        i.append(j.strip())
    print(i)