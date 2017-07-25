# -*- coding: utf-8 -*-
import random

literki = {'a' : 'A', 'b': 'B', 'c' : 'C', 'd' : 'D'}
print(literki)
print(len(literki))
print(literki['a'], literki['c'])
literki['c'] = "napis"
print(literki['c'])
print(literki.keys(), literki.values())
literki['e']='E'
del literki['c']
print(literki)
literki[2] = "abc"
print(literki)
to_str =str(literki)
print(to_str[0], to_str[1])

#P44 od jeden do piec
'''nazwa = {'jeden':1, 'dwa':2, 'trzy':3, 'cztery':4, 'pięć':5, 'piec':5}
key1 = input("Podaj liczbę: ")
print(key1.capitalize() +" w postaci dziesiętnej to: "+str(nazwa[key1]))

#P47
liczby = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V'}

print(key1.capitalize() +" w postaci dziesiętnej to: "+str(nazwa[key1])+", a w postaci rzymskiej to: "+liczby[nazwa[key1]])'''

#P48
'''nazwa = input("Jaki produkt chesz zamówić? (chleb, bułki, bagietka): ")
ilosc = int(input("Podaj ilosc zamównionego produktu: "))
nazwa_t = {'chleb': '0x1', 'bułki':'0x2', 'bagietka':'0x3'}
cena = {'0x1':1.99, '0x2':3.99, '0x3':5.99}
print("Do zapłaty: "+str(cena[nazwa_t[nazwa]]*ilosc)+ "zł ("+str(round((cena[nazwa_t[nazwa]]*ilosc)*1.23,2))+"zł brutto.)")'''

'''cena = {'chleb':1.99, 'bułki':3.99, 'bagietka':5.99}
print("Do zapłaty: "+str(cena[nazwa]*ilosc)+ "zł ("+str(round((cena[nazwa]*ilosc)*1.23,2))+"zł brutto.)")'''

# ZBIORY
ksztalty = set(['kolo','kwadrat', 'trojkat'])
ksztalty.add('okrąg')
ksztalty.discard('kolo')
print(ksztalty)
okragle = set(['okrąg'])
print(len(ksztalty), len(okragle))
print(ksztalty.issubset(okragle))
print(ksztalty.issuperset(okragle))
# operacje na zbiorach
print(ksztalty)
print(okragle)
print(ksztalty|okragle)
print(ksztalty&okragle)
print(ksztalty-okragle)
print(ksztalty^okragle)

# P49
S = set()
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
L = list(S)
print(L[:6])

# instrukcja warunkowa if

'''
a = int(input("Podaj liczbę: "))
if (a%2==0):
    print("Liczba "+str(a)+" jest parzysta.")
    if (a>=10):
        print("Liczba "+str(a)+" jest parzysta i większa równa od 10.")
    else:
        print("Liczba "+str(a)+" jest parzysta i mniejsza od 10.")
else:
    print("Liczba "+str(a)+" jest nieparzysta")
print("jestem już za instrukcją if")'''

'''a = int(input("Podaj liczbę: "))

if (a%2==0 and a>=10):
    print("Liczba "+str(a)+" jest parzysta i większa równa od 10.")
elif (a%2==0 and a<10):
    print("Liczba "+str(a)+" jest parzysta i mniejsza od 10.")
else:
    print("Liczba "+str(a)+" jest nieparzysta")'''

#P53
if (0):
    print(bool(0))
if (1):
    print(bool(1))
if (2):
    print(bool(2))
if (3):
    print(bool(3))
if (4):
    print(bool(4))

#P54
'''a = int(input("Podaj liczbę: "))
if (a <= 9 and a >= 0):
    print("Liczba "+str(a)+" znajduje się w przedziale od 0 do 9.")
else:
    print("out of range")'''
    
lista = [0,1,3,4,5,6,7,8,9]
'''index = int(input("Podaj indeks elementu, który chcesz wyświetlić: "))
if (index>=0 and index<=(len(lista)-1)):
    print("index is ok")
    print(lista[index])
else:
    print('out of range')'''
#P55
if (lista[0] > 0 and lista[1]>0):
    print("Oba elementy są większe od 0")
elif(lista[0] > 0 and lista[1]<=0):
    print("Pierwszy element jest większy od zera, a drugi mniejszy od 0")
elif(lista[0] <= 0 and lista[1]>0):
    print("Pierwszy element jest mniejszy od zera, a drugi większy od 0")
else:
    print("Oba elementy są mniejsze od 0")

# dwa zbiory i konstrukcją if sprawdzic czy są swoimi podzbiorami albo nadzbiorami

A = set([1,2,3,4,5])
B = set([2,3,5])
if(A==B):
    print("Zbiory są równe")
elif(A.issubset(B)):
    print("A jest podzbiorem B")
elif(A.issuperset(B)):
    print("A jest nazdbiorem B")
else:
    print("Zbiory są różne")

# pętle while
lista = [1,2,3,4,5,6,7,8,9]
i=0
while(i <= len(lista)-1):
    print("Indeks: "+str(i)+"\t Wartość: "+str(lista[i]))
    i += 1
print("poza pętlą")

i=len(lista)-1
while(i >=0 ):
    if (int(lista[i])%2==0):
        print("Indeks: "+str(i)+"\t Wartość: "+str(lista[i]))
    i-=1
else:
    print("jestem w else")
print("jestem poza pętlą")

# która z liczb jest większa i o ile? wyr trójargumentowe
a=14
b=10
print("a jest większe od b o: "+str(a-b)) if(a>=b) else print("a jest mniejsze od b o: "+str(b-a))