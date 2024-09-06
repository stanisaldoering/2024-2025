from random import randint
def los(n):
    lista=[]
    for i in range(n):
        lista.append(randint(0,100))
    return lista
print(los(5))