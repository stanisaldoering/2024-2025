
# napisz funckje ktora w petli prosi o podanie liczby naturalnej z sprawdzeniem tej liczby i zapisuje kazda podana liczbe  do odpowiedniej lity parzyste, nieparzyste. Natomiast jeśli funckaj napotka 0 to ma zakończyć cały program

# def suma_kw(liczba):
#     suma=0
#     while liczba>0:
#         cyfra=liczba%10
#         kwadrat_cyfry=cyfra**2
#         liczba=liczba//10
#     return  suma
# print(suma_kw(32))
#
#
# def wesola(liczba):
#     lista_liczb=[]
#     while liczba != 1 and liczba not in lista_liczb:
#         lista_liczb.append(liczba)
#         liczba=suma_kw(liczba)
#     return liczba
# print(wesola(34))
#
# licbza=10

def l():
    w=[]
    p=[]
    n=[]
    a=1
    while a<2:
        i=int(input('podaj liczbe'))
        if i%2==0:
            p.append(i)
        if i%2!=0:
            n.append(i)
        w.append(i)
        if i== 0:
            a=a+911
            print(w)
            print(p)
            print(n)
l()