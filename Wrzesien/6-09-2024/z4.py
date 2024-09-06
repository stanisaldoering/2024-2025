lista=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


# def wiersze(list):
#     wiersz=[]
#     for i in lista:
#         wiersz.append(sum(i))
#     return wiersz
# print(wiersze(lista))

def kolumn(list):
    kolumny=[]
    for i in range(len(lista)):
        suma=0
        for j in range(len(lista[i])):
            suma+=lista[j][i]
        kolumny.append(suma)
    return kolumny
