# -*- coding: utf-8 -*-

napis = "zawartosc"
print(napis.capitalize())
print(napis.count("aw"))
print(napis.islower())
print(napis.index("a"))
print(napis.replace("a","A"))

Tab = []
Tab.append(1)
Tab.append("abc")
Tab.append("A")

'''print(Tab[0],Tab[1],Tab[2])
# deklaracja i przypisanie wartości
oceny = []
a = input("Podaj ocenę: ")
oceny.append(a)
oceny.append(input("Podaj drugą ocenę: "))
print(oceny[0], oceny[1])
oceny[0] = '5'
print(oceny[0], oceny[1])'''

oceny2 = [3,4,5,6,7,8,9,10]
print(oceny2[1])

ListList = [ [1, 2, 3], ["Nocny", "Dzienny"] ]
print(ListList[1][1])
ListList = [ [1, 2, 3,["a","b","c"]], ["Nocny", "Dzienny"] ]
print(ListList[0][3][1])
print(oceny2[3:5])
print(oceny2[3::2])
print(oceny2[3:])
print(len(oceny2))

text = "napis"
lista = list(text)
print(lista)
lista[2] = "w"
print(lista)
print(lista.pop(2))
print(lista[2], len(lista))

# P41
art = []
art.append("chleb")
art.append("woda")
art.append("masło")
ceny =[]
ceny.append(1.15)
ceny.append(2.45)
ceny.append(2.05)
print(art, ceny)
print(art[0]+"\t\t"+str(ceny[0]))
print(art[1]+"\t\t"+str(ceny[1]))
print(art[2]+"\t\t"+str(ceny[2]))
# 2 sposób
arty = [['mleko',"chleb", "cukierki"], [1.99,3.15,13.55]]
print(arty)
print("nazwa\t\tcena")
print(arty[0][0]+"\t\t"+str(arty[1][0]))
print(arty[0][1]+"\t\t"+str(arty[1][1]))
print(arty[0][2]+"\t"+str(arty[1][2]))

krotka = ("a",2,13.5)
krotka2 = "a","b","c"
print(krotka)
print(krotka2)

data = ('01','01', '2018')
print("Data ważności atykułu:",data[0]+"-"+data[1]+"-"+data[2])

data2 = (("Mleko","Chleb","Cukierki"), ("01-01-2019", "01-01-2020", "01-01-2018"))
print(data2[0][0]+"\t\t"+data2[1][0])
print(data2[0][1]+"\t\t"+data2[1][1])
print(data2[0][2]+"\t"+data2[1][2])

tabelka = [("Kowal", ("Nowak", "-Cos")),("15-06-1981", "01-10-1968"), ["dev", "dev"]]
tabelka[2][0] = "admin"
# tabelka[0][0] = "Kowalski" - wyskoczy błąd bo nie można zmienić krotki
print(tabelka[0][0], tabelka[1][0], tabelka[2][0])
print(tabelka[0][1][0], tabelka[1][1], tabelka[2][1])
print(tabelka[0][1][0]+tabelka[0][1][1], tabelka[1][0], tabelka[2][1])