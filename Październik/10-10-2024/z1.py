def pobieranie():
    temperatura={}
    with open ("temperatura.txt", 'r') as file:
        for line in file:
            temperatura.update({line[0:10]:int(line[11::].strip())})
    return temperatura
print(pobieranie())

# podaj maskymalna dlugosc okresu wzrastania temperatury w podanym czasie

for i in temperatura:
    if i[0]