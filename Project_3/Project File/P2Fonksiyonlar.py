import random
import numpy as np
import datetime
from OrtakFonksiyonlar import OrtakFonksiyonlar



  
class Dugum:
    def __init__(self, value = None, next_element = None):
        self.value = value
        self.next_element = next_element
  
class Yigin:

    def __init__(self):
        self.head = None
        self.length = 0
  
    def ekle(self, data):
        self.head = Dugum(data, self.head)
        self.length += 1
  
    def cikar(self):
        if self.length != 0:
            return_value = self.head.value
            self.head = self.head.next_element
            self.length -= 1
            return return_value
        else:
            return None

class P2Fonksiyonlar(OrtakFonksiyonlar):
    
    def __init__(self):
        OrtakFonksiyonlar().__init__()


    def RastgeleLabirentOlustur(self, satir_sayisi, sutun_sayisi, baslangic_koordinat, bitis_koordinat):

        labirent_listesi = [ [1 for _ in range(sutun_sayisi) ] for _ in range(satir_sayisi) ]
        ziyaret_edilen = [ [False for _ in range(sutun_sayisi)] for _ in range(satir_sayisi)]
        onceki_koordinat = [ [(-1, -1) for _ in range(sutun_sayisi)] for _ in range(satir_sayisi) ]

        S = Yigin()
        S.ekle(baslangic_koordinat) 

        while S.length:
            x, y = S.cikar()
            ziyaret_edilen[x][y] = True

            if (x + 1 < satir_sayisi) and labirent_listesi[x + 1][y] == 0 and onceki_koordinat[x][y] != (x + 1,  y):
                continue
            if (0 < x) and labirent_listesi[x-1][y] == 0 and onceki_koordinat[x][y] != (x-1,  y):
                continue
            if (y + 1 < sutun_sayisi) and labirent_listesi[x][y + 1] == 0 and onceki_koordinat[x][y] != (x, y + 1):
                continue
            if (y > 0) and labirent_listesi[x][y-1] == 0 and onceki_koordinat[x][y] != (x, y-1):
                continue

            labirent_listesi[x][y] = 0
            yigin_listesi = []

            if (x + 1 < satir_sayisi) and ziyaret_edilen[x + 1][y] == False:
                
                ziyaret_edilen[x + 1][y] = True
                yigin_listesi.append((x + 1,  y))
                onceki_koordinat[x + 1][y] = (x, y)
            
            if (0 < x) and ziyaret_edilen[x-1][y] == False:
                
                ziyaret_edilen[x-1][y] = True
                yigin_listesi.append((x-1,  y))
                onceki_koordinat[x-1][y] = (x, y)
            
            if (y + 1 < sutun_sayisi) and ziyaret_edilen[x][y + 1] == False:
                
                ziyaret_edilen[x][y + 1] = True
                yigin_listesi.append((x, y + 1))
                onceki_koordinat[x][y + 1] = (x, y)
            
            if (y > 0) and ziyaret_edilen[x][y-1] == False:
                
                ziyaret_edilen[x][y-1] = True
                yigin_listesi.append((x, y-1))
                onceki_koordinat[x][y-1] = (x, y)
            
            bitis_koordinat_flag = False
            while len(yigin_listesi):
                neighbour = yigin_listesi.pop(random.randint(0, len(yigin_listesi)-1))
                if neighbour == bitis_koordinat:
                    bitis_koordinat_flag = True
                else:
                    S.ekle(neighbour)

            if bitis_koordinat_flag:
                S.ekle(bitis_koordinat)
                    
        labirent_listesi[baslangic_koordinat[0]][baslangic_koordinat[1]] = "S"
        labirent_listesi[bitis_koordinat[0]][bitis_koordinat[1]]         = "F"

        labirent = []
        for row in labirent_listesi:
            line = ""
            for value in row:
                line +=str(value)
            labirent.append("5" + line + "5")
        
        labirent.insert(0, "5"*len(labirent[0]))
        labirent.append("5"*len(labirent[0]))

        if (labirent[len(labirent) - 3][len(labirent[0])-2] == "1" and
             labirent[len(labirent) - 2][len(labirent[0])-3] == "1"):
            labirent[len(labirent) - 3][len(labirent[0])-2] = "0"
            


           
        return labirent
    
    def LabirentDolas2(self, robot, robot_baslangic_koordinat, wall_size, wall_coordinates,
                       fridge_coordinates, hedef_koordinat, canvas ):

        
        
        robot.showturtle()
        start_time = datetime.datetime.now()
        adim_sayisi = 0
        
        geri_donulen = [robot_baslangic_koordinat]
        ziyaret_edilen = [robot_baslangic_koordinat]
        self.ogrenilen = [robot_baslangic_koordinat]
        robot.down()

        while True:
            robot.color("green")
            robot.width(wall_size/2)
            
            uygun_komsular = [komsu for komsu in self.TumKomsular(robot, wall_size, wall_coordinates)
                               if komsu not in ziyaret_edilen and komsu not in wall_coordinates
                                 and komsu not in fridge_coordinates]
            
            if uygun_komsular:
            
                sonraki_koordinat = random.choice(uygun_komsular)
                self.RobotYuzuDon(robot, (robot.xcor(), robot.ycor()), sonraki_koordinat)

                robot.goto(sonraki_koordinat[0], sonraki_koordinat[1])

                adim_sayisi +=1
                ziyaret_edilen.append((sonraki_koordinat[0], sonraki_koordinat[1]))
                geri_donulen.append((sonraki_koordinat[0], sonraki_koordinat[1]))
                self.ogrenilen.append((sonraki_koordinat[0], sonraki_koordinat[1]))
                komsular = self.TumKomsular(robot, wall_size, wall_coordinates)
                for komsu in komsular:
                    if komsu not in self.ogrenilen:
                        self.ogrenilen.append(komsu)

                if self.CevreKontrol(robot, wall_size,wall_coordinates, hedef_koordinat, geri_donulen):
                    break
            
            else:
                if (len(geri_donulen) == 0):
                    canvas.create_text(0,0, text="HEDEF BULUNAMAMAKTADIR",
                                        fill="red",font=('Helvetica 15 bold') )
                    break
                self.GeriDon(robot, geri_donulen, wall_size,wall_coordinates,ziyaret_edilen, fridge_coordinates)

        end_time = datetime.datetime.now()
        gecen_sure = (end_time - start_time).total_seconds()

        return (adim_sayisi,gecen_sure)

    
   