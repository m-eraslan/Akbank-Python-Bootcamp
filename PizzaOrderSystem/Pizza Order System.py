import datetime
import csv
import time

print("Pizza Order System")

def menu():
    with open("menu.txt","r",encoding="utf=8") as file:
        print(file.read())

def sipariş_bilgileri():
    with open("Orders_Database.csv",mode="r") as yeni_dosya:
        print(yeni_dosya.read())


class Pizza():
    def __init__(self, cost, description):
        self.cost = cost
        self.description = description
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description
class klasik(Pizza):
    def __init__(self, cost, description):
        self.cost = cost
        self.description = description
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description
class margherita(Pizza):
    def __init__(self, cost, description):
        self.cost = cost
        self.description = description
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description
class turk_pizza(Pizza):
    def __init__(self, cost, description):
        self.cost = cost
        self.description = description
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description
class sade_pizza(Pizza):
    def __init__(self, cost, description):
        self.cost = cost
        self.description = description
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description

class Sos():
    def __init__(self, cost, description):
        self.cost = cost
        self.description = description
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description
class olive(Sos):
    def __init__(self, cost, description):
        self.cost = cost
        self.description = description
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description
class mushrooms(Sos):
    def __init__(self, cost, description):
        self.cost = cost
        self.description = description
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description
class goat_cheese(Sos):
    def __init__(self, cost, description):
        self.cost = cost
        self.description = description
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description
class meat(Sos):
    def __init__(self, cost, description):
        self.cost = cost
        self.description = description
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description
class onion(Sos):
    def __init__(self, cost, description):
        self.cost = cost
        self.description = description
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description
class corn(Sos):
    def __init__(self, cost, description):
        self.cost = cost
        self.description = description
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description

class Decarator():
    def __init__(self ,Pizza,Sos):
        self.Pizza=Pizza
        self.Sos=Sos
    def get_cost(self):
        return self.Sos.get_cost() + self.Pizza.get_cost()
    def get_description(self):
        return self.Sos.get_description() + ' ' + self.Pizza.get_description()

klasikpizza=klasik(30,"Klasik Pizza")
margheritapizza=margherita(40,"Margeritta Pizza")
turkpizza=turk_pizza(50,"Türk Pizza")
sadepizza=sade_pizza(20,"Sade Pizza")
zeytin=olive(5,"Zeytin")
mantar=mushrooms(8,"mantar")
keçipeyniri=goat_cheese(9,"Keçi Peyniri")
et=meat(15,"Et")
soğan=onion(7,"Soğan")
mısır=corn(6,"Mısır")


toplam = 0
urun=[]
soslar=[]
while True:
    print(""""
    pizza seçmek için 'p' basın 
    sos seçmek için 's' basın
    hesap için  'h' basın""")
    time.sleep(1)
    kod=input("Seçmek istediğiniz menünün kodunu giriniz:")
    if kod=="p":
        menu()
        time.sleep(1)
        pizza_kod =input("pizza kod:")
        if pizza_kod == "1":
            toplam+=int(klasikpizza.cost)
            urun.append(klasikpizza.get_description())
            print(klasikpizza.get_description(), klasikpizza.get_cost())
        elif pizza_kod == "2":
            toplam += int(margheritapizza.cost)
            urun.append(margheritapizza.get_description())
            print(margheritapizza.get_description(), margheritapizza.get_cost())
        elif pizza_kod == "3":
            toplam += int(turkpizza.cost)
            urun.append(turkpizza.get_description())
            print(turkpizza.get_description(), turkpizza.get_cost())
        elif pizza_kod == "4":
            toplam += int(sadepizza.cost)
            urun.append(sadepizza.get_description())
            print(sadepizza.get_description(), sadepizza.get_cost())
    elif kod=="s":
        while True:
            menu()
            time.sleep(1)
            print("Ana menuye dönmek için 'q' basın")
            sos_kod = input("Seçmek istediğiniz sos kodunu giriniz:")
            if sos_kod=="q":
                break
            if sos_kod == "11":
                toplam += int(zeytin.cost)
                soslar.append(zeytin.get_description())
                print(zeytin.get_description(), zeytin.get_cost())
            elif sos_kod == "12":
                toplam += int(mantar.cost)
                soslar.append(mantar.get_description())
                print(mantar.get_description(), mantar.get_cost())
            elif sos_kod == "13":
                toplam += int(keçipeyniri.cost)
                soslar.append(keçipeyniri.get_description())
                print(keçipeyniri.get_description(), keçipeyniri.get_cost())
            elif sos_kod == "14":
                toplam += int(et.cost)
                soslar.append(et.get_description())
                print(et.get_description(), et.get_cost())
            elif sos_kod == "15":
                toplam += int(soğan.cost)
                soslar.append(soğan.get_description())
                print(soğan.get_description(), soğan.get_cost())
            elif sos_kod == "16":
                toplam += int(mısır.cost)
                soslar.append(mısır.get_description())
                print(mısır.get_description(), mısır.get_cost())
    elif kod=="h":
        print(toplam,"TL hesap tutmaktadır.")
        ad_soyad=input("Adınız Soyadınız:")
        try:
            tc = int(input("TC kimlik numaranızı giriniz:"))
        except:
            print("11 haneli TC kimlik numaranızı giriniz.")
            tc = int(input("TC kimlik numaranızı giriniz:"))
        try:
            kart_no = int(input("Kredi kartı numaranızı giriniz:"))
        except:
            print("kart numaranızı giriniz.")
        try:
            kart_şifre = int(input("Kart şifresi:"))
        except:
            print("4 haneli  kart şifrenizi giriniz")
            kart_şifre=int(input("Kart şifresi:"))

        tarih=datetime.datetime.today()
        with open("Orders_Database.csv",mode="a",encoding="utf-8") as yeni_dosya:
            yeni_yazıcı = csv.writer(yeni_dosya, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            yeni_yazıcı.writerow(["İsim Soyisim","T.C.","Kart","Şifre","Pizza","Sos","Tarih"])
            yeni_yazıcı.writerow([ad_soyad,tc,kart_no,kart_şifre,urun[0],soslar,tarih])
        break
    else:
        print("Yanlış kod girdiniz tekrar deneyiniz.")
        continue
print(f"Adı Soyadı:{ad_soyad},TC:{tc},Kart:{kart_no},Şifre:{kart_şifre},Pizza Altı:{urun[0]},sos:{soslar},Tarih:{tarih}")