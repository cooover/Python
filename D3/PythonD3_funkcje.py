# -*- coding: utf-8 -*-
import random
import math
'''
def powitanie(imie):
    witaj = "Witaj "+ imie
    return witaj
    
a = powitanie("Ania")
b = powitanie("Ala")
c = powitanie("Ola")
print(a,b,c)

L = []
for i in range(1,4):
    L.append(powitanie(input("Podaj imię do listy: ")))
print(L)

def dodawanie(a,b, imie="Anonim", nazwisko="Anonim"):
    wynik = a + b
    print(a,b)
    print(imie, nazwisko)
    return wynik

res = dodawanie(14,24,nazwisko="Kow")
print(res)
#--------------------
def silnia(n):
    i=1
    res=1
    while(i<=n):
        res=res*i
        i+=1
    return res
#--------------------
print(silnia(5))
#--------------------
def silnia2(n):
    res = 1
    L = []
    i = 1
    while(i<=n):
        res=res*i
        L.append(res)
        i+=1
    return L
#--------------------
def wyswietl(lista):
    for i in lista:
        print(i,end=" ")
#--------------------       

wyswietl(silnia2(4))

#P70 [0,1,1,2,3,5,8,..]
def ciag_fib(n):
    F=[0,1]
    i=2
    suma=0
    while(i<n):
        a=F[i-1]+F[i-2]
        F.append(a)
        i+=1
    for i in F:
        suma+=i
    return F[len(F)-1], suma, F
print(ciag_fib(6))'''

#P71
def zdania(a = 5):
    wyrazy=["python","głupie","funkcje","chcę","iść","do","domu","to","zdanie","ma","wypisać","losowe","wyrazy","czy","działa"]
    i = 0
    Zdanie = []
    while (i<a):
        Zdanie.append(wyrazy[random.randint(0,len(wyrazy)-1)])   
        i += 1
    return Zdanie

def format(zdanie):
    for i,v in enumerate(zdanie):
        if(i == 0):
            print(v.capitalize(), end=" ")
        elif(i == len(zdanie)-1):
            print(v,end=" ")
        else:
            print(v, end=" ")
format(zdania(15))
print()
#P72
def odleglosc(x1,y1,x2,y2):
    return round(((x1-x2)**2 + (y1-y2)**2)**(1/2),2)
print((odleglosc(1,1,5,5)))

i= 0
x = []
y = []

while(i < 2):
    if (i ==1):
        print("Podaj położenie końcowe: ")
    else:
        print("Podaj położenie pczątkowe: ")
    u1 = int(input(""))
    u2 = int(input(""))
    x.append(u1)
    y.append(u2)
    i+=1
print("Dystans:",odleglosc(x[0],y[0],x[1],y[1]))