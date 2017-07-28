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
'''class Lotto:
    def __init__(self):
        self.Tab = random.sample(range(1,50),6)
    def __del__(self):
        del self.Tab'''
'''class Lotto:
    def __init__(self):
        self.Tab = random.sample(range(1,50),6)
        self.sortuj()

    def sortuj(self):
        self.Tab_s = sorted(self.Tab)
        self.__str__()
    def __str__(self):
        for i, v in enumerate(self.Tab_s):
            if(i==len(self.Tab_s)-1):
                print(v)
            else:
                print(v,end=",")'''

class Lotto:
    def __init__(self):
        self.L = range(1,50)
        self.Tab = random.sample(self.L,6)
        self.sortuj()
    def sortuj(self):
        self.Tab_s = sorted(self.Tab)
        self.__str__()
    def __str__(self):
        self.res=""
        for i, v in enumerate(self.Tab_s):
            if(i==len(self.Tab_s)-1):
                self.res+= str(v)
            else:
                self.res+= str(v)+", "
        return "Wynik losowania: "+ self.res

los1 = Lotto()
print(los1)
los2 = Lotto()
print(los2)



class Szkolenia:
    def __init__(self, nazwa, termin, cena_n, il_os):
        self.nazwa = nazwa
        self.termin = termin
        self.cena_n = cena_n
        self.il_os = il_os
    def obliczCalk(self):
        self.Suma_b = (self.il_os*self.cena_n)*1.23
        return self.Suma_b
    
class Technologie(Szkolenia):
    def __init__(self, nazwa, termin, cena_n, il_o, technologia, poziom):
        super().__init__(nazwa, termin, cena_n, il_o)
        self.technologia = technologia
        self.poziom = poziom

class Trenerzy(Technologie):
    def __init__(self, nazwa, termin, cena_n, il_o, technologia, poziom, imie, nazwisko, pensja):
        super().__init__(nazwa, termin, cena_n, il_o, technologia, poziom)
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja
    def obliczCalkTrener(self):
        return self.obliczCalk() - self.pensja*1.23

s1 = Technologie("Kurs Python dla dzieci", "2000-02-20", 2000, 20, "python", "podstawowy")    
print(s1.obliczCalk())
s2 = Trenerzy("Kurs Python dla dzieci", "2000-02-20", 2000, 20, "python", "podstawowy", "Adam", "Nowak", 1000) 
print(s2.obliczCalkTrener())

# P80

class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena
    def __str__(self):
        self.res = "Produkt o nazwie: "+self.nazwa+" ma cenę: "+str(self.cena)
        return self.res
class Oprogramowanie(Produkt):
    def __init__(self, nazwa, cena, jezyk, system):
        super().__init__(nazwa, cena)
        self.jezyk = jezyk
        self.system = system
    def __str__(self):
        
        self.res2 = super().__str__()+ ", jego język oprogramowania to: "+self.jezyk+" a system: "+self.system
        return self.res2
class Szkolenia(Oprogramowanie):
    def __init__(self, nazwa, cena, jezyk, system, termin):
        super().__init__(nazwa, cena, jezyk, system)
        self.termin = termin
    def __str__(self):
        
        self.res3 = super().__str__()+ ". Szkolenie odbędzie się: "+self.termin
        return self.res3
    
sk1 = Szkolenia("'Witaj Python'", 1000, "Python2.8", "MacOS", "2017-07-07")
print(sk1)
sk2 = Szkolenia("'Java dla zaawansowanych'", 2000, "Java", "Linux", "2017-09-01")
print(sk2)

# P80-(470)

class Kolory:
    def __init__(self,k1,k2,k3):
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
    def __str__(self):
        return "Utworzony kolor to RGB to: (" + str(self.k1)+", "+str(self.k2)+", "+str(self.k3)+")"      
    def __add__(self, other):
        return (self.k1 + other.k1)/2, (self.k2 + other.k2)/2, (self.k3 + other.k3)/2
kolor1 = Kolory(100,100,100)
print(kolor1)
kolor2 = Kolory(100,150,50)
print(kolor2)
kolor3 = kolor1+kolor2
print(kolor3)

#P80-(dodatkowe)

class Pracownik:
    def __init__(self, imie, nazwisko, etat="Staż", pensja=500):
        self.imie = imie
        self.nazwisko = nazwisko
        self.etat = etat
        self.pensja = pensja
    def pensjaBrutto(self):
        self.pensja_b = self.pensja * 1.23
        return self.pensja_b, self.pensja

class Kontrakt(Pracownik):
    def __init__(self, imie, nazwisko, etat="Staż", pensja=500):
        super().__init__(imie, nazwisko, etat, pensja)
    def zmianaKontraktu(self, etat, pensja):
        self.etat = etat
        self.pensja = pensja
    def nadgodziny(self, ilosc):
        self.ilosc = ilosc
        self_pensja = self.pensja + ((self.pensja/(20*8)) * self.ilosc)
    def __str__(self):
        return "Pensja pracownika: " + self.imie +" "+self.nazwisko+" z nadgodzinami: "+str(self.pensja*1.23)+"zł brutto."
    
p1 = Kontrakt("Adam", "Nowak")
print(p1.pensjaBrutto())
p1.zmianaKontraktu("Dev",5000)
print(p1.pensjaBrutto())
p1.nadgodziny(50)
print(p1.pensjaBrutto())
print(p1)