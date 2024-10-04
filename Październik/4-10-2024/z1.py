# utworz słownik prdokutów w magazynie, produkty maja byc zapisane w nastepujacy sposob
# zdefiniuj funkcje obliaczajacą wartosc naszego magazynu
# wyswietralajce stan magazynu(powinno wyswietlac produkt, ilosc i cene
# dodawanie nowego produktu do magazynu
# aktualizacja ilosci istenijących produktów
produkty={
    'ser':{'ilość':10,'cena':2},
    'kiełbasa':{'ilość':3,'cena':15},
    'chleb':{'ilość':30,'cena':5},
    'bułki':{'ilość':100,'cena':2},
    'szynka':{'ilość':20,'cena':20},
    'kukurydza':{'ilość':90,'cena':13},
    'ogórek':{'ilość':15,'cena':30},
    'pomidor':{'ilość':200,'cena':5},
    'sok':{'ilość':40,'cena':7},
    'truskawka':{'ilość':1000,'cena':50}
}
def wartosc(produkty):
    wmg = 0
    for produkt, i in produkty.items():
        wmg += i['ilość']*i['cena']
    return wmg

w=wartosc(produkty)
print("wartosc produktów w magzynie to ",w)

def stan(produkty):
    print("Stan magazynu:")
    for j, i in produkty.items():
        print (j,i)
print(stan(produkty))

def dodaj(produkty,produkt,ilosc,cena):
    if produkt in produkty:
        return f'produkt istnieje w magazynie'
    produkty[produkt]={'ilość':ilosc,'cena':cena}
    return f"Produkt:{produkt} dodano do magazuny"

def zmien(produkty,produkt,ilosc):
    if produkt in produkty:
        produkty[produkt]['ilość']=ilosc
        return f"Zmieniono dane produktu:{produkt}"
    return f"{produkt} nie znajuuje sie sie"



# def menu