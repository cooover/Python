# -*- coding: utf-8 -*-
import random
'''class PierwszaKlasa:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dodaj()
        self.odejmij()
    def dodaj(self):
        self.wynik_d = self.x + self.y
        return self.wynik_d
    def odejmij(self):    
        self.wynik_o = self.x - self.y
        return self.wynik_o
    def __str__(self):
        return "Wynik dodawania wynosi: "+str(self.wynik_d)+", a odejmowania: "+str(self.wynik_o)
    def __add__(self, other):
        return self.x + other.x, self.y + other.y
    def __ge__(self, other):
        return self.wynik_d >= other.wynik_d, self.wynik_o >= other.wynik_o
obiekt1 = PierwszaKlasa(5,6)
print(obiekt1)
obiekt2 = PierwszaKlasa(1,2)
# rzutowanie z __str__
print(obiekt2)
# rzutowanie z __add__
print(obiekt1+obiekt2)
# rzutowanie na operacje >=
print(obiekt1>=obiekt2)

#P75
class Zawodnik:
    def __init__(self, imie, nazwisko, waga, wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.waga = waga
        self.wzrost = wzrost
        self.obliczBMI()
    def obliczBMI(self):
        self.bmi = round(self.waga/((self.wzrost/100)**2))
    def __str__(self):
        return "BMI dla "+self.imie+" "+self.nazwisko+" wynosi: "+str(self.bmi)

z1 = Zawodnik("Anna","Nowak",60,170)
print(z1)
z2 = Zawodnik("Zofia", "Kowalska",80, 175)
print(z2)'''
#--------------------------------------------------
class Sklep:
    def __init__(self, towar, cena, ilosc):
        self.towar_klasa = towar
        self.cena_klasa = cena
        self.ilosc_klasa = ilosc
    def zaplata(self):
        self.do_zaplaty = self.cena_klasa*self.ilosc_klasa
#--------------------------------------------------
zakup1 = Sklep("chleb",3.99,4)
print(zakup1.towar_klasa)
print(zakup1.cena_klasa)
print(zakup1.ilosc_klasa)
zakup1.ilosc_klasa = 5
print(zakup1.ilosc_klasa)
zakup1.zaplata()
print(zakup1.do_zaplaty)

# P78
class Lotto:
    def __init__(self):
        print(random.sample(range(1,50),6))

los1 = Lotto()
los2 = Lotto()
los3 = Lotto()
los4 = Lotto()
'''class Lotto:
    def __init__(self):
        self.Tab = random.sample(range(1,50),6)
    def __del__(self):
        del self.Tab'''
