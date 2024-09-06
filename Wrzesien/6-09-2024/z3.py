owoce=['gruszka','ananas','banan','kiwi','granat']

def szuk(lista):
    return[i.count('a') for i in lista]
print(szuk(owoce))