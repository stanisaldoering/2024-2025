def pobieranie():
    temperatura={}
    with open ("temperatura.txt", 'r') as file:
        for line in file:
            tmp=int(line[11::].strip())
            temperatura.update({line[0:10]: tmp})
    return temperatura

# podaj maskymalna dlugosc okresu wzrastania temperatury w podanym czasie

dane=pobieranie()
print(dane)
tmplist=[]
t=[]
for i in dane.values():
    tmplist.append(i)

iloscdni=0
tmpIloscdni=1
for i in range(len(tmplist)-1):
    if tmplist[i]<= tmplist[i+1]:
        tmpIloscdni+=1
    else:
        if iloscdni < tmpIloscdni:
            iloscdni=tmpIloscdni
        tmpIloscdni=1
print(iloscdni)

# ile bylo dni w ktorych temperatura powietrza byla mniejsza niz srednia temperatura w calym okresie
srednia=sum(tmplist)/ len(tmplist)
print(srednia)
t=[]
for i in tmplist:
    if i<srednia:
        t.append(i)
print(len(t))

# oblicz srednie temepratury w poszczegolnych dniach tygdinia
pn=[]
wt=[]
sr=[]
czw=[]
pt=[]
sb=[]
ndz=[]

pt.append(tmplist[0]+7)
