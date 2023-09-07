import tkinter
from tkinter import ttk
import numpy as np
import random
from DataBase import *

random.seed(2)

def generateEntry(main,width, x, y):
    text = tkinter.Entry(main, width=width, font=("cambira 12 bold"))
    text.pack()
    text.place(x = x, y = y)
    return text

def generateSpin(main, from_, to, width, values, font, x,y):
    spin =  ttk.Spinbox(main, from_=from_,  to=to, width=width, values= values,  font = font)
    spin.pack()
    spin.set(3)
    spin.place(x = x, y = y)

    return spin

def generateLabel(main, text, bg, font, x, y):
    label = ttk.Label(main, text = text, background=bg, font = font)
    label.pack()
    label.place(x = x, y = y)
    return label

def generateCombobox(main, width, font, x, y):
    players_list = ttk.Combobox(main, width=width, font = font)
    players_list.pack()
    players_list.place(x = x, y = y)

    return players_list

def generateButton(main, text, bg, fg, width, font, x, y):
    girisbutonu = tkinter.Button(main, text=text, bg=bg,fg=fg, width=width, font = font)                                  
    girisbutonu.pack()
    girisbutonu.place(x = x, y = y)

    return girisbutonu

NameList = ["Ahmet", "Mehmet", "Zeynep", "Ayşe", "Sevil", "Betül", "Rıza", "Emir", "Safiye", "Berk", "Ada", "Recep"]
SurnameList = ["Yenidağ", "Erdoğan", "Öztürk", "İnce", "Yener", "Uysal","Güçlü","Niğdelioğlu", "Solmaz", "Yenigün", "Emikönel", "Korkmaz"]
regions = []
players = []


class Players():

    def __init__(self, id, role, name, surname, password, money, eatings, goods):
        self.id = id
        self.role = role
        self.name = name
        self.surname = surname
        self.username = name[0:4] + surname[0:4] + str(id)
        self.password = password
        self.workplace = 0

        self.money = money
        self.eatings = eatings
        self.goods = goods

    def getInfo(self):

        information =  str(self.id) +"\n"  +  self.name + " " + self.surname + "\n"+ self.username + "\n"+ str(self.password) + \
            "\n"+"{} nolu {}".format(str(self.workplace.id), self.workplace.type) + "\n" + str(self.money) \
             + "\n" + str(self.eatings) + "\n" + str(self.goods)
        
        return information

administer = Players(0, "Yönetici", "Rıdvan", "İNCE", 1453, 100000, 100000, 100000)
nullPlayer = Players(-1, "Oyuncu", "Null", "Null", 0000, 10000, 10000, 10000)


class Land():

    def __init__(self, id, type, owner):
        self.id = id
        self.type = type
        self.owner = owner
        self.value = random.randint(500, 1000)
        self.rented = False
        self.renter = nullPlayer

    def getInfo(self):
        information = str(self.id)+"\n" + self.type + "\n" + self.owner.name + " " + self.owner.surname + "\n" + str(self.value)
        return information

class Business():

    def __init__(self, id, type, owner, capacity, worker_number, grade):
        self.id = id
        self.type = type
        self.owner = owner
        self.capacity = capacity
        self.worker_number = worker_number
        self.grade = grade
        self.value = random.randint(1000, 1500)
        self.rent = round(self.value/50,2)
        self.fixIncome = round(self.rent*9,2)
        self.rented = False
        self.renter = nullPlayer

nullregion = Business(-1, "Mağaza", nullPlayer, 1, 1, 1)

class ShoppingCenter(Business):

    def __init__(self, id, type, owner, capacity, worker_number, grade): 
        super().__init__(id, type, owner, capacity, worker_number, grade)
        self.good_fee = round(self.value/500,2)
        self.wage = round(self.good_fee*10,2)

    def getInfo(self):

        information = str(self.id) + "\n" + self.type + "\n" + self.owner.name + " " + self.owner.surname + "\n" + \
            str(self.capacity) + "\n" + str(self.worker_number) + "\n" + str(self.grade) + "\n" + str(self.value) + "\n" + \
                str(self.rent) + "\n" + str(self.fixIncome) +"\n" + str(self.rented) +  "\n" + self.renter.name + " " +self.renter.surname + \
        "\n" + str(self.good_fee) + "\n" + str(self.wage)

        return information
    
nullregion = ShoppingCenter(-1, "Mağaza", nullPlayer, 1, 1, 1)

class Market(Business):

    def __init__(self, id, type, owner, capacity, worker_number, grade): 
        super().__init__(id, type, owner, capacity, worker_number, grade)
        self.food_fee = round(self.value/400,2)
        self.wage = round(self.food_fee*10,2)


    def getInfo(self):

        information = str(self.id) + "\n" + self.type + "\n" + self.owner.name + " " + self.owner.surname + "\n" + \
            str(self.capacity) + "\n" + str(self.worker_number) + "\n" + str(self.grade) + "\n" + str(self.value) + "\n" + \
                str(self.rent) + "\n" + str(self.fixIncome) + "\n" + str(self.rented) +  "\n" + self.renter.name + " " +self.renter.surname + "\n" + \
        str(self.food_fee) + "\n" + str(self.wage)
        

        return information

class RealEstate(Business):
   
    def __init__(self, id, type, owner, capacity, worker_number, grade): 
        super().__init__(id, type, owner, capacity, worker_number, grade)
        self.rent_commission = round(self.rent,2)
        self.sold_commission = round(self.rent*2,2)
        self.wage = round(self.rent,2)

    def getInfo(self):

        information = str(self.id) + "\n" + self.type + "\n" + self.owner.name + " " + self.owner.surname + "\n" + \
            str(self.capacity) + "\n" + str(self.worker_number) + "\n" + str(self.grade) + "\n" + str(self.value) + "\n" + \
                str(self.rent) + "\n" + str(self.fixIncome) + "\n" + str(self.rented) +  "\n" + self.renter.name + " " +self.renter.surname + \
                    "\n" + str(self.rent_commission) + "\n" + str(self.sold_commission) + "\n" + str(self.wage)

        return information

def YoneticiBilgiGuncelle(Yonetici, OyunAlanlari, yoneticiParaMiktari, yoneticiEsyaMiktari,
                           yoneticiYemekMiktari, yoneticiAlanlarSahib, yoneticiAlanlarKira):

    yoneticiParaMiktari.delete(0, tkinter.END)
    yoneticiEsyaMiktari.delete(0, tkinter.END) 
    yoneticiYemekMiktari.delete(0, tkinter.END) 

    yoneticiParaMiktari.insert(0, str(Yonetici.money))
    yoneticiEsyaMiktari.insert(0, str(Yonetici.goods)) 
    yoneticiYemekMiktari.insert(0, str(Yonetici.eatings)) 

    options1 = [str(x.id) + " - " + x.type for x in OyunAlanlari if x.owner.id == Yonetici.id]
    options2 = [str(x.id) + " - " + x.type for x in OyunAlanlari if x.owner.id == Yonetici.id and x.rented == True]

    yoneticiAlanlarSahib["values"] = options1
    yoneticiAlanlarKira["value"]  = options2

    yoneticiAlanlarSahib.set(options1[0])
    if len(options2) > 0:
        yoneticiAlanlarKira.set(options2[0])
    else:
        yoneticiAlanlarKira.set("-")

def generateRegions(satir,sutun):
    if len(regions) > 0:
        regions.clear()

    index = 0
    for index in range(1,satir*sutun-2):
        a = Land(index,"ARSA", administer)
        regions.append(a)
    
    yonetici_magaza1 = ShoppingCenter(index+1,"MAĞAZA", administer, 1000, 0,1)
    yonetici_market1 = Market(index+2,"MARKET", administer, 1000, 0,1)
    yonetici_emlak1  = RealEstate(index+3,"EMLAK", administer, 1000, 0,1)
    # yonetici_magaza2 = ShoppingCenter(index+4,"MAĞAZA", administer, np.inf,0,1)
    # yonetici_market2 = Market(index+5,"MARKET", administer, np.inf, 0,1)
    # yonetici_emlak2  = RealEstate(index+6,"EMLAK", administer, np.inf, 0,1)

    regions.append(yonetici_magaza1)
    regions.append(yonetici_market1)
    regions.append(yonetici_emlak1)
    # regions.append(yonetici_magaza2)
    # regions.append(yonetici_market2)
    # regions.append(yonetici_emlak2)

def generatePlayers(NumberofPlayers, text1, text2, text3):
    if len(players) > 0:
        players.clear()
    players.append(nullPlayer)
    players.append(administer)

    for i in range(1,NumberofPlayers+1):
        p = Players(i, "Oyuncu", random.choice(NameList), random.choice(SurnameList), random.randint(10000, 99999), int(text1.get()), int(text2.get()), int(text3.get()))
        players.append(p)

def assignPersontoWrokplace():

    nullPlayer.workplace = nullregion
    administer.workplace = nullregion

    for i in players[2:]:
        workplaceforperson = random.choice([x for x in regions if x.type != "ARSA"])
        i.workplace = workplaceforperson
        workplaceforperson.worker_number +=1

def CalisanListesiOlustur(oyuncu_listesi, region):
   
    calisanListesi = []
    if len(calisanListesi) > 0:
        calisanListesi.clear()
    
    calisanListesi = [x.name +  " " + x.surname for x in oyuncu_listesi[2:] if x.workplace.id == region.id]
    calisanlar = ""

    if len(calisanListesi) > 0:
        indeks = 1
        for p in calisanListesi:
            calisan = "{} - {}\n".format(indeks, p)
            calisanlar = calisanlar + calisan
            indeks+=1
    else:
        calisanlar = calisanlar + "---"
    calisanlar = calisanlar[0:-2]

    return calisanlar

def PlayerDetailedScreen(OyuncuListesi):

    root = tkinter.Tk()
    root.title("Oyuncu Detay")
    root.geometry("350x400")
    root.config(bg="grey")

    value = OyuncuListesi.get()
    id = value[0:value.index(" ")]
    player = players[int(id) + 1]
    

    generateLabel(root, "Oyuncu id: ", "grey", ("cambria 12 bold" ), 10, 10)
    generateLabel(root, "Ad/Soyad: ", "grey", ("cambria 12 bold" ), 10, 35)
    generateLabel(root, "Kullanıcı Adı: ", "grey", ("cambria 12 bold" ), 10, 60)
    generateLabel(root, "Şifre: ", "grey", ("cambria 12 bold" ), 10, 85)
    generateLabel(root, "Çalışma Yeri: ", "grey", ("cambria 12 bold" ), 10, 110)
    generateLabel(root, "Para Miktarı: ", "grey", ("cambria 12 bold" ), 10, 135)
    generateLabel(root, "Yemek Miktarı: ", "grey", ("cambria 12 bold" ), 10, 160)
    generateLabel(root, "Eşya Miktarı: ", "grey", ("cambria 12 bold" ), 10, 185)


    oyuncuId = generateEntry(root, 5, 130,10); oyuncuId.delete(0, tkinter.END); oyuncuId.insert(0, str(player.id))
    oyuncuAdi = generateEntry(root, 20, 130,35); oyuncuAdi.delete(0, tkinter.END); oyuncuAdi.insert(0, player.name + " " + player.surname)
    kullanici = generateEntry(root, 20, 130,60); kullanici.delete(0, tkinter.END); kullanici.insert(0, player.username)
    sifre = generateEntry(root, 20, 130,85); sifre.delete(0, tkinter.END); sifre.insert(0, str(player.password))
    isyeri = generateEntry(root, 20, 130,110); isyeri.delete(0, tkinter.END); isyeri.insert(0, str(player.workplace.id) + " nolu " + player.workplace.type)
    ParaMiktari = generateEntry(root, 7, 130,135); ParaMiktari.delete(0, tkinter.END); ParaMiktari.insert(0, str(player.money))
    YemekMiktari = generateEntry(root, 7, 130,160); YemekMiktari.delete(0, tkinter.END); YemekMiktari.insert(0, str(player.eatings))
    EsyaMiktari = generateEntry(root, 7, 130,185); EsyaMiktari.delete(0, tkinter.END); EsyaMiktari.insert(0, str(player.goods))
    
    OyuncuListesi.set("Oyuncu Seçiniz")
    root.mainloop()

def LandDetailedScreen(id, type,owner, value):

    root = tkinter.Tk()
    root.title("Arsa Detay")
    root.geometry("350x400")
    root.config(bg="grey")

    generateLabel(root, "Alan id", "grey", ("cambria 12 bold" ), 10, 10)
    generateLabel(root, "Alan Tipi", "grey", ("cambria 12 bold" ), 10, 35)
    generateLabel(root, "Alan Sahibi", "grey", ("cambria 12 bold" ), 10, 60)
    generateLabel(root, "Satış Değeri", "grey", ("cambria 12 bold" ), 10, 85)
       
    Alan_id = generateEntry(root, 5, 130,10)
    Alan_id.delete(0, tkinter.END)
    Alan_id.insert(0, id)

    AlanTip = generateEntry(root, 15, 130,35)
    AlanTip.delete(0, tkinter.END)
    AlanTip.insert(0, type)

    AlanSahibi = generateEntry(root, 20, 130,60)
    AlanSahibi.delete(0, tkinter.END)
    AlanSahibi.insert(0, owner)

    AlanDegeri = generateEntry(root, 5, 130,85)
    AlanDegeri.delete(0, tkinter.END)
    AlanDegeri.insert(0, value)

        
    root.mainloop()

def ShoppingDetailedScreen(id, type,owner, capacity,worker_number, grade,value, rent, fixIncome, rented, renter, goodfee, shopping_wage, workers):

    root = tkinter.Tk()
    root.title("Arsa Detay")
    root.geometry("350x500")
    root.config(bg="grey")

    generateLabel(root, "Alan id", "grey", ("cambria 12 bold" ), 10, 10)
    generateLabel(root, "Alan Tipi", "grey", ("cambria 12 bold" ), 10, 35)
    generateLabel(root, "Alan Sahibi", "grey", ("cambria 12 bold" ), 10, 60)
    generateLabel(root, "Kapasite", "grey", ("cambria 12 bold" ), 10, 85)
    generateLabel(root, "Calışan Sayısı", "grey", ("cambria 12 bold" ), 10, 110)
    generateLabel(root, "Seviye", "grey", ("cambria 12 bold" ), 10, 135)
    generateLabel(root, "Satış Bedeli", "grey", ("cambria 12 bold" ), 10, 160)
    generateLabel(root, "Kira Bedeli", "grey", ("cambria 12 bold" ), 10, 185)
    generateLabel(root, "Sabit Gelir", "grey", ("cambria 12 bold" ), 10, 210)
    generateLabel(root, "Eşya Fiyatı", "grey", ("cambria 12 bold" ), 10, 235)
    generateLabel(root, "Kirada mı", "grey", ("cambria 12 bold" ), 10, 260)
    generateLabel(root, "Kiracı", "grey", ("cambria 12 bold" ), 10, 285)
    generateLabel(root, "Ücret Düzeyi", "grey", ("cambria 12 bold" ), 10, 310)
    generateLabel(root, "Calışanlar", "grey", ("cambria 12 bold" ), 10, 335)

    shopping_id = generateEntry(root, 15, 130,10); shopping_id.delete(0, tkinter.END); shopping_id.insert(0, id)
    shopping_type = generateEntry(root, 15, 130,35); shopping_type.delete(0, tkinter.END); shopping_type.insert(0, type)
    shopping_owner = generateEntry(root,15, 130,60); shopping_owner.delete(0, tkinter.END); shopping_owner.insert(0, owner)
    shopping_capacity = generateEntry(root, 15, 130,85); shopping_capacity.delete(0, tkinter.END); shopping_capacity.insert(0, capacity)
    shopping_worker_number = generateEntry(root, 5, 130,110); shopping_worker_number.delete(0, tkinter.END); shopping_worker_number.insert(0, worker_number)
    shopping_grade = generateEntry(root, 15, 130,135); shopping_grade.delete(0, tkinter.END); shopping_grade.insert(0, grade)
    shopping_value = generateEntry(root, 15, 130,160); shopping_value.delete(0, tkinter.END); shopping_value.insert(0, value)
    shopping_rent = generateEntry(root, 15, 130,185); shopping_rent.delete(0, tkinter.END); shopping_rent.insert(0, rent)
    shopping_fixIncome = generateEntry(root, 15, 130,210); shopping_fixIncome.delete(0, tkinter.END); shopping_fixIncome.insert(0, fixIncome)
    shopping_goodfee = generateEntry(root, 15, 130,235); shopping_goodfee.delete(0, tkinter.END); shopping_goodfee.insert(0, goodfee)
    shopping_rented = generateEntry(root, 15, 130,260); shopping_rented.delete(0, tkinter.END); shopping_rented.insert(0, str(rented))
    shopping_renter = generateEntry(root, 15, 130,285); shopping_renter.delete(0, tkinter.END); shopping_renter.insert(0, renter)
    wage = generateEntry(root, 15, 130,310); wage.delete(0, tkinter.END); wage.insert(0, shopping_wage)
    
    calisanKisiler = tkinter.Text(root, width=23, height=5, font=("cambira 12"))
    calisanKisiler.pack()
    calisanKisiler.place(x =130, y = 335 )
    calisanKisiler.insert("1.0", workers)

    root.mainloop()

def MarketDetailedScreen(id, type,owner, capacity,worker_number, grade,value, rent, fixIncome, rented, renter, foodfee, market_wage, workers):


    root = tkinter.Tk()
    root.title("Arsa Detay")
    root.geometry("350x500")
    root.config(bg="grey")

    generateLabel(root, "Alan id", "grey", ("cambria 12 bold" ), 10, 10)
    generateLabel(root, "Alan Tipi", "grey", ("cambria 12 bold" ), 10, 35)
    generateLabel(root, "Alan Sahibi", "grey", ("cambria 12 bold" ), 10, 60)
    generateLabel(root, "Kapasite", "grey", ("cambria 12 bold" ), 10, 85)
    generateLabel(root, "Calışan Sayısı", "grey", ("cambria 12 bold" ), 10, 110)
    generateLabel(root, "Seviye", "grey", ("cambria 12 bold" ), 10, 135)
    generateLabel(root, "Satış Bedeli", "grey", ("cambria 12 bold" ), 10, 160)
    generateLabel(root, "Kira Bedeli", "grey", ("cambria 12 bold" ), 10, 185)
    generateLabel(root, "Sabit Gelir", "grey", ("cambria 12 bold" ), 10, 210)
    generateLabel(root, "Yemek Fiyatı", "grey", ("cambria 12 bold" ), 10, 235)
    generateLabel(root, "Kirada mı", "grey", ("cambria 12 bold" ), 10, 260)
    generateLabel(root, "Kiracı", "grey", ("cambria 12 bold" ), 10, 285)
    generateLabel(root, "Ücret Düzeyi", "grey", ("cambria 12 bold" ), 10, 310)
    generateLabel(root, "Calışanlar", "grey", ("cambria 12 bold" ), 10, 335)


    market_id = generateEntry(root, 15, 130,10); market_id.delete(0, tkinter.END); market_id.insert(0, id)
    market_type = generateEntry(root, 15, 130,35); market_type.delete(0, tkinter.END); market_type.insert(0, type)
    market_owner = generateEntry(root,15, 130,60); market_owner.delete(0, tkinter.END); market_owner.insert(0, owner)
    market_capacity = generateEntry(root, 15, 130,85); market_capacity.delete(0, tkinter.END); market_capacity.insert(0, capacity)
    market_worker_number = generateEntry(root, 5, 130,110); market_worker_number.delete(0, tkinter.END); market_worker_number.insert(0, worker_number)
    market_grade = generateEntry(root, 15, 130,135); market_grade.delete(0, tkinter.END); market_grade.insert(0, grade)
    market_value = generateEntry(root, 15, 130,160); market_value.delete(0, tkinter.END); market_value.insert(0, value)
    market_rent = generateEntry(root, 15, 130,185); market_rent.delete(0, tkinter.END); market_rent.insert(0, rent)
    market_fixIncome = generateEntry(root, 15, 130,210); market_fixIncome.delete(0, tkinter.END); market_fixIncome.insert(0, fixIncome)
    market_goodfee = generateEntry(root, 15, 130,235); market_goodfee.delete(0, tkinter.END); market_goodfee.insert(0, foodfee)
    market_rented = generateEntry(root, 15, 130,260); market_rented.delete(0, tkinter.END); market_rented.insert(0, str(rented))
    market_renter = generateEntry(root, 15, 130,285); market_renter.delete(0, tkinter.END); market_renter.insert(0, renter)
    wage = generateEntry(root, 15, 130,310); wage.delete(0, tkinter.END); wage.insert(0, market_wage)
    
    calisanKisiler = tkinter.Text(root, width=23, height=5, font=("cambira 12"))
    calisanKisiler.pack()
    calisanKisiler.place(x =130, y = 335 )
    calisanKisiler.insert("1.0", workers)

    root.mainloop()

def RealEstateDetailedScreen(id, type,owner, capacity,worker_number, grade,value, rent, fixIncome, rented, renter, rent_commission,sold_commission, realEstate_wage, workers):
    root = tkinter.Tk()
    root.title("Arsa Detay")
    root.geometry("350x500")
    root.config(bg="grey")

    generateLabel(root, "Alan id", "grey", ("cambria 12 bold" ), 10, 10)
    generateLabel(root, "Alan Tipi", "grey", ("cambria 12 bold" ), 10, 35)
    generateLabel(root, "Alan Sahibi", "grey", ("cambria 12 bold" ), 10, 60)
    generateLabel(root, "Kapasite", "grey", ("cambria 12 bold" ), 10, 85)
    generateLabel(root, "Calışan Sayısı", "grey", ("cambria 12 bold" ), 10, 110)
    generateLabel(root, "Seviye", "grey", ("cambria 12 bold" ), 10, 135)
    generateLabel(root, "Satış Bedeli", "grey", ("cambria 12 bold" ), 10, 160)
    generateLabel(root, "Kira Bedeli", "grey", ("cambria 12 bold" ), 10, 185)
    generateLabel(root, "Sabit Gelir", "grey", ("cambria 12 bold" ), 10, 210)
    generateLabel(root, "Kira Komisyon", "grey", ("cambria 12 bold" ), 10, 235)
    generateLabel(root, "Satış Komisyon", "grey", ("cambria 12 bold" ), 10, 260)
    generateLabel(root, "Kirada mı", "grey", ("cambria 12 bold" ), 10, 285)
    generateLabel(root, "Kiracı", "grey", ("cambria 12 bold" ), 10, 310)
    generateLabel(root, "Ücret Düzeyi", "grey", ("cambria 12 bold" ), 10, 335)


    generateLabel(root, "Calışanlar: ", "grey", ("cambria 12 bold" ), 10, 360)


    emlak_id = generateEntry(root, 15, 130,10); emlak_id.delete(0, tkinter.END); emlak_id.insert(0, id)
    emlak_type = generateEntry(root, 15, 130,35); emlak_type.delete(0, tkinter.END); emlak_type.insert(0, type)
    emlak_owner = generateEntry(root,15, 130,60); emlak_owner.delete(0, tkinter.END); emlak_owner.insert(0, owner)
    emlak_capacity = generateEntry(root, 15, 130,85); emlak_capacity.delete(0, tkinter.END); emlak_capacity.insert(0, capacity)
    emlak_worker_number = generateEntry(root, 5, 130,110); emlak_worker_number.delete(0, tkinter.END); emlak_worker_number.insert(0, worker_number)
    emlak_grade = generateEntry(root, 15, 130,135); emlak_grade.delete(0, tkinter.END); emlak_grade.insert(0, grade)
    emlak_value = generateEntry(root, 15, 130,160); emlak_value.delete(0, tkinter.END); emlak_value.insert(0, value)
    emlak_rent = generateEntry(root, 15, 130,185); emlak_rent.delete(0, tkinter.END); emlak_rent.insert(0, rent)
    emlak_fixIncome = generateEntry(root, 15, 130,210); emlak_fixIncome.delete(0, tkinter.END); emlak_fixIncome.insert(0, fixIncome)
    emlak_rent_commission = generateEntry(root, 15, 130,235); emlak_rent_commission.delete(0, tkinter.END); emlak_rent_commission.insert(0, rent_commission)
    emlak_sold_commission = generateEntry(root, 15, 130,260); emlak_sold_commission.delete(0, tkinter.END); emlak_sold_commission.insert(0, sold_commission)
    emlak_rented = generateEntry(root, 15, 130,285); emlak_rented.delete(0, tkinter.END); emlak_rented.insert(0, str(rented))
    emlak_renter = generateEntry(root, 15, 130,310); emlak_renter.delete(0, tkinter.END); emlak_renter.insert(0, renter)
    wage = generateEntry(root, 15, 130,335); wage.delete(0, tkinter.END); wage.insert(0, realEstate_wage)
    
    calisanKisiler = tkinter.Text(root, width=23, height=5, font=("cambira 12"))
    calisanKisiler.pack()
    calisanKisiler.place(x =130, y = 360 )
    calisanKisiler.insert("1.0", workers)

    root.mainloop()


def Simulations(NumberofPeriod, regionList, playerList, reducingEatingAmount, reducingGoodsAmount, reducingMoneyAmount, increasingfixIncomeShare):

    for period in range(NumberofPeriod):

        for player in playerList:
           
            player.money += player.workplace.wage

            UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {player.money} WHERE Playerid = {player.id}")

            if player.workplace.rented == True:
                player.workplace.renter.money -= player.workplace.wage
                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {player.workplace.renter.money} WHERE Playerid = {player.workplace.renter.id}")
            else:
                player.workplace.owner.money -= player.workplace.wage
                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {player.workplace.owner.money} WHERE Playerid = {player.workplace.owner.id}")

            if player.workplace.type =="EMLAK":
                player.eatings -= reducingEatingAmount
                player.goods -=reducingGoodsAmount
                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Eatings = {player.eatings} WHERE Playerid = {player.id}")
                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Goods = {player.goods} WHERE Playerid = {player.id}")

                if player.eatings <= 0 or player.goods <= 0:
                    DeleteInfoFromDataBase(f"DELETE FROM {OyuncularTablosu} WHERE Playerid = {player.id}")
                    playerList.pop(playerList.index(player))

            elif player.workplace.type =="MAĞAZA":
                player.eatings -= reducingEatingAmount
                player.money -=reducingMoneyAmount
                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Eatings = {player.eatings} WHERE Playerid = {player.id}")
                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {player.money} WHERE Playerid = {player.id}")

                if player.eatings <= 0 or player.goods <= 0:
                    DeleteInfoFromDataBase(f"DELETE FROM {OyuncularTablosu} WHERE Playerid = {player.id}")
                    playerList.pop(playerList.index(player))
                
            elif player.workplace.type =="MARKET":
                player.goods -=reducingGoodsAmount
                player.money -=reducingMoneyAmount
                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {player.money} WHERE Playerid = {player.id}")
                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Goods = {player.goods} WHERE Playerid = {player.id}")

                if player.eatings <= 0 or player.goods <= 0:
                    DeleteInfoFromDataBase(f"DELETE FROM {OyuncularTablosu} WHERE Playerid = {player.id}")
                    playerList.pop(playerList.index(player))
               
                
        for region in regionList:

            if region.rented != True and region.type != "ARSA":
                region.owner.money += region.fixIncome
                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {region.owner.money} WHERE Playerid = {region.owner.id}")

            elif region.rented == True and region.type != "ARSA":
                region.renter.money += region.fixIncome
                region.renter.money -= region.rent
                region.owner.money += region.rent
                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {region.owner.money} WHERE Playerid = {region.owner.id}")
                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {region.renter.money} WHERE Playerid = {region.renter.id}")

            if region.type != "ARSA" and region.capacity == region.worker_number and region.grade <3:
                region.grade +=1
                region.capacity +=3
                region.fixIncome = region.fixIncome * (1+ (increasingfixIncomeShare /100))
                UpdateDataBase(f"UPDATE {AlanTablo[region.type]} SET Capacity = {region.capacity} WHERE Areaid = {region.id}")
                UpdateDataBase(f"UPDATE {AlanTablo[region.type]} SET FixIncome = {region.fixIncome} WHERE Areaid = {region.id}")


        




            









