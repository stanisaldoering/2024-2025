# punkty=((1,2),(2,6),(8,9))
# def pole(punkty):
#     p1,p2,p3=punkty
#     return abs((p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1])-(p1[1]*p2[0]+p2[1]*p3[0]+p3[1]*p1[0]))/2
# print(pole(punkty))


# klucz: wartosc
dictNew={
    'imie':'Jan',
    'wiek': 20
}

dictnew2={
    'lista':[1,2,3,4,5,]
}

print(dictNew['imie'])
print(dictNew)

for i in dictNew:
    print(i)

for i in dictNew:
    print(i,':',dictNew[i])


towar={
    'mars':10,
    'orion': 13,
    'princepolo':5
}

print(towar)
towar['orion']=30
print(towar)

liczby={
    1:1000,
    2:33333,
    4:555555,
}
print(liczby[2])

# print(liczby[:-1])- takiej rzeczy nue mozemy robic

print(liczby.keys())
print(liczby.items())
print(liczby.get(1))
liczby.clear()
print(liczby)

