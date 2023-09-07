import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import random
from ClassandFunctions import *
from DataBase import *

random.seed(2)

Marketid = 1
Magazaid = 1
Emlakid = 1

root = tkinter.Tk()
def MainScreen():

    global alanx, alany, OyuncuDetayButon, OyuncuSistemeGirisButon, BaslangicYemek, BaslangicEsya, BaslangicPara, BaslangicOyuncuSayisi, players_list, \
    OyunAlaniFrame, yoneticiParaMiktari, yoneticiEsyaMiktari, yoneticiYemekMiktari, yoneticiAlanlarSahib, yoneticiAlanlarKira, InsaatParasi, SabitGelirAO
    
    root.title("Giris Ekranı")
    root.geometry("1300x720")

    #OYUN PARAMETRELERİ
    ###################################

    OyunParametreFrame = tkinter.Frame(root, width=350, height=375, bg="coral2", highlightbackground="black", highlightthickness=2)
    OyunParametreFrame.pack()
    OyunParametreFrame.place(x = 10, y = 20)

    generateLabel(OyunParametreFrame, "OYUN PARAMETRELERİ","coral2",("Cambria 15 bold"), 55,10)
    generateLabel(OyunParametreFrame, "Oyun Alanı","coral2",("Cambria 12 bold"), 10,50)
    generateLabel(OyunParametreFrame, "Oyun Bitiş Tarihi","coral2",("Cambria 12 bold"), 10,80)
    generateLabel(OyunParametreFrame, "Başlangıç Yemek Miktarı","coral2",("Cambria 12 bold"), 10,110)
    generateLabel(OyunParametreFrame, "Başlangıç Eşya Miktarı","coral2",("Cambria 12 bold"), 10,140)
    generateLabel(OyunParametreFrame, "Başlangıç Para Miktarı","coral2",("Cambria 12 bold"), 10,170)
    generateLabel(OyunParametreFrame, "Oyuncu Sayısı","coral2",("Cambria 12 bold"), 10,200)
    generateLabel(OyunParametreFrame, "Eksilecek Yemek Miktarı","coral2",("Cambria 12 bold"), 10,230)
    generateLabel(OyunParametreFrame, "Eksilecek Eşya Miktarı","coral2",("Cambria 12 bold"), 10,260)
    generateLabel(OyunParametreFrame, "Eksilecek Para Miktarı","coral2",("Cambria 12 bold"), 10,290)
    generateLabel(OyunParametreFrame, "İnşaat Parası  /  Sabit Gelir AO","coral2",("Times 10 bold"), 10,320)


    alanx = generateSpin(OyunParametreFrame, 1, 5, 3, list(range(1,6)), ("arial 10 bold"), 220, 50)
    alany = generateSpin(OyunParametreFrame, 1, 5, 3, list(range(1,6)), ("arial 10 bold"), 270, 50)
    satirsayisi = int(alany.get())
    sutunsayisi = int(alanx.get())

    cal = DateEntry(OyunParametreFrame, font = ("arial 10 bold"))
    cal.pack()
    cal.place(x = 220, y = 80)

    BaslangicYemek = generateEntry(OyunParametreFrame, 5, 220, 110); BaslangicYemek.insert(0, "2000")
    BaslangicEsya = generateEntry(OyunParametreFrame, 5, 220, 140); BaslangicEsya.insert(0, "2000")
    BaslangicPara = generateEntry(OyunParametreFrame, 5, 220, 170); BaslangicPara.insert(0, "2000")
    BaslangicOyuncuSayisi = generateEntry(OyunParametreFrame, 5, 220, 200); BaslangicOyuncuSayisi.insert(0, str(satirsayisi*sutunsayisi*2)); BaslangicOyuncuSayisi["state"] = "readonly"

    EksilecekYemek = generateEntry(OyunParametreFrame, 5, 220, 230); EksilecekYemek.insert(0, "50")
    EksilecekEsya = generateEntry(OyunParametreFrame, 5, 220, 260); EksilecekEsya.insert(0, "50")
    EksilecekPara = generateEntry(OyunParametreFrame, 5, 220, 290); EksilecekPara.insert(0, "10")

    InsaatParasi = generateEntry(OyunParametreFrame, 5, 20, 340); InsaatParasi.insert(0, "1000") 
    SabitGelirAO = generateEntry(OyunParametreFrame, 5, 110, 340); SabitGelirAO.insert(0, "%20")


    girisbutonu = tkinter.Button(OyunParametreFrame, text="MetaLand Olustur", bg="white",
                                            fg="black", width=15, font = ("arial 10 bold"),
                                            command=lambda:[generateRegions(int(alany.get()),int(alanx.get())),
                                                            generatePlayers(int(alany.get())*int(alanx.get())*2, BaslangicYemek, BaslangicEsya, BaslangicPara),
                                                            assignPersontoWrokplace(),
                                                            generateButtons(int(alany.get()),int(alanx.get()), players),
                                                            YoneticiBilgiGuncelle(administer, regions, yoneticiParaMiktari, yoneticiEsyaMiktari,
                                                                                  yoneticiYemekMiktari, yoneticiAlanlarSahib, yoneticiAlanlarKira),
                                                            GenerateDataBase(regions, players)
                                                            ]
                                                            )
    girisbutonu.pack()
    girisbutonu.place(x = 200, y = 335)

    #OYUN ALANI
    ###########################################################
    OyunAlaniFrame = tkinter.Frame(root, width=800, height=700)
    OyunAlaniFrame.pack()
    OyunAlaniFrame.place(x = 375, y = 10) 

    #OYUNCU BİLGİLERİ
    ############################################################
    OyuncuBilgiAlaniFrame = tkinter.Frame(root, width=350, height=75, bg="coral2", highlightbackground="black", highlightthickness=2)
    OyuncuBilgiAlaniFrame.pack()
    OyuncuBilgiAlaniFrame.place(x = 10, y = 400) 

    generateLabel(OyuncuBilgiAlaniFrame, "OYUNCU BİLGİLERİ","coral2",("Cambria 12 bold"), 5,0)

    players_list = ttk.Combobox(OyuncuBilgiAlaniFrame, width=15, font = ("arial 13 bold"))
    selected = tkinter.StringVar(OyuncuBilgiAlaniFrame)
    players_list["textvariable"] = selected
    players_list.pack()
    players_list.place(x = 5, y = 30)
    players_list.set("Oyuncu Seçiniz")

    OyuncuDetayButon = tkinter.Button(OyuncuBilgiAlaniFrame, text="Oyuncu Detay",
                                    font = ("arial 10 bold"), command=lambda: [PlayerDetailedScreen(players_list)],
                                        state="disabled"
                                        )
    OyuncuDetayButon.pack()
    OyuncuDetayButon.place(x =170, y = 30 )


    #OYUNCU SİSTEME GİRİŞ
    #############################################################
    OyuncuSistemeGirisFrame = tkinter.Frame(root, width=350, height=150, bg="coral2", highlightbackground="black", highlightthickness=2)
    OyuncuSistemeGirisFrame.pack()
    OyuncuSistemeGirisFrame.place(x = 10, y = 480) 

    generateLabel(OyuncuSistemeGirisFrame, "OYUNCU SİSTEME GİRİŞ","coral2",("Cambria 15 bold"), 60,5)
    generateLabel(OyuncuSistemeGirisFrame, "Kullanıcı Adı: ","coral2",("Cambria 15 bold"), 10,40)
    generateLabel(OyuncuSistemeGirisFrame, "Şifre: ","coral2",("Cambria 15 bold"), 10,70)

    usernameEntry = generateEntry(OyuncuSistemeGirisFrame, 10, 140, 40)
    usernameEntry.insert(0, "RızaKork17")
    passwordEntry = generateEntry(OyuncuSistemeGirisFrame, 10, 140, 70)
    passwordEntry.insert(0, "78860")

    OyuncuSistemeGirisButon = tkinter.Button(OyuncuSistemeGirisFrame, text="Giriş",
                                    font = ("arial 12 bold"), command=lambda: [playerLoggin(usernameEntry.get(), passwordEntry.get(),
                                                                                            players, regions)],
                                        state="disabled"
                                        )
    OyuncuSistemeGirisButon.pack()
    OyuncuSistemeGirisButon.place(x =140, y = 100 )

    #SİMÜLASYON EKRANI
    ###############################################################

    SimulasyonFrame = tkinter.Frame(root, width=350, height=75, bg="coral2", highlightbackground="black", highlightthickness=2)
    SimulasyonFrame.pack()
    SimulasyonFrame.place(x = 10, y = 635) 

    generateLabel(SimulasyonFrame, "SİMULASYON","coral2",("Cambria 15 bold"), 100,0)
    generateLabel(SimulasyonFrame, "Dönem Sayısı: ","coral2",("Cambria 12 bold"), 0,40)

    donemSayisi = generateSpin(SimulasyonFrame, 1, 10, 7, list(range(1,11)), ("Times 12 bold"), 110, 40)

    print(int(donemSayisi.get()), regions, players, 
          float(EksilecekYemek.get()), float(EksilecekEsya.get()), float(EksilecekPara.get()), 
          float(SabitGelirAO.get()[1:]))


    SimulasyonButon = tkinter.Button(SimulasyonFrame, text="Simule Et",
                                    font = ("arial 10 bold"), command=lambda: [Simulations( int(donemSayisi.get()), 
                                                                                            regions,
                                                                                            players,   
                                                                                            float(EksilecekYemek.get()),
                                                                                            float(EksilecekEsya.get()), 
                                                                                            float(EksilecekPara.get()),                                                                                             
                                                                                            float(SabitGelirAO.get()[1:])
                                                                                            ),

                                                                                            generateButtons(int(alany.get()),int(alanx.get()), players)
                                                                                           ])
    SimulasyonButon.pack()
    SimulasyonButon.place(x =200, y = 37 )


    # YÖNETİCİ EKRANI
    ##########################################################
    YoneticiFrame = tkinter.Frame(root, width=800, height=100, bg="coral2", highlightbackground="black", highlightthickness=2)
    YoneticiFrame.pack()
    YoneticiFrame.place(x = 370, y = 610) 

    generateLabel(YoneticiFrame, "Yönetici Oyun Bilgileri ","coral2",("Cambria 13 bold"), 300,0)
    generateLabel(YoneticiFrame, "Para Miktarı","coral2",("Cambria 12 bold"), 0,30)
    generateLabel(YoneticiFrame, "Eşya Miktarı","coral2",("Cambria 12 bold"), 0,60)
    generateLabel(YoneticiFrame, "Yemek Miktarı","coral2",("Cambria 12 bold"), 230,30)
    generateLabel(YoneticiFrame, "Sahip Olunan Arsa/İşletme","coral2",("Cambria 12 bold"), 470,30)
    generateLabel(YoneticiFrame, "Kiradaki İşletme","coral2",("Cambria 12 bold"), 470,60)

    yoneticiParaMiktari = generateEntry(YoneticiFrame, 10, 110,30)
    yoneticiEsyaMiktari = generateEntry(YoneticiFrame, 10, 110,60)
    yoneticiYemekMiktari = generateEntry(YoneticiFrame, 10, 350,30)
    yoneticiAlanlarSahib = generateCombobox(YoneticiFrame,10, ("Times 10 bold"), 675, 30)
    yoneticiAlanlarKira = generateCombobox(YoneticiFrame,10, ("Times 10 bold"), 675, 60)

    #VERİ TABANI EKRANI
    ##########################################################
    DataBaseFrame = tkinter.Frame(root, width=120, height=700, bg="coral2", highlightbackground="black", highlightthickness=2)
    DataBaseFrame.pack()
    DataBaseFrame.place(x = 1175, y = 10) 
    
    generateLabel(DataBaseFrame, "TABLOLAR","coral2",("Cambria 13 bold underline"), 0,100)

    OyuncularButon = tkinter.Button(DataBaseFrame, text="Oyuncular", bg="coral2" ,   font = ("arial 10 bold"), command=lambda: [GetInfoFromDataBase(OyuncularTablosu)]).place(x =5, y = 130 )
    TumAlanlarButon = tkinter.Button(DataBaseFrame, text="Tüm Alanlar", bg="coral2" ,font = ("arial 10 bold"), command=lambda: [GetInfoFromDataBase(AlanlarTablosu)]).place(x =5, y = 170 )
    MarketButon = tkinter.Button(DataBaseFrame, text="Market", bg="coral2" ,font = ("arial 10 bold"), command=lambda: [GetInfoFromDataBase(MarketTablosu)]).place(x =5, y = 210 )
    MağazaButon = tkinter.Button(DataBaseFrame, text="Mağaza", bg="coral2" ,font = ("arial 10 bold"), command=lambda: [GetInfoFromDataBase(MagazaTablosu)]).place(x =5, y = 250 )
    EmlakButon = tkinter.Button(DataBaseFrame, text="Emlak", bg="coral2" ,font = ("arial 10 bold"), command=lambda: [GetInfoFromDataBase(EmlakTablosu)]).place(x =5, y = 290 )
    AlanTipleri = tkinter.Button(DataBaseFrame, text="ALAN TİPLERİ", bg="coral2" , font = ("arial 10 bold"), command=lambda: [GetInfoFromDataBase(AlanTipiTablosu)]).place(x =5, y = 360 )
    Roller = tkinter.Button(DataBaseFrame, text="ROLLER", bg="coral2" ,font = ("arial 10 bold"), command=lambda: [GetInfoFromDataBase(RollerTablosu)]).place(x =5, y = 400 )


MainScreen()
#----------------------------------------------------------------------

def generateButtons(x,y, oyuncu_listesi):

    BaslangicOyuncuSayisi["state"] = "normal"
    BaslangicOyuncuSayisi.delete(0, tkinter.END)
    BaslangicOyuncuSayisi.insert(0, str(int(alany.get())*int(alanx.get())*2))
    BaslangicOyuncuSayisi["state"] = "readonly"
    OyuncuDetayButon["state"] = "active"
    OyuncuSistemeGirisButon["state"] = "active"

    options = [str(x.id)+" - " + x.name +" "+ x.surname for x in players]
    players_list["values"] = options

    for widgets in OyunAlaniFrame.winfo_children():
        widgets.destroy()

    index = 0
    for i in range(y):
        for j in range(x):

            region = regions[index]
            lang = regions[index].getInfo()
            a = lang.split("\n")

            if a[1] =="ARSA":
                id            = a[0]
                type          = a[1]
                owner         = a[2]
                value         = a[3]

                def action(land_id = id, land_type = type, land_owner = owner, land_value = value):

                    LandDetailedScreen(land_id, land_type, land_owner, land_value)

                AlanButon = tkinter.Button(OyunAlaniFrame, text="Alan id: {}\nAlan Tipi: {}".format(id, type),
                                        width=14, height=5,
                                        font = ("arial 11 bold"),
                                        background="pink",
                                        command=action)
                AlanButon.pack()
                AlanButon.place(x = j*150+50, y = i*120+10)
                index+=1

            else:
                id            = a[0]
                type          = a[1]
                owner         = a[2]
                capacity      = a[3]
                workerNumber  = a[4]
                grade         = a[5]
                value         = a[6]
                rent          = a[7]
                fixincome     = a[8]
                rented        = a[9]
                renter        = a[10]


                if a[1] =="MAĞAZA":
                    goodfee       = a[11]
                    shopping_wage   = a[12]

                    def action(shoppingcenter_id = id, shoppingcenter_type = type, shoppingcenter_owner = owner,
                               shoppingcenter_capacity = capacity, shoppingcenter_worker_number = workerNumber,
                                shoppingcenter_grade = grade,  shoppingcenter_value = value, shoppingcenter_rent = rent, shoppingcenter_fixincome = fixincome,
                                shoppingcenter_rented = rented, shoppingcenter_renter = renter,
                                shoppingcenter_goodfee = goodfee, ShoppingWage = shopping_wage,  shoppingcenter_workers = CalisanListesiOlustur(oyuncu_listesi, region)):
                        
                        ShoppingDetailedScreen(shoppingcenter_id, shoppingcenter_type,shoppingcenter_owner, shoppingcenter_capacity,shoppingcenter_worker_number,
                                             shoppingcenter_grade,shoppingcenter_value, shoppingcenter_rent, shoppingcenter_fixincome,
                                              shoppingcenter_rented, shoppingcenter_renter, shoppingcenter_goodfee, ShoppingWage, shoppingcenter_workers)

                    AlanButon = tkinter.Button(OyunAlaniFrame, text="Alan id: {}\nAlan Tipi: {}".format(id, type),
                                            width=14, height=5,
                                            font = ("arial 11 bold"),
                                            background="pink",
                                            command=action)
                    AlanButon.pack()
                    AlanButon.place(x = j*150+50, y = i*120+10)
                    index+=1   

                if a[1] =="MARKET":
                    food_fee       = a[11]
                    market_wage    = a[12]

                    def action(market_id = id, market_type = type, market_owner = owner,
                               market_capacity = capacity, market_worker_number = workerNumber,
                                market_grade = grade,  market_value = value, market_rent = rent, market_fixincome = fixincome,
                                market_rented = rented, market_renter = renter,
                                market_foodfee = food_fee, MarketWage = market_wage, market_workers = CalisanListesiOlustur(oyuncu_listesi, region)):
                        
                        MarketDetailedScreen(market_id, market_type,market_owner, market_capacity,market_worker_number,
                                             market_grade,market_value, market_rent, market_fixincome,
                                             market_rented, market_renter, market_foodfee, MarketWage, market_workers)

                    AlanButon = tkinter.Button(OyunAlaniFrame, text="Alan id: {}\nAlan Tipi: {}".format(id, type),
                                            width=14, height=5,
                                            font = ("arial 11 bold"),
                                            background="pink",
                                            command=action)
                    AlanButon.pack()
                    AlanButon.place(x = j*150+50, y = i*120+10)
                    index+=1     

                if a[1] =="EMLAK":
                    rent_commission       = a[11]
                    sold_commission       = a[12]
                    realEstate_wage       = a[13]

                    def action(emlak_id = id, emlak_type = type, emlak_owner = owner,
                               emlak_capacity = capacity, emlak_worker_number = workerNumber,
                                emlak_grade = grade,  emlak_value = value, emlak_rent = rent, emlak_fixincome = fixincome,
                                emlak_rented = rented, emlak_renter = renter,
                                emlak_rent_commission = rent_commission,  emlak_sold_commission = sold_commission, RealEstateWage = realEstate_wage,
                                emlak_workers = CalisanListesiOlustur(oyuncu_listesi, region)):
                        
                        RealEstateDetailedScreen(emlak_id, emlak_type,emlak_owner, emlak_capacity,emlak_worker_number,
                                             emlak_grade,emlak_value, emlak_rent, emlak_fixincome,
                                             emlak_rented,emlak_renter, emlak_rent_commission,emlak_sold_commission, RealEstateWage, emlak_workers)

                    AlanButon = tkinter.Button(OyunAlaniFrame, text="Alan id: {}\nAlan Tipi: {}".format(id, type),
                                            width=14, height=5,
                                            font = ("arial 11 bold"),
                                            background="pink",
                                            command=action)
                    AlanButon.pack()
                    AlanButon.place(x = j*150+50, y = i*120+10)
                    index+=1                

def playerLoggin(username, password, oyuncular, alanlar):

    logginplayer = administer
    playerindex = 0
    for player in players:
        if player.username == username and str(player.password) == password:
            logginplayer = player
            break
        playerindex+=1

    PlayerScreen(logginplayer, oyuncular,alanlar, playerindex)
 
def PlayerScreen(logginplayer, oyuncular, alanlar, oyuncuindex):

    root = tkinter.Tk()
    root.title("Oyuncu Ekranı")
    root.geometry("880x600")
    root.config(bg="lightblue")

    frame1 = tkinter.Frame(root, width=280, height=575, bg="white")
    frame1.pack()
    frame1.place(x = 590, y = 10 )

    #HESAP BİLGİLERİ
    #######################################################
    #######################################################
    frame11 = tkinter.Frame(frame1, width=280, height=150, bg="white", highlightbackground="black", highlightthickness=2)
    frame11.pack()
    frame11.place(x = 0, y = 0)

    generateLabel(frame11, "HESAP BİLGİLERİ", "white", ("times 14 bold underline"), 10, 10)
    generateLabel(frame11, "Kullanıcı Adı:", "white", ("cambira 12 bold"), 10, 50 )
    generateLabel(frame11, "Şifre:", "white", ("cambira 12 bold"), 10, 80 )
    
    username = generateEntry(frame11, 12, 120, 50)
    password = generateEntry(frame11, 12, 120, 80)

    username.delete(0, tkinter.END)
    username.insert(0, logginplayer.username)
    password.delete(0, tkinter.END)
    password.insert(0, str(logginplayer.password))

    #OYUN BİLGİLERİ
    #######################################################
    ####################################################### 
    frame12 = tkinter.Frame(frame1, width=280, height=425, bg="white", highlightbackground="black", highlightthickness=2)
    frame12.pack()
    frame12.place(x = 0, y = 151)

    generateLabel(frame12, "OYUN BİLGİLERİ", "white", ("times 14 bold underline"), 10, 10)
    generateLabel(frame12, "İşyeri", "white", ("cambira 12 bold"), 10, 50 )
    generateLabel(frame12, "Para Miktarı", "white", ("cambira 12 bold"), 10, 80 )
    generateLabel(frame12, "Yemek Miktarı", "white", ("cambira 12 bold"), 10, 110 )
    generateLabel(frame12, "Eşya Miktarı", "white", ("cambira 12 bold"), 10, 140 )
    generateLabel(frame12, "İ-A (Sahibi)", "white", ("cambira 12 bold"), 10, 170 )
    generateLabel(frame12, "İ-A (Kiradaki)", "white", ("cambira 12 bold"), 10, 200 )
    generateLabel(frame12, "İ-A (Kiracıyım)", "white", ("cambira 12 bold"), 10, 230 )

    workplace = generateEntry(frame12, 15, 125, 50)
    money = generateEntry(frame12, 12, 125, 80)
    eatings = generateEntry(frame12, 12, 125, 110)
    goods = generateEntry(frame12, 12, 125, 140)

    sahibolunanalan = generateCombobox(frame12, 12, ("cambira 10"), 125,170)
    sahibolunanalan["value"] = [str(x.id) + " - " + x.type for x in alanlar if x.owner.id == logginplayer.id ]
    sahibolunanalan.set("Seçim Yapınız")
    
    kiradaki = generateCombobox(frame12, 12, ("cambira 10"), 125,200)
    kiradaki["value"] = [str(x.id) + " - " + x.type for x in alanlar if x.owner.id == logginplayer.id and 
                         x.rented == True]
    kiradaki.set("Seçim Yapınız")

    kiraciyım = generateCombobox(frame12, 12, ("cambira 10"), 125,230)
    kiraciyım["value"] = [str(x.id) + " - " + x.type for x in alanlar 
                          if x.type !="ARSA" and type(x.renter) !=str and  x.renter.id == logginplayer.id]
    kiraciyım.set("Seçim Yapınız")


    workplace.delete(0, tkinter.END)
    workplace.insert(0, str(logginplayer.workplace.id) + " nolu " + logginplayer.workplace.type)
    money.delete(0, tkinter.END)
    money.insert(0, str(logginplayer.money))

    eatings.delete(0, tkinter.END)
    eatings.insert(0, str(logginplayer.eatings))
    goods.delete(0, tkinter.END)
    goods.insert(0, str(logginplayer.goods))

    isim = logginplayer.name + " " + logginplayer.surname
    generateLabel(frame12, "HOŞGELDİN", "lightblue", ("helvetica 16 italic bold underline"), 85, 280)
    generateLabel(frame12, isim, "lightblue", ("helvetica 16 italic bold underline"), 85, 320)

    #SATINALMA BİLGİLERİ
    #######################################################
    #######################################################  
    frame2 = tkinter.Frame(root, width=570, height=580, bg="white")
    frame2.pack()
    frame2.place(x = 10, y = 10 )

    frame21 = tkinter.Frame(frame2, width=555, height=110, bg="white",highlightbackground="black", highlightthickness=1)
    frame21.pack()
    frame21.place(x = 10, y = 10 )

    generateLabel(frame21, "SATINALMA İŞLEMLERİ", "lightblue", ("helvetica 13 bold"), 0, 0)
    generateLabel(frame21, "Yemek", "white", ("helvetica 12 bold"), 5, 50)
    generateLabel(frame21, "Eşya", "white", ("helvetica 12 bold"), 5, 80)
    
    generateLabel(frame21, "İşletme", "white", ("helvetica 12 bold"), 100, 25)
    generateLabel(frame21, "Fiyat", "white", ("helvetica 12 bold"), 235, 25)
    generateLabel(frame21, "Miktar", "white", ("helvetica 12 bold"), 305, 25)
    generateLabel(frame21, "Maliyet", "white", ("helvetica 12 bold"), 385, 25)

    yemekisletme_combo = generateCombobox(frame21, 15, ("cambira 10"), 65, 50)
    esyaisletme_combo = generateCombobox(frame21, 15, ("cambira 10"), 65, 80)
    yemekisletme_combo["values"] = [str(x.id) + " - " + x.type for x in alanlar if x.type == "MARKET"]
    esyaisletme_combo["values"] = [str(x.id) + " - " + x.type for x in alanlar if x.type == "MAĞAZA"]

    yemek_fiyat = generateEntry(frame21, 10, 200,50)
    esya_fiyat = generateEntry(frame21, 10, 200,80)
    yemek_miktar = generateSpin(frame21, 1,10,3,list(range(1,11)),("times 12 bold"), 310,50)
    yemek_miktar.configure(command=lambda: [yemekMaliyet()])
    esya_miktar = generateSpin(frame21, 1,10,3,list(range(1,11)),("times 12 bold"), 310,80)
    esya_miktar.configure(command=lambda: [esyaMaliyet()])

    yemek_maliyet = generateEntry(frame21, 12, 370, 50)
    esya_maliyet = generateEntry(frame21, 12, 370, 80)

    def yemekMaliyet():
        price = float(yemek_fiyat.get())
        miktar = float(yemek_miktar.get())
        yemek_maliyet.delete(0, tkinter.END)
        yemek_maliyet.insert(0, str(round(price*miktar,2)))

    def esyaMaliyet():
        price = float(esya_fiyat.get())
        miktar = float(esya_miktar.get())
        esya_maliyet.delete(0, tkinter.END)
        esya_maliyet.insert(0, str(round(price*miktar,2)))

    def on_select_food(event):
        yemek_fiyat.delete(0, tkinter.END)
        selected = event.widget.get()
        isletme = [x for x in alanlar if x.id == int(selected[0: selected.index(" ")])][0]
        yemek_fiyat.insert(0, str(isletme.food_fee)) 
        price = float(yemek_fiyat.get())
        miktar = float(yemek_miktar.get())
        yemek_maliyet.delete(0, tkinter.END)
        yemek_maliyet.insert(0, str(round(price*miktar,2)))

    yemekisletme_combo.bind('<<ComboboxSelected>>', on_select_food)

    def on_select_good(event):
        esya_fiyat.delete(0, tkinter.END)
        selected = event.widget.get()
        isletme = [x for x in alanlar if x.id == int(selected[0: selected.index(" ")])][0]
        esya_fiyat.insert(0, str(isletme.good_fee)) 

        price = float(esya_fiyat.get())
        miktar = float(esya_miktar.get())
        esya_maliyet.delete(0, tkinter.END)
        esya_maliyet.insert(0, str(round(price*miktar,2)))

    esyaisletme_combo.bind('<<ComboboxSelected>>', on_select_good)

    yemekokey = generateButton(frame21, "OK","white","black", 3, ("helvetica 8 bold"), 500,47 )
    yemekokey.configure(command=lambda: [yemekOkeyButton()])

    esyaokey = generateButton(frame21, "OK","white","black", 3, ("helvetica 8 bold"), 500,77 )
    esyaokey.configure(command=lambda: [esyaOkeyButton()])


    def yemekOkeyButton():
        toplamMaliyet = float(yemek_maliyet.get())
        oyuncuPara = float(money.get())
        mevcutYemekMiktari = int(eatings.get())
        artiyemekMiktari = int(yemek_miktar.get())
        yeniYemekMiktari = mevcutYemekMiktari + artiyemekMiktari
        isletmeid = yemekisletme_combo.get()[0: yemekisletme_combo.get().index(" ")]
        isletme = [x for x in alanlar if str(x.id) == isletmeid][0]
        

        if toplamMaliyet > oyuncuPara:
            yemekisletme_combo.delete(0, tkinter.END)
            yemek_fiyat.delete(0, tkinter.END)
            yemek_maliyet.delete(0, tkinter.END)
            messagebox.showinfo("showinfo", "PARANIZ YETERSİZ")

        else:
            logginplayer.money -=toplamMaliyet
            logginplayer.eatings +=artiyemekMiktari
            money.delete(0, tkinter.END)
            money.insert(0, str(round(logginplayer.money,2)))
            eatings.delete(0, tkinter.END)
            eatings.insert(0, yeniYemekMiktari)
            isletme.owner.money +=toplamMaliyet


            UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {logginplayer.money} WHERE Playerid = {logginplayer.id}")
            UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Eatings = {logginplayer.eatings} WHERE Playerid = {logginplayer.id}")
            UpdateDataBase(f"UPDATE {OyuncularTablosu} SET  Money = {isletme.owner.money} WHERE Playerid = {isletme.owner.id}")

            yemekisletme_combo.delete(0, tkinter.END)
            yemek_fiyat.delete(0, tkinter.END)
            yemek_maliyet.delete(0, tkinter.END)

    def esyaOkeyButton():

        toplamMaliyet = float(esya_maliyet.get())
        oyuncuPara = float(money.get())
        mevcutEsyaMiktari = int(goods.get())
        artiEsyaMiktari = int(esya_miktar.get())
        yeniEsyaMiktari = mevcutEsyaMiktari + artiEsyaMiktari
        isletmeid = esyaisletme_combo.get()[0: esyaisletme_combo.get().index(" ")]
        isletme = [x for x in alanlar if str(x.id) == isletmeid][0]
        

        if toplamMaliyet > oyuncuPara:
            esyaisletme_combo.delete(0, tkinter.END)
            esya_fiyat.delete(0, tkinter.END)
            esya_maliyet.delete(0, tkinter.END)
            messagebox.showinfo("showinfo", "PARANIZ YETERSİZ")

        else:
            logginplayer.money -=toplamMaliyet
            logginplayer.goods +=artiEsyaMiktari
            money.delete(0, tkinter.END)
            money.insert(0, str(round(logginplayer.money,2)))
            goods.delete(0, tkinter.END)
            goods.insert(0, yeniEsyaMiktari)
            isletme.owner.money +=toplamMaliyet

            UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {logginplayer.money} WHERE Playerid = {logginplayer.id}")
            UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Goods = {logginplayer.goods} WHERE Playerid = {logginplayer.id}")
            UpdateDataBase(f"UPDATE {OyuncularTablosu} SET  Money = {isletme.owner.money} WHERE Playerid = {isletme.owner.id}")

            esyaisletme_combo.delete(0, tkinter.END)
            esya_fiyat.delete(0, tkinter.END)
            esya_maliyet.delete(0, tkinter.END)

    #İŞLETME YAP
    ###############################################################
    ###############################################################
    frame23 = tkinter.Frame(frame2, width=555, height=155, bg="white",highlightbackground="black", highlightthickness=1)
    frame23.pack()
    frame23.place(x = 10, y = 400 )

    generateLabel(frame23, "İŞLETME YAP", "lightblue", ("helvetica 13 bold"), 0, 0)
    generateLabel(frame23, "Arsa Seç", "white", ("helvetica 12 bold"), 5, 30)
    generateLabel(frame23, "İşletme Türü Seç", "white", ("helvetica 12 bold"), 5, 60)
    generateLabel(frame23, "Maliyet", "white", ("helvetica 12 bold"), 5, 90)
    
    mevcutArsalar = generateCombobox(frame23, 15, ("cambira 10"), 150, 30)

    isletmeTuru = generateCombobox(frame23, 15, ("cambira 10"), 150, 60)
    isletmeTuru["values"] = ["Market", "Mağaza", "Emlak"]

    def isletmeTuruKontrol(event):
        value = InsaatParasi.get()
        binamaliyet.delete(0, tkinter.END)
        binamaliyet.insert(0, value)
        
    isletmeTuru.bind('<<ComboboxSelected>>', isletmeTuruKontrol)

    binamaliyet= generateEntry(frame23, 12, 150, 90 )
    binamaliyet.config(bg="grey")


    insaatokey = generateButton(frame23, "İşletme Yap","white","black", 10, ("helvetica 10 bold"), 150,120 )
    insaatokey.configure(command=lambda: [insaatOkButton()])

    def insaatOkButton():

        global Marketid, Magazaid, Emlakid

        insaatMaliyeti = float(binamaliyet.get())
        oyuncuPara = logginplayer.money

        arsaid = mevcutArsalar.get()[0: mevcutArsalar.get().index(" ")]
        kurulacakİsletme = isletmeTuru.get()

        if insaatMaliyeti > oyuncuPara:
            messagebox.showinfo("showinfo", "PARANIZ YETERSİZ")
            mevcutArsalar.delete(0, tkinter.END)
            isletmeTuru.delete(0, tkinter.END)
            binamaliyet.delete(0, tkinter.END)
            return
        
        else:
            if kurulacakİsletme == "Market":
                isletme = Market(int(arsaid),"MARKET", logginplayer, 3,0,1)
                alanlar[int(arsaid) - 1] = isletme
                logginplayer.money -=insaatMaliyeti
                administer.money += insaatMaliyeti

                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {logginplayer.money} WHERE Playerid = {logginplayer.id}")
                UpdateDataBase(f"UPDATE {AlanlarTablosu} SET AreaTypeid = {AreaTypesTableDict[isletme.type]} WHERE Areaid = {int(arsaid)}")
                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {administer.money} WHERE Playerid = {int(administer.id)}")
                insertinfo("markets_table", [Marketid, isletme.capacity, isletme.worker_number, isletme.grade, isletme.rent, isletme.fixIncome, isletme.food_fee, isletme.wage, isletme.id ])
                Marketid+=1

            if kurulacakİsletme == "Mağaza":
                isletme = ShoppingCenter(int(arsaid),"MAĞAZA", logginplayer, 3,0,1)
                alanlar[int(arsaid) - 1] = isletme
                logginplayer.money -=insaatMaliyeti
                administer.money += insaatMaliyeti

                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {logginplayer.money} WHERE Playerid = {logginplayer.id}")
                UpdateDataBase(f"UPDATE {AlanlarTablosu} SET AreaTypeid = {AreaTypesTableDict[isletme.type]} WHERE Areaid = {int(arsaid)}")
                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {administer.money} WHERE Playerid = {int(administer.id)}")
                insertinfo("shoppingcenters_table", [Magazaid, isletme.capacity, isletme.worker_number, isletme.grade, isletme.rent, isletme.fixIncome, isletme.good_fee, isletme.wage, isletme.id ])
                Magazaid+=1



            if kurulacakİsletme == "Emlak":
                isletme = RealEstate(int(arsaid),"EMLAK", logginplayer,3,0,1)
                alanlar[int(arsaid) - 1] = isletme
                logginplayer.money -=insaatMaliyeti
                administer.money += insaatMaliyeti

                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {logginplayer.money} WHERE Playerid = {logginplayer.id}")
                UpdateDataBase(f"UPDATE {AlanlarTablosu} SET AreaTypeid = {AreaTypesTableDict[isletme.type]} WHERE Areaid = {int(arsaid)}")
                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {administer.money} WHERE Playerid = {int(administer.id)}")

                insertinfo("realestates_tables", [Emlakid,  isletme.capacity, isletme.worker_number, isletme.grade, isletme.rent,
                                                   isletme.fixIncome, isletme.rent_commission, isletme.sold_commission, isletme.wage, isletme.id])
                Emlakid+=1


            mevcutArsalar.delete(0, tkinter.END)
            isletmeTuru.delete(0, tkinter.END)
            binamaliyet.delete(0, tkinter.END)

            money.delete(0, tkinter.END)
            money.insert(0, str(oyuncuPara -insaatMaliyeti))
            sahibolunanalan["value"] = [str(x.id) + " - " + x.type for x in alanlar if x.owner.id == logginplayer.id ]
            arsaIsletme_kombo["value"] = [str(x.id) + " - " + x.type for x in alanlar if x.owner.id != logginplayer.id]
            mevcutArsalar["values"] = [str(x.id) + " - " + x.type for x in alanlar if x.type == "ARSA" and x.owner.id == logginplayer.id]
            islem_combo.bind('<<ComboboxSelected>>', islemTuruKontrol)
            generateButtons(int(alany.get()),int(alanx.get()), players)
        
    #ÇALIŞMA YERİ DEĞİŞTİR
    ###############################################################
    ###############################################################
    generateLabel(frame23, "ÇALIŞMA YERİ", "lightblue", ("helvetica 13 bold"), 300, 0)
    generateLabel(frame23, "Mevcut ÇY", "white", ("helvetica 12 bold"), 300, 30)
    generateLabel(frame23, "ÇY Değiştir", "white", ("helvetica 12 bold"), 300, 60)

    mevcutCY= generateEntry(frame23, 14, 400, 30 )
    mevcutCY.insert(0, str(logginplayer.workplace.id) + " nolu " + logginplayer.workplace.type)
    CYDegistir = generateCombobox(frame23, 15, ("cambira 10"), 400, 60)
    CYDegistir["values"] = [str(x.id) + " " + x.type for x in alanlar if logginplayer.workplace != x and x.renter != logginplayer and  x.owner !=logginplayer and x.type != "ARSA"]
    CYDegistir.set("Seçim Yap")
    
    calismaOk = generateButton(frame23, "OK","white","black", 6, ("helvetica 10 bold"), 400,90)
    calismaOk.configure(command=lambda:[calismaDegistirButtonOk()])

    def calismaDegistirButtonOk():

        MevcutCalismaYeri = [x for x in alanlar if logginplayer.workplace == x][0]
        TalepedilenCalismaYeri = [x for x in alanlar if str(x.id) == CYDegistir.get()[0: CYDegistir.get().index(" ")]][0]


        if TalepedilenCalismaYeri.capacity > TalepedilenCalismaYeri.worker_number:

            TalepedilenCalismaYeri.worker_number +=1
            MevcutCalismaYeri.worker_number -=1
            logginplayer.workplace = TalepedilenCalismaYeri

            UpdateDataBase(f"UPDATE {AlanTablo[MevcutCalismaYeri.type]} SET WorkerNumber = {MevcutCalismaYeri.worker_number} WHERE Areaid = {MevcutCalismaYeri.id}")
            UpdateDataBase(f"UPDATE {AlanTablo[TalepedilenCalismaYeri.type]} SET WorkerNumber = {TalepedilenCalismaYeri.worker_number} WHERE Areaid = {TalepedilenCalismaYeri.id}")
            UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Workplaceid = {logginplayer.workplace.id} WHERE Playerid = {logginplayer.id}")

            generateButtons(int(alany.get()),int(alanx.get()), players)
            CYDegistir.set("Seçim Yap")
            mevcutCY.delete(0, tkinter.END)
            mevcutCY.insert(0, str(logginplayer.workplace.id) + " nolu " + logginplayer.workplace.type)
            workplace.delete(0, tkinter.END)
            workplace.insert(0, str(logginplayer.workplace.id) + " nolu " + logginplayer.workplace.type)

    #EMLAK İŞLEMLERİ
    ###############################################################
    ###############################################################

    frame22 = tkinter.Frame(frame2, width=555, height=260, bg="white",highlightbackground="black", highlightthickness=1)
    frame22.pack()
    frame22.place(x = 10, y = 135 )

    generateLabel(frame22, "EMLAK İŞLEMLERİ", "lightblue", ("helvetica 13 bold"), 0, 30)

    generateLabel(frame22, "İşlem Türü", "white", ("helvetica 12 bold"), 5, 70)
    generateLabel(frame22, "Arsa/İşlet.", "white", ("helvetica 12 bold"), 5, 100)
    generateLabel(frame22, "Alıcı/Kiracı", "white", ("helvetica 12 bold"), 5, 130)

    
    generateLabel(frame22, "Emlakçı", "white", ("helvetica 12 bold"), 5, 160)

    generateLabel(frame22, "Diğer Oyuncu", "white", ("helvetica 12 bold"), 275, 70)
    generateLabel(frame22, "İşlem Bedeli", "white", ("helvetica 12 bold"), 275, 100)
    generateLabel(frame22, "Komisyon", "white", ("helvetica 12 bold"), 275, 130)
    generateLabel(frame22, "Toplam", "white", ("helvetica 12 bold"), 275, 160)

    # KOMBOBOXLAR
    islem_combo = generateCombobox(frame22, 15, ("cambira 10"), 130, 70)
    islem_combo["value"] = ["Satış", "Satın Alma", "Kirala", "Kiraya Ver"]

    arsaIsletme_kombo = generateCombobox(frame22, 15, ("cambira 10"), 130, 100)

    alicikiraci_combo = generateCombobox(frame22, 15, ("cambira 10"), 130, 130)
    alicikiraci_combo["value"] = [str(x.id) + " - " + x.name + " " + x.surname for x in oyuncular
                                  if x.id != logginplayer.id]

    emlakci_combo = generateCombobox(frame22, 15, ("cambira 10"), 130, 160)
    emlakci_combo["value"] = [str(x.id) + " - " + x.type for x in alanlar if x.type == "EMLAK"]
    #------------------------------------------------------------------------------------------


    def islemTuruKontrol(event):
        selected = event.widget.get()

        arsaIsletme_kombo.delete(0,tkinter.END)
        emlakci_combo.delete(0,tkinter.END)

        if selected == "Satın Alma":
            arsaIsletme_kombo["value"] = [str(x.id) + " - " + x.type for x in alanlar if x.owner.id != logginplayer.id]
            alicikiraci_combo["state"] = "disabled"

        elif selected == "Kirala":
            arsaIsletme_kombo["value"] = [str(x.id) + " - " + x.type for x in alanlar if x.owner.id != logginplayer.id and x.type !="ARSA"]
            alicikiraci_combo["state"] = "disabled"

        elif selected == "Satış":
            arsaIsletme_kombo["value"] = [str(x.id) + " - " + x.type for x in alanlar if x.owner.id == logginplayer.id] 
            alicikiraci_combo["state"] = "active"

        elif selected == "Kiraya Ver":
            arsaIsletme_kombo["value"] = [str(x.id) + " - " + x.type for x in alanlar if x.owner.id == logginplayer.id and x.type !="ARSA"] 
            alicikiraci_combo["state"] = "active"

        else:
            arsaIsletme_kombo["value"] = []

    islem_combo.bind('<<ComboboxSelected>>', islemTuruKontrol)

    #ENTRYLER
    digerOyuncu= generateEntry(frame22, 14, 390, 70 )
    digerOyuncu.config(bg="grey")

    islembedeli= generateEntry(frame22, 12, 390, 100 )
    islembedeli.config(bg="grey")

    komisyon= generateEntry(frame22, 12, 390, 130 )
    komisyon.config(bg="grey")

    toplam = generateEntry(frame22, 12, 390, 160 )
    toplam.config(bg="grey")
    #------------------------------------------------------------------------------------------

    kontrolet_buton = generateButton(frame22, "Kontrol Et","white","black", 8, ("helvetica 8 bold"), 130,190)
    kontrolet_buton.configure(command = lambda: [kontrol_et()])

    onayla_buton = generateButton(frame22, "İşlemi Onayla","white","black", 10, ("helvetica 8 bold"), 390,190 )
    onayla_buton.configure(command = lambda: [onayla()])

    def kontrol_et():

        digerOyuncu.delete(0, tkinter.END)
        islembedeli.delete(0, tkinter.END)
        komisyon.delete(0, tkinter.END)
        toplam.delete(0, tkinter.END)

        islemturu = islem_combo.get()
        arsa_isletme = arsaIsletme_kombo.get()
        emlakci = emlakci_combo.get()

        yer = [x for x in alanlar if x.id == int(arsa_isletme[0: arsa_isletme.index(" ")])][0]
        emlak = [x for x in alanlar if x.id == int(emlakci[0: emlakci.index(" ")])][0]

        isim = str(yer.owner.name) + " " + str(yer.owner.surname)      
        digerOyuncu.insert(0, isim)

        if islemturu == "Satış" or islemturu == "Satın Alma":

            satisbedeli = str(yer.value)
            satiskomisyonBedeli = str(emlak.sold_commission)
            
            islembedeli.insert(0, satisbedeli)
            komisyon.insert(0, satiskomisyonBedeli)
            toplam.insert(0, str(round(float(satisbedeli) + float(satiskomisyonBedeli), 2)))

            if islemturu == "Satış":
                digerOyuncu.delete(0, tkinter.END)
                digerOyuncu.insert(0, alicikiraci_combo.get())
        
        elif islemturu == "Kirala" or islemturu == "Kiraya Ver":

            kiraBedeli = str(yer.rent)
            kirakomisyonbedeli = str(emlak.rent_commission)
            islembedeli.insert(0, kiraBedeli)
            komisyon.insert(0, kirakomisyonbedeli)
            toplam.insert(0, str(round(float(kiraBedeli) + float(kirakomisyonbedeli),2)))

            if islemturu == "Kiraya Ver":
                digerOyuncu.delete(0, tkinter.END)
                digerOyuncu.insert(0, alicikiraci_combo.get())

    def onayla():

        islemturu = islem_combo.get()
        arsa_isletme = arsaIsletme_kombo.get()
        emlakci = emlakci_combo.get()

        yer = [x for x in alanlar if x.id == int(arsa_isletme[0: arsa_isletme.index(" ")])][0]
        emlak = [x for x in alanlar if x.id == int(emlakci[0: emlakci.index(" ")])][0]
        digeroyuncu = yer.owner

        toplammaliyet = round(float(toplam.get()),2)
        oyuncuparamiktari = round(float(money.get()),2)

        if islemturu == "Satın Alma":

            if yer.type == "ARSA" and logginplayer != administer:  # 2'den fazla arsanın kontrol edilmesi
                mevcutArsaSayisi = len([x for x in alanlar if x.type == "ARSA" and x.owner == logginplayer])
                if mevcutArsaSayisi ==2:
                    messagebox.showinfo("showinfo", "2'den Fazla Arsa Satın alamazsınız")
                    digerOyuncu.delete(0, tkinter.END)
                    islembedeli.delete(0, tkinter.END)
                    komisyon.delete(0, tkinter.END)
                    toplam.delete(0, tkinter.END)
                    return

            if toplammaliyet > oyuncuparamiktari:
                messagebox.showinfo("showinfo", "PARANIZ YETERSİZ")
                digerOyuncu.delete(0, tkinter.END)
                islembedeli.delete(0, tkinter.END)
                komisyon.delete(0, tkinter.END)
                toplam.delete(0, tkinter.END)
                return
 
            else:
                satisbedeli = yer.value
                satiskomisyonBedeli = emlak.sold_commission
                logginplayer.money -= round(toplammaliyet,2)
                digeroyuncu.money -= round(satiskomisyonBedeli)
                
                money.delete(0, tkinter.END)
                money.insert(0, str(round(oyuncuparamiktari -toplammaliyet,2) ))
                
                if emlak.rented == True:
                    emlak.renter.money += 2*satiskomisyonBedeli
                    UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {emlak.renter.money} WHERE Playerid = {emlak.renter.id}")
                else:
                    emlak.owner.money += 2*satiskomisyonBedeli
                    UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {emlak.owner.money} WHERE Playerid = {emlak.owner.id}")

                yer.owner.money +=satisbedeli
                yer.owner = logginplayer


                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {logginplayer.money} WHERE Playerid = {logginplayer.id}")
                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {digeroyuncu.money} WHERE Playerid = {digeroyuncu.id}")

                UpdateDataBase(f"UPDATE {AlanlarTablosu} SET  Ownerid = {logginplayer.id} WHERE Areaid = {yer.id}")

                
                sahibolunanalan["value"] = [str(x.id) + " - " + x.type for x in alanlar if x.owner.id == logginplayer.id ]
                mevcutArsalar["values"] = [str(x.id) + " - " + x.type for x in alanlar if x.type == "ARSA" and x.owner.id == logginplayer.id]
                CYDegistir["values"] = [str(x.id) + " " + x.type for x in alanlar if logginplayer.workplace != x and x.renter != logginplayer and  x.owner !=logginplayer and x.type != "ARSA"]
                generateButtons(int(alany.get()),int(alanx.get()), players)
                YoneticiBilgiGuncelle(administer, regions, yoneticiParaMiktari, yoneticiEsyaMiktari, yoneticiYemekMiktari, yoneticiAlanlarSahib, yoneticiAlanlarKira)

                digerOyuncu.delete(0, tkinter.END)
                islembedeli.delete(0, tkinter.END)
                komisyon.delete(0, tkinter.END)
                toplam.delete(0, tkinter.END)

                islem_combo.delete(0, tkinter.END)
                alicikiraci_combo.delete(0, tkinter.END)
                arsaIsletme_kombo.delete(0, tkinter.END)
                emlakci_combo.delete(0, tkinter.END)
                
        elif islemturu == "Kirala":
           
            if toplammaliyet > oyuncuparamiktari:
                messagebox.showinfo("showinfo", "PARANIZ YETERSİZ")
                digerOyuncu.delete(0, tkinter.END)
                islembedeli.delete(0, tkinter.END)
                komisyon.delete(0, tkinter.END)
                toplam.delete(0, tkinter.END)
                return
  
            else:
                kirabedeli = yer.rent
                kirakomisyonBedeli = emlak.rent_commission
                yer.rented = True
                yer.renter = logginplayer
                logginplayer.money -= round(toplammaliyet,2)
                digeroyuncu.money -= round(kirakomisyonBedeli, 2)
                money.delete(0, tkinter.END)
                money.insert(0, str(oyuncuparamiktari -toplammaliyet))

                if emlak.rented == True:
                    emlak.renter.money += 2*kirakomisyonBedeli
                    UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {emlak.renter.money} WHERE Playerid = {emlak.renter.id}")
                else:
                    emlak.owner.money += 2*kirakomisyonBedeli
                    UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {emlak.owner.money} WHERE Playerid = {emlak.owner.id}")

                yer.owner.money += kirabedeli

                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {logginplayer.money} WHERE Playerid = {logginplayer.id}")
                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {digeroyuncu.money} WHERE Playerid = {digeroyuncu.id}")
                UpdateDataBase(f"UPDATE {AlanlarTablosu} SET  Renterid = {logginplayer.id} WHERE Areaid = {yer.id}")

                generateButtons(int(alany.get()), int(alanx.get()), players)
                kiraciyım["value"] = [str(x.id) + " - " + x.type for x in alanlar if x.type !="ARSA" and type(x.renter) !=str and  x.renter.id == logginplayer.id]
                CYDegistir["values"] = [str(x.id) + " " + x.type for x in alanlar if logginplayer.workplace != x and x.renter != logginplayer and  x.owner !=logginplayer and x.type != "ARSA"]
                YoneticiBilgiGuncelle(administer, regions, yoneticiParaMiktari, yoneticiEsyaMiktari,
                           yoneticiYemekMiktari, yoneticiAlanlarSahib, yoneticiAlanlarKira)
                
                digerOyuncu.delete(0, tkinter.END)
                islembedeli.delete(0, tkinter.END)
                komisyon.delete(0, tkinter.END)
                toplam.delete(0, tkinter.END)

                islem_combo.delete(0, tkinter.END)
                alicikiraci_combo.delete(0, tkinter.END)
                arsaIsletme_kombo.delete(0, tkinter.END)
                emlakci_combo.delete(0, tkinter.END)

        elif islemturu == "Satış":

            digerOyunucu_isim = alicikiraci_combo.get()
            digerOyuncuid = digerOyunucu_isim[0: digerOyunucu_isim.index(" ")]
            other_player = [x for x in oyuncular if str(x.id) == digerOyuncuid ][0]

            if yer.type == "ARSA" and other_player != administer:  # 2'den fazla arsanın kontrol edilmesi
                mevcutArsaSayisi = len([x for x in alanlar if x.type == "ARSA" and x.owner == logginplayer])
                if mevcutArsaSayisi == 2:
                    messagebox.showinfo("showinfo", "2'den Fazla Arsa Satın Alınamaz")
                    digerOyuncu.delete(0, tkinter.END)
                    islembedeli.delete(0, tkinter.END)
                    komisyon.delete(0, tkinter.END)
                    toplam.delete(0, tkinter.END)
                    return

            if toplammaliyet > other_player.money:
                messagebox.showinfo("showinfo", "DİĞER OYUNCNUN PARASI YETERSİZ")
                digerOyuncu.delete(0, tkinter.END)
                islembedeli.delete(0, tkinter.END)
                komisyon.delete(0, tkinter.END)
                toplam.delete(0, tkinter.END)
                return

            else:

                satisbedeli = yer.value
                satiskomisyonBedeli = emlak.sold_commission
                other_player.money -= round(toplammaliyet,2)
                logginplayer.money -= round(satiskomisyonBedeli, 2)
                money.delete(0, tkinter.END)
                money.insert(0, str(round(oyuncuparamiktari + satisbedeli,2)))
                
                if emlak.rented == True:
                    emlak.renter.money += 2*satiskomisyonBedeli
                    UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {emlak.renter.money} WHERE Playerid = {emlak.renter.id}")
                else:
                    emlak.owner.money += 2*satiskomisyonBedeli
                    UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {emlak.owner.money} WHERE Playerid = {emlak.owner.id}")

                yer.owner.money +=satisbedeli
                yer.owner = other_player

                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {logginplayer.money} WHERE Playerid = {logginplayer.id}")
                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {other_player.money} WHERE Playerid = {other_player.id}")
                UpdateDataBase(f"UPDATE {AlanlarTablosu} SET  Ownerid = {other_player.id} WHERE Areaid = {yer.id}")


                generateButtons(int(alany.get()),int(alanx.get()), players)
                sahibolunanalan["value"] = [str(x.id) + " - " + x.type for x in alanlar if x.owner.id == logginplayer.id ]
                mevcutArsalar["values"] = [str(x.id) + " - " + x.type for x in alanlar if x.type == "ARSA" and x.owner.id == logginplayer.id]
                CYDegistir["values"] = [str(x.id) + " " + x.type for x in alanlar if logginplayer.workplace != x and x.renter != logginplayer and  x.owner !=logginplayer and x.type != "ARSA"]
                YoneticiBilgiGuncelle(administer, regions, yoneticiParaMiktari, yoneticiEsyaMiktari,
                           yoneticiYemekMiktari, yoneticiAlanlarSahib, yoneticiAlanlarKira)

                digerOyuncu.delete(0, tkinter.END)
                islembedeli.delete(0, tkinter.END)
                komisyon.delete(0, tkinter.END)
                toplam.delete(0, tkinter.END)

                islem_combo.delete(0, tkinter.END)
                alicikiraci_combo.delete(0, tkinter.END)
                arsaIsletme_kombo.delete(0, tkinter.END)
                emlakci_combo.delete(0, tkinter.END)

        elif islemturu == "Kiraya Ver":
            
            digerOyunucu_isim = alicikiraci_combo.get()
            digerOyuncuid = digerOyunucu_isim[0: digerOyunucu_isim.index(" ")]
            other_player = [x for x in oyuncular if str(x.id) == digerOyuncuid ][0]

            if toplammaliyet > other_player.money:

                messagebox.showinfo("showinfo", "DİĞER OYUNCNUN PARASI YETERSİZ")
                digerOyuncu.delete(0, tkinter.END)
                islembedeli.delete(0, tkinter.END)
                komisyon.delete(0, tkinter.END)
                toplam.delete(0, tkinter.END)
                return
            else:

                kiraBedeli = yer.rent
                kirakomisyonbedeli = emlak.rent_commission

                yer.rented = True
                yer.renter = other_player

                other_player.money -= round(kiraBedeli,2)

                logginplayer.money += round(kiraBedeli,2)
                logginplayer.money -= round(kirakomisyonbedeli,2)


                if emlak.rented == True:
                    emlak.renter.money += 2*kirakomisyonbedeli
                    UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {emlak.renter.money} WHERE Playerid = {emlak.renter.id}")
                else:
                    emlak.owner.money += 2*kirakomisyonbedeli
                    UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {emlak.owner.money} WHERE Playerid = {emlak.owner.id}")

                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {logginplayer.money} WHERE Playerid = {logginplayer.id}")
                UpdateDataBase(f"UPDATE {OyuncularTablosu} SET Money = {other_player.money} WHERE Playerid = {other_player.id}")
                UpdateDataBase(f"UPDATE {AlanlarTablosu} SET  Renterid = {other_player.id} WHERE Areaid = {yer.id}")
              

                money.delete(0, tkinter.END)
                money.insert(0, str(oyuncuparamiktari + kiraBedeli))

                generateButtons(int(alany.get()), int(alanx.get()), players)
                kiradaki["value"] = [str(x.id) + " - " + x.type for x in alanlar if x.owner.id == logginplayer.id and x.rented == True]
                CYDegistir["values"] = [str(x.id) + " " + x.type for x in alanlar if logginplayer.workplace != x and x.renter != logginplayer and  x.owner !=logginplayer and x.type != "ARSA"]

                YoneticiBilgiGuncelle(administer, regions, yoneticiParaMiktari, yoneticiEsyaMiktari,
                           yoneticiYemekMiktari, yoneticiAlanlarSahib, yoneticiAlanlarKira)
                
                digerOyuncu.delete(0, tkinter.END)
                islembedeli.delete(0, tkinter.END)
                komisyon.delete(0, tkinter.END)
                toplam.delete(0, tkinter.END)

                islem_combo.delete(0, tkinter.END)
                alicikiraci_combo.delete(0, tkinter.END)
                arsaIsletme_kombo.delete(0, tkinter.END)
                emlakci_combo.delete(0, tkinter.END)

        else:
            pass

    root.mainloop()

def GenerateDataBase(Regions, Players):

    global Marketid, Magazaid, Emlakid

    DropTables()
    GenerateTables()

    AreaTypes = {"ARSA": 1,
                 "MARKET": 2,
                 "MAĞAZA": 3,
                 "EMLAK": 4}
    
    Roles = {"Yönetici":1,
             "Oyuncu": 2}
    

    for player in Players:
        values = [player.id, Roles[player.role], player.name, player.surname, player.username, player.password, player.workplace.id, player.money, player.eatings, player.goods ]
        insertinfo("players_table", values)

    for r in Regions:

        values = [r.id, AreaTypes[r.type], r.owner.id, r.value, r.rented, r.renter.id]
        insertinfo("areas_table", values)

        if r.type == "MARKET":
            values = [Marketid, r.capacity, r.worker_number, r.grade, r.rent, r.fixIncome, r.food_fee, r.wage, r.id]
            insertinfo("markets_table", values)
            Marketid = Marketid + 1
        
        if r.type == "MAĞAZA":
            values = [Magazaid, r.capacity, r.worker_number, r.grade, r.rent, r.fixIncome, r.good_fee, r.wage, r.id]
            insertinfo("shoppingcenters_table", values)
            Magazaid = Magazaid + 1
        
        if r.type == "EMLAK":
            values = [Emlakid, r.capacity, r.worker_number, r.grade, r.rent, r.fixIncome, r.rent_commission, r.sold_commission, r.wage, r.id]
            insertinfo("realestates_tables", values)
            Emlakid = Emlakid + 1
#---------------------------------------------------------------------------------------------------

root.mainloop()