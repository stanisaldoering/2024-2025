# sorted([1,2,3,4])
# [1,2,3,4].sort()
# reversed()
# sum()
# len()
# min()
# max()

# tuple
# tuple są literowane
zmienna=(1,2,3,'a','b','b')
print(zmienna)
lista=[1,2,3,'a','b','b']
a=tuple(lista)
print(a)

napis='PROGRAMOWANIE'
n=tuple(napis)
print(n)

liczba=[10000001]
l=tuple(liczba)
print(l)

# stwórz tuple z ocenami ucznia z informatyki
# a nastepnie uzyj metody count() do zliczenia wystąpień danej oceny
oceny=(1,1,1,1,2,2,2,5,5,5,4,4,4,)
print(oceny.count(5))


# przechowaj wspolrzedne w tupli w ktorej kazdy element to para wspolrzednych x i y. oblicz pole trojkąta
# pkt((1,2)(2,6),(8,9))