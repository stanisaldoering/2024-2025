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
for i, j in enumerate(tmplist):
    if i%7==0:
        pt.append(j)
    if i%7==1:
        sb.append(j)
sredniapt=sum(pt)/len(pt)
sredniasb=sum(sb)/len(sb)
print(sredniapt)
print(sredniasb)

for z in range(7):
    d=[]
    for i,j in enumerate(tmplist):
        if i %7 ==z:
            d.append(j)
    srednia=sum(d)/len(d)
    print(srednia)

 # w jakim okresie podaj daty wystapił najdluszy ciagnik w ktorym teperatatura byla nizsza w niz w dniu poprzednim podaj taki okres
p=[]
for k in dane.items():
    p.append(k)
print(p)

data=[]
tmp = []
for n in range(len(p)-1):
    if p[n][1]>p[n+1][1]:
        tmp.append(p[n])
    else:
        if len(data) < len(tmp):
            data = tmp
            tmp = []
        else:
            tmp = []
print(data)
# podaj ile dni w miesiacu kwietniu jest temperatura wyzsza od temeratury dzien wczesniej
kw=[]
a='4'
for i in range(len(p)-1):
    if a is p[i]:
        kw.append(p[i])
print(kw)

