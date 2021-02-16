# Sorteaza o lista data fara .sort()

lista = [123,1243,3453,45776,2342,456456,32423,534634,4523,634,2356,345,3456,436,45645,6456,456,456,45,645,6345,34534,534545,7645767]
invers = True
while invers:
    invers = False
    for i in range(len(lista)-1): #ia toata lungimea listei, intrucat len() numara inapand de la 1
        if lista[i]>lista[i+1]: #verifica daca primul element din lista este mai mare decat urmatorul
            invers = True #devine adevarat, astfel incat va rula inca o data
            lista[i], lista[i+1]=lista[i+1], lista[i] #se face switch-ul intre primul element si al doilea
print(lista)
