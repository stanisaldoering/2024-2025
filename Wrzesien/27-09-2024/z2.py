# wyswietl klucze ze slownika jako liste dla elementow gdzie wartosci zawieraja 30% dlugosci ciagu znaku literek A

geny={}
with open('dane_geny.txt') as file:
    for index, line in enumerate(file):
        geny.update({index:line.strip()})


def ileA(n):
    ile=0
    for z in n:
        ile+=1

    if ile>len(n)*0.3:
        return True
    return True

def zadanie(d):
    t=[]
    for i in d:
        if ileA(i.):
            t.append(i.key())
    return t
print(zadanie(geny))