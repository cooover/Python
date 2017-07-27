# -*- coding: utf-8 -*-
import random

def srednia(*arg):
    suma = 0
    sr = 0
    for v in arg:
        suma = suma + v
        print('suma',suma)
        sr = suma/len(arg)
        print('srednia',sr)
    return sr
        
print(srednia(2,3))
print(srednia())

# P74 - (002)
#---------------------------------------------
def wykresM(znak='*', ilosc=10):
    i=0
    Wartosci=[]
    while(i<ilosc):
        Wartosci.append(int(input("Podaj wartosc: ")))
        i+=1
    print(Wartosci)
    for v in Wartosci:
        print(znak*v)
#---------------------------------------------
#wykresM('%',3)
def wykresA(znak='*', ilosc=10):
    i=0
    Wartosci=[]
    while(i<ilosc):
        Wartosci.append(random.randint(0,9))
        i+=1
    print(Wartosci)
    for v in Wartosci:
        print(znak*v)

#wykresA('*',3)

def menu(znak='*', ilosc=10):
    a = input("Czy chcesz ręcznie wpisywać liczby? (t/n): ")
    if(a=='t'):
        wykresM(znak,ilosc)
    elif(a=='n'):
        wykresA(znak,ilosc)
    else:
        print("wpisales zły znak")



def wykres(d, znak = "*", ilosc = 10):
    i = 0
    Wartosci = []
    if (d == "M"):
        while(i < ilosc):
            Wartosci.append(int(input("Podaj kolenjną wartość: ")))
            i += 1       	 
    elif (d == "A"):
        while(i < ilosc):
            Wartosci.append(random.randint(0,9))
            i += 1	 
    for v in Wartosci:
        print(znak * v)

def menu2():
    znak_menu = input("podaj znak: ")
    ilosc_menu = input("podaj ilosc: ")  	 
    decyzja = input("Wybierz opcję: (A)-auto, (M)-manual")
    if (znak_menu == "" and ilosc_menu != ""):
        wykres(d=decyzja, ilosc = int(ilosc_menu))
    elif(znak_menu != "" and ilosc_menu == ""):
        wykres(d=decyzja, znak = znak_menu)
    elif (znak_menu != "" and ilosc_menu != ""):
        wykres(decyzja,znak_menu,int(ilosc_menu))
    else:
        wykres(d=decyzja)

def wykres3(d, znak = "*", ilosc = 10):
    i = 0
    Wartosci = []
    if (d == "M"):
        while(i < ilosc):
            var = int(input("Podaj kolejną wartość: "))
            while(var <0 or var>9):
                print("Podaj wartość z przedziału [0,9]: ")
                var = int(input("Podaj kolejną wartość: "))
            Wartosci.append(var)
            i += 1       	 
    elif (d == "A"):
        while(i < ilosc):
            Wartosci.append(random.randint(0,9))
            i += 1   
    for v in Wartosci:
        print(znak * v) 

def menu3():
    znak_menu = input("podaj znak: ")
    ilosc_menu = input("podaj ilosc: ")  	 
    decyzja = input("Wybierz opcję: (A)-auto, (M)-manual")
    while(decyzja !="A" and decyzja !="M"):
        print("Wpisałeś złą literkę ")
        decyzja = input("wpisz M lub A: ")         
    if (znak_menu == "" and ilosc_menu != ""):
        wykres3(d=decyzja, ilosc = int(ilosc_menu))
    elif(znak_menu != "" and ilosc_menu == ""):
        wykres3(d=decyzja, znak = znak_menu)
    elif (znak_menu != "" and ilosc_menu != ""):
        wykres3(decyzja,znak_menu,int(ilosc_menu))
    else:
        wykres3(d=decyzja)

#menu3()

# P74-(005)
def HTML_export(napis, color="black", size= "12px", weight="5"):
    return '<span style="color: '+ color +'; font-size: '+size+'; font-weight: '+weight+'">'+napis+'</span>'
print(HTML_export("Witaj w HTML", color="green", weight="3"))

# P74-(008)
kolor = "black"
ilosc = 0
ilosc_w = 0
ilosc_b = 0
def naprzemian():
    global kolor
    global ilosc, ilosc_w, ilosc_b
    ilosc+=1
    if(kolor=="white"):
        kolor = "black"
        ilosc_b+=1
    elif(kolor=="black"):
        kolor = "white"
        ilosc_w+=1
    return kolor
'''
print(naprzemian())
print(naprzemian())
print(naprzemian())
print(naprzemian())
print(naprzemian())
print("Funkcja naprzemian zostala wywołana:",ilosc, "razy. Kolor biały wypisano:",ilosc_w,"a czarny:",ilosc_b)
'''

# P74-(120)
def dodawanie(a,b):
    return a+b
def odejmowanie(a,b):
    return a-b
    
    
def menu4():
    z = input("Co chcesz zrobić? Dodać dwie liczby, odjąć czy wyjść z programu? (+/-/Q): ")
    while(z!="Q"):
        if(z=="+"):
            print(dodawanie(int(input("a=")),int(input("b=")))  )
            z= input("Co dalej? (+/-/Q): ")
        elif(z=="-"):
            print( odejmowanie(int(input("a=")),int(input("b="))) )  
            z =input("Co dalej (+/-/Q): ")
        else:
            print("Zły znak")
            z= input("Co dalej? (+/-/Q): ")
    print("Koniec")
            
#(menu4())

#P74-(240)
def tablica():
    Tab = []
    i = "t"
    print("Wprowadz elementy (enter) - koniec")
    while (i !=""):
        i = input(" ")
        if(i != ""):
            while True:
                try:
                    i = float(i)
                    break
                except ValueError:
                    print("Błąd! Podaj liczbę")
                    i = input(" ")
            Tab.append(i)
        elif(i==""):
            print("Wpowadzanie zakończone")
            return Tab


def wypisz5(limit, lista):
    print("filtruje elementy większe od", limit)
    suma= 0
    for v in lista:
        if(v>=limit):
            print(v,end=",")
            suma+=v
    print("Suma:", suma)

wypisz5(int(input("Podaj limit odcięcia: ")), tablica())
          
def sum(T):
    suma=0
    for v in T:
        if(v>=5):
            suma+=v
    return suma
#print(sum(tablica()))
