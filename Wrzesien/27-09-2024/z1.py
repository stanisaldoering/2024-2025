d={'a':20,'b':10,'c':15}
print(d.get('b'))
if d.get('z')!=None:
    print("instnieje")
else:
    print('Brak w gitcie')


g={'a':20,'b':10,'c':15}
p=list(g.items())
print(p)
print(p[0])
print(p[1][1])
#stasiu to cygan
g.pop('b')
print(g)
x={'a':10,'b':40,'c':100}
y={'b':1000,'d':1000000}
print(x)
x.update(y)
print(x)

geny={}
with open('dane_geny.txt') as file:
    for index, line in enumerate(file):
        geny.update({index:line.strip()})
        print(index,line)
