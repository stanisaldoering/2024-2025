# 1 Napisz funkcję parzyste_liczby, która przyjmuje listę liczb całkowitych i
# zwraca nową listę zawierającą tylko liczby parzyste z pierwotnej listy.
import random
liczby=[]
for i in range(10):
    l=random.randint(0,100)
    liczby.append(l)
print(liczby)
p=[]
def parzyste():
    for i in liczby:
        if i%2==0:
            p.append(i)
    return p
print(parzyste())

# 2. Napisz program, który poprosi użytkownika
# o wprowadzenie 5 liczb, a następnie wyświetli je w porządku malejącym w liście.
lista=[]
for i in range(1,6):
    liczby=int(input("podaj liczbe"))
    lista.append(liczby)
lista.sort(reverse=True)
print(lista)
# 3napisz funlcje suma która przyjmuje liste zawierajaca inne listy z liczbami całkowitymi i zwraca sume wszystkich liczb
suma=0
listaaa=[[1,2,3],[4,5,6],[5,5,5]]
for podlista in listaaa:
    for i in podlista:
        suma+=i
print(suma)


# 4. Napisz program, który utworzy krotkę zawierającą liczby od
# 1 do 10, a następnie wyświetli tylko liczby nieparzyste znajdujące się w tej krotce.

o=[]
np=[]
for i in range(10):
    m=random.randint(1,10)
    o.append(m)
for j in o:
    if j%2!=0:
        np.append(j)
krotka1=tuple(o)
krotka2=tuple(np)
print(krotka1)
print(krotka2)
# 5. Napisz funkcję najstarsza_osoba, która przyjmuje słownik,
# gdzie kluczami są imiona osób, a wartościami ich wiek. Funkcja powinna zwrócić imię najstarszej osoby.#
wiek={'edek':66,'staszek':34,'henryk':69,'mirosław':99}
def najstarsza_osoba(wiek):
    naj=max(wiek,key=wiek.get)
    return naj
print(najstarsza_osoba(wiek))

