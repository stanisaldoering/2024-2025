# # wyszukaj inedksy genow spelniajce nasepujace kryteria:
# # gen musi byc dlzuszy niz 30 elementow oraz zawierac sekwencje AAABBB przynajemniej dwa razy
#
geny={}
with open('dane__geny.txt') as file:
    for index, line in enumerate(file):
        geny.update({index:line.strip()})


g=[]
klucz="AAABBB"
for i in geny.items():
    if len(i[1])>30:
        if i[1].count("AAABBB")>=2:
            g.append(i[0]) 
print(g)
