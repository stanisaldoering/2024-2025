# napisz funkcje zwracajaca 5 wyolosowychn liczb w liscie
# from random import randint
# def los(n):
#     lista=[]
#     for i in range(n):
#         lista.append(randint(0,100))
#     return lista
# print(los(5))

#
owoce=['gruszka','ananas','banan','kiwi','granat']
# def liczby(lista):
#     return [len(i) for i in owoce]
# print(liczby(owoce))

def szuk(lista):
    return[i.count('a') for i in lista]
print(szuk(owoce))