# -*- coding: utf-8 -*-
import random

'''literki = {'a' : 'A', 'b': 'B', 'c' : 'C', 'd' : 'D'}
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
print(to_str[0], to_str[1])'''

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
'''
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
'''
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
'''
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
    print(bool(4))'''

#P54
'''a = int(input("Podaj liczbę: "))
if (a <= 9 and a >= 0):
    print("Liczba "+str(a)+" znajduje się w przedziale od 0 do 9.")
else:
    print("out of range")'''
    
#lista = [0,1,3,4,5,6,7,8,9]
'''index = int(input("Podaj indeks elementu, który chcesz wyświetlić: "))
if (index>=0 and index<=(len(lista)-1)):
    print("index is ok")
    print(lista[index])
else:
    print('out of range')'''
'''#P55
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
'''
# pętle while
'''lista = [1,2,3,4,5,6,7,8,9]
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

for var in lista:
    print("Wartość: "+str(var))
    
lista.append(15)
for index, var in enumerate(lista):
    print("Index: "+str(index)+"\tWartość: "+str(var))
    
SL = {'a':1, 'b':2, 'c':3}
for k in SL:
    print(k, SL[k])
for k in SL:
    if(SL[k]>=2):
        print(k, SL[k])    

s1 = range(100)
print(s1)
for i in s1:
    print(i)
    
for j in range(15,25):
    print(j)
    
for k in range (0,100):
    print("Wynik: %-4i%-6i%-8i" % (k,k**2,k**3))
    
for x in range(5,100,10):
    print("Pierwiastkiem liczby %4i jest %6.3f" % (x,x**0.5))'''
# P57
'''zamowienie = input("wybierz towar: ")
sklep_prod = {"monitor16'":1, "klawiatura Logitech":2, "mysz Logitech":3}
for k in sklep_prod:
    if(zamowienie == k):
        print("Podukt dostępny: "+ k)
        break'''
    
# P58?
'''zamowienie = input("wybierz towar: ")
zamowienie_ilosc = int(input("Podaj ilość zamawianego produktu: "))
sklep_prod = {"monitor":1, "klawiatura":2, "mysz":3}
prod_cena = {1:1500, 2:400, 3:200}
prod_dostepnosc = {1:5, 2:5, 3:15}
if(zamowienie in sklep_prod.keys()):
        if (prod_dostepnosc[sklep_prod[zamowienie]] >= zamowienie_ilosc):
                print("Produkt dostępny: "+zamowienie)
                print("Zamawiasz: "+ str(zamowienie_ilosc)+" szt.")
        elif(prod_dostepnosc[sklep_prod[zamowienie]] < zamowienie_ilosc):
                print("Produkt dostępny: "+zamowienie)
                print("Jest dostępne tylko: "+ str(prod_dostepnosc[sklep_prod[zamowienie]])+" szt.")
else:
        print ('blad')'''
        
       
#print("Cena: "+ str(zamowienie_ilosc*prod_cena[sklep_prod[zamowienie]]))

'''sklep_prod = {"monitor":1, "klawiatura":2, "mysz":3}
prod_cena = {1:1500, 2:400, 3:200}
prod_dostepnosc = {1:5, 2:5, 3:15}
suma = 0
i = "t"
while(i == "t"):
    zamowienie = input("Wybierz towar: ")
    zamowienie_ilosc = int(input("Podaj ilość zamawianego produktu: "))
    if (zamowienie in sklep_prod.keys()):
        if (prod_dostepnosc[sklep_prod[zamowienie]] >= zamowienie_ilosc):
            print("Produkt dostępny: "+zamowienie)
            print("Zamawiasz: "+ str(zamowienie_ilosc)+" szt.")
            suma += zamowienie_ilosc*prod_cena[sklep_prod[zamowienie]]     
        elif(prod_dostepnosc[sklep_prod[k]] < zamowienie_ilosc):
            print("Produkt dostępny: "+zamowienie)
            print("Jest dostępne tylko: "+ str(prod_dostepnosc[sklep_prod[zamowienie]])+" szt.")
    else:
            print("Brak produktu, który chcesz zamówić")
    i= input("Czy chcesz zamawiać dalej? (t/n)")
print("Do zapłaty: "+str(suma))'''

# P60
'''ciag = []
to_dec = {"1":"jeden", "2":"dwa","3":"trzy", "4":"cztery", "5":"pięć", "6":"sześć", "7":"siedem", "8":"osiem", "9":"dziewięć"}
i = "t"
while(i == "t"):
    cyfra = input("Podaj cyfrę: ")
    if (cyfra.isdigit()): 
        ciag.append(to_dec[cyfra])            
    else:
        print("podana wartość nie jest cyfrą")   
    i = input("Czy chcesz wprowadzać dalej? (t/n)")
for k in ciag:
    print(k, end=" ")'''

#P61
line = [1,2,3,4,5]
n=1
print("  %3i%3i%3i%3i%3i"% (1,2,3,4,5))
print("==================")
while(n<=5):
    print(str(n)+"|",end="")
    print("%3i%3i%3i%3i%3i"%(n*line[0],n*line[1],n*line[2],n*line[3],n*line[4]))
    n+=1

#P63
liczby = range(1,10,2)
n = len(liczby)-1
while (n>=0):
    if(n==0):
        print(liczby[n]**2)
    else:
        print(liczby[n]**2,end=",")
    n-=1