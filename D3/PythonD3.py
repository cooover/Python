# -*- coding: utf-8 -*-
import random
# wyświetla x do potęgi y
'''x = int(input("Podaj x: "))
y = int(input("Podaj y: "))
res =1
i = 1
while(i<=y):
    res = res*x
    i+=1
print(str(x)+" do potęgi "+str(y)+" równa się: "+str(res))'''

# oblicz sumę ciągu geometrycznego i i-ty wyraz (a1 +a1Q + a1g*g)...  n= a1q^(n-1)
'''
a1 = float(input("Podaj pierwszą liczbę: "))
q = float(input("Podaj q: "))
n = int(input("Podaj ilość elementów: "))
S = 0
i = 0
l = []
while(i<=(n-1)):
    S = S + a1 * q**i
    l.append(a1 * q**i)
    i+=1
print("%10s %15.2f"%("Suma:", S))
print("%10s "%("Składowe:"), end="")
#print("Ostatni element wynosi: "+str(a1 * q**(n-1)))
#print("Składowe ciągu: ",end="")
for i,v in enumerate(l):
    if(i==0):
        print("%15.2f"%(i), end=" ")
    else:
        print("%5.2f"%(v), end=" ")

'''
# P64
'''napis = input("Podaj napis: ")
szukana = input("Jakiej litery szukasz?: ")
i = 0
licz = 0
while(i <= (len(napis)-1)):
    if(napis[i] == szukana):
        print("Znaleziono "+napis[i]+" na "+str(i+1)+" pozycji.")
        licz+=1
    i+=1
print("Szukaną frazę znalezioniono: "+str(licz)+" razy.")'''

'''
napis = input("Podaj napis: ")
szukana = input("Jakiej litery szukasz?: ")
licznik = 0
i = 0
while(i<len(napis)):
    tab = napis[i:i+len(szukana)]
    if(tab==szukana):
        print("znaleziono na pozycji: "+str(i+1))
        licznik+=1
        i= i+ len(szukana)
    else:
        i=i+1
print(licznik)
'''
'''
i = int(input("Od ilu stopni zacząć?: "))
j = int(input("Do ilu?: "))
k = int(input("Co ile?: "))
print("%7s | %7s"%("C","F"))'''
'''if ((j-i)%k==0):
    C = range(i,j+k,k)
else:
    C = range(i,j,k)

z= len(C)-1'''
'''while (j-i<k):
    print("za duzy skok")
    k = int(input("Co ile?: "))
while(j >= i):
    print("%+7i | %+7.2f"%(j,j*1.8 +32))
    j-=k'''
    

'''while(z>=0):
    if (C[z]==0):
        print("------------------------")
        print("%7i | %7.2f"%(C[z], (C[z]*1.8)+32))
        print("------------------------")        
    else:
        print("%+7i | %+7.2f"%(C[z], (C[z]*1.8)+32))
    z-=1'''

#P68
Dop = ("3", "3.5","4","4.5","5","5.5")
O=[]
i='x'

print("Podaj oceny do wprowadzenia: ")
while (i !=""):
    i = input(" ")
    if(i in Dop):
        O.append(float(i))
    elif(i==""):
        print("Wpowadzanie ocen zakończone")
    else:
        print("zła ocena")
sr=0
if (len(O) !=0):
    for i in O:
        sr += i
    print("Średnia ocen to: ", round(sr/len(O),2))
else:
    print("Brak ocen")
print(O)