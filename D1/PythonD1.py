# -*- coding: utf-8 -*-

# komentarz jednowierszowy
zmienna1 = 5
zmienna2 = 5.3
'''
poczatek komentarza blokowego
text = "to jest moj tekst"
text2 = 'to jest inny tekst'
literki = "A"
literki = 'a'
koniec komentarza blokowego
'''
'''witaj = "I'm Hanna"
zmienna3 = 2 + 5
Zmienna3 = 'liczba'
nowa_zmienna = zmienna3 + 5
print(zmienna1)
print(zmienna1,zmienna2)
print(witaj)
print(zmienna3,Zmienna3)
print(nowa_zmienna)
print("Hi, "+witaj)
print("HI, "+witaj+". How are you?")
print("Przed zmiana:", Zmienna3)
Zmienna3 = 3.14
print("Po zmianie", Zmienna3)
del (zmienna1)
#print(zmienna1)'''

#P1
'''a = 1
b = 2.4
c = "w1"
print(a,b,c)'''

#P2
'''a = 2.1
b = "abc"
c = 0
print(a,b,c)'''

#P5
'''
imie = input("Podaj imie: ")
nazwisko = input("Podaj nazwisko: ")
data = input("Podaj datę urodzenia: ")
stanowisko = input("Podaj stanowisko: ")
placa = input("Podaj płacę: ")
print("Twoje dane to: ",imie, nazwisko, data, stanowisko, placa)'''

#P6
'''pi = 3.14
# int() - rzutuje na integer
# input() - czyta wartość z klawiatury - string!
promien = int(input("Podaj liczbę "))
pole_kola = pi*promien*promien
# podstawa **wykladnik  (wtedy tez zaokragla do 2 miejsca po przecinku)
print(pole_kola, pi*promien**2)
# type() - zwraca typ wartości zmiennej
print(type(pole_kola))
print(type(21j))'''
'''dluga = 3147483647
print(type(dluga))
#dluga2 = 32L
#print(type(dluga2))
print(3/2, 3//2)
print(round(3.14159, 2))
print(round(1.2), round(1.5), round(1.8))
print(round(-1.2), round(-1.5), round(-1.8))
print(int(1.2), int(1.5), int(1.8))
print(int(1.2+0.5), int(1.5+0.5), int(1.8+0.5))
print(int(-1.2+0.5), int(-1.5+0.5), int(-1.8+0.5))'''

#P10 tylko z netto podać brutto
'''kwota_netto = float(input("Podaj kwotę netto: "))
vat = int(input("Podaj stawkę vat (3%, 7%, 23%): "))
kwota_brutto = kwota_netto + (kwota_netto*(vat/100))
print("Twoja kwota brutto przy stawce " +str(vat) +" vat wynosi: "+ str(kwota_brutto)+" zł.")'''

#P11
'''nazwa_p1 = "chleb"
nazwa_p2 = "mleko"
nazwa_p3 = "cukierki"

cena_p1 = 1.99
cena_p2 = 4.5
cena_p3 = 15.99

zamowienie_p1 = int(input("Liczba chlebow: "))
zamowienie_p2 = float(input("Litry mleka: "))
zamowienie_p3 = float(input("Waga cukierków(g): "))
suma = (cena_p1 * zamowienie_p1) + (cena_p2 * zamowienie_p2) + ((cena_p3/1000 ) * (zamowienie_p3))

print("Twoje zamówienie")
print("================")
print("Liczba chlebow: ", zamowienie_p1, "szt.")
print("Ilość mleka: ", zamowienie_p2, "l")
print("Waga cukierków: ", zamowienie_p3, "g.")
print("================")
print("Do zapłaty:")
print("================")
print(round(suma,2), " zł.")'''

#print((1+1j)+(13+21j))

#P13
'''a = 12
b = 1+(-1j)
print (a*b)

log1 = True
print(type(log1))

print (bool(""), bool(0), bool("Ala"))

a = """
autor:
data:
wersja:
"""
print(a)
# /n - znak przejścia do nowej linii
b= "autor:\ndata:\nwersja:\n"
print(b)

txt = "napis"
print(txt*3)

imie = input("Podaj imię: ")
#imie_1 = imie +", "
imie_2 = imie + "."
n = int(input("Ile razy wypisać imię?: "))
wypisz = (imie +", ") * (n-1) + imie_2
print(wypisz)'''

#P22
'''imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
wiek = input("Podaj wiek: ")
pensja = input("Podaj pensja: ")
stanowisko = input("Podaj stanowisko: ")
napis = "Pan/i "+imie+" "+nazwisko+" (wiek: "+wiek+" lat)"+" pracuje na stanowisku: "+stanowisko+" (pensja: "+pensja+" brutto).\n"
print(napis*10)'''
'''a = 1
print(type(str(a)))

x = 1
a = 5.5
b = 6.5
print(type(a+b+x))'''

#P25
'''print("Kwota netto/h", round(kwota_netto_h,2),"zł.")
print("Kwota brutto/h", round(kwota_netto_h*1.23,2),"zł.")'''

#P26
'''p = False
q = True
dM1 = not (p and q) 
dM2 = (not p) or (not q)
print(dM1,dM2)
print(dM1 == dM2)'''

#P27
'''a = False
b = False
c = True

p1 = not a and not b and not c
p2 = not a and not b and c
p3 = not a and b and not c
p4 =  a and not b and not c

print(p1 or p2 or p3 or p4)

print('ala' < 'alan')'''

# P28
liczba = round((17**(1/2)),2)
uroj = 1j
res = str(liczba * uroj)
print("Liczba zespolona: 0+"+res)

# P29
z = 17 % 7
print(z**2 +z*3)

# P30
print((str(1.2e+3+34.5)+";")*20)

# P32
'''a = input("Wpisz pierwszy napis: ")
b = input("Wpisz drugi napis: ")
print("Napis 1 jest większy leksykograficznie", a > b)
print("Napisy są takie same", a == b)
print("Napis 2 jest większy leksykograficznie", a < b)'''

print("imie\t"+"nazwisko\t"+"stanowisko")

# P38
SPK = int(input("Podaj stan początkowy konta: "))
P = float(input("Podaj stopę oprocentowania: "))
N = int(input("Podaj liczbę lat: "))
res = round(SPK*(1+P/100)**N,2)
print("Kwota po "+str(N) +" latach wynosi: "+str(res)+"zł.")