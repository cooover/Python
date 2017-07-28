# -*- coding: utf-8 -*-
import pymysql
class MySQLConnector:
    def __init__(self, passwd):
        self.passwd = passwd
        self.conn = pymysql.connect("localhost", "root", self.passwd, "skoczkowie")
        self.c = self.conn.cursor()
        print("Polączenie ustanowione")
        nav=""
        while(nav!="Q"):
            nav = input("Co chcesz zrobic?(S)- wyświetlić, (I)- wprowadzić zawodnika, (U)- zmienić dane, (D) - usunąć, (Q) - nic, wyjść z programu): ")
            if(nav== "S"):
                self.select()
            elif(nav=="I"):
                self.insert()
            elif(nav=="U"):
                self.update()
            elif(nav=="D"):
                self.delete()
        print("Polączenie zakończone")
        self.conn.close()
    def select(self):
        self.c.execute("SELECT id_skoczka, imie, nazwisko, kraj FROM zawodnicy order by id_skoczka;")
        res = self.c.fetchall()
        print("%-11s %-15s %-30s %-3s" % ("id_skoczka", "imie", "nazwisko", "kraj"))
        print("---------------------------------------------------------------")
        for v in res:
            id_skoczka = v[0]
            imie = v[1]
            nazwisko = v[2]
            kraj = v[3]
            print ("%-11s %-15s %-30s %-3s" % (id_skoczka, imie, nazwisko, kraj))
    def insert(self):
        self.c.execute("INSERT INTO zawodnicy VALUES (25, 'xxx', 'xxx', 'GER', '1981-02-24', 187, 68);")
        self.conn.commit()
        print("Dane wprowadzono")
    def update(self):
        self.c.execute("update zawodnicy set imie = 'Jan', nazwisko = 'Kowalski' where id_skoczka = 25;")
        self.conn.commit()
        print("Dane zmieniono")
    def delete(self):
        self.c.execute("delete from zawodnicy where id_skoczka=25;")
        self.conn.commit()
        print("Dane usunięto")        
c1 = MySQLConnector("kurs")