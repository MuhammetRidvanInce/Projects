import numpy as np
import random 
import datetime
from OrtakFonksiyonlar import OrtakFonksiyonlar



class P1Fonksiyonlar(OrtakFonksiyonlar):

    def __init__(self):
        OrtakFonksiyonlar().__init__()

    def LabirentDolas(self, canvas, robot, robot_baslangic_koordinat, 
                      hedef_koordinat, duman, wall_size, wall_coordinates,
                      fridge_coordinates, stamp_koordinat, stamp_id):

        
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
                self.DumanTemizle(robot.xcor(), robot.ycor(), duman, wall_size, stamp_id, stamp_koordinat)
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
                    duman.clearstamps()
                    break
                self.GeriDon(robot, geri_donulen, wall_size,wall_coordinates,ziyaret_edilen, fridge_coordinates)
        
        end_time = datetime.datetime.now()
        gecen_sure = (end_time - start_time).total_seconds()

        return (adim_sayisi,gecen_sure)
   
    def RobotHedefYerlestir(self, robot, hedef, road_coordinates ):
        robot_baslangic_koordinat = random.choice(road_coordinates)
        hedef_baslangic_koordinat = random.choice(road_coordinates)

        while robot_baslangic_koordinat == hedef_baslangic_koordinat:
            robot_baslangic_koordinat = random.choice(road_coordinates)
            hedef_baslangic_koordinat = random.choice(road_coordinates)

        self.robot.goto(robot_baslangic_koordinat[0], robot_baslangic_koordinat[1])
        robot.showturtle()
        robot.stamp()       
        hedef.goto(hedef_baslangic_koordinat[0], hedef_baslangic_koordinat[1])
        hedef.showturtle()
        hedef.stamp()

        return (robot_baslangic_koordinat, hedef_baslangic_koordinat)

    def Dumanla(self, stamp_koordinat, stamp_id, duman, wall_size_pixel, all_coordinates):
        duman.shapesize(*((wall_size_pixel/20, wall_size_pixel/20, wall_size_pixel/20)))
        for koordinat in all_coordinates:
            duman.goto(koordinat[0], koordinat[1])
            stamp = duman.stamp()
            stamp_koordinat.append((koordinat[0], koordinat[1]))
            stamp_id.append(stamp)

    def DumanTemizle(self, x, y, duman, wall_size, stamp_id,stamp_koordinat ):
        duman_temizle_koordinat = [(0.0,0.0), (0.0, wall_size), (wall_size, 0.0), (0.0, -1*wall_size), (-1*wall_size, 0.0)]
        for koordinat in duman_temizle_koordinat:
            if ((x + koordinat[0], y + koordinat[1]) in stamp_koordinat):
                duman.clearstamp(stamp_id[stamp_koordinat.index((x + koordinat[0], y + koordinat[1]))])

#---------------------------------------------------------------------------------------------------------------------------
    def EngelSec(self, engel_tipi, engel_listesi):
            engeller = []
            if engel_tipi == "1":
                engeller = [i for i in list(engel_listesi.keys()) if engel_listesi[i][0].prod() == 1 and engel_listesi[i][1] == 1]
            elif engel_tipi == "2":
                engeller = [i for i in list(engel_listesi.keys()) if (engel_listesi[i][0].prod() == 2 and engel_listesi[i][1] == 1)
                                                                    or (engel_listesi[i][0].prod() == 4 and engel_listesi[i][1] == 1)
                                                                    ]
            elif engel_tipi=="3":
                engeller = [i for i in list(engel_listesi.keys()) if (engel_listesi[i][0].prod() == 3 and engel_listesi[i][1] == 1)
                                                                    or (engel_listesi[i][0].prod() == 6 and engel_listesi[i][1] == 1)
                                                                    or (engel_listesi[i][0].prod() == 9 and engel_listesi[i][1] == 1)
                                                                    ]  
            engel = random.choice(engeller)
            return engel # engelin resminin dosya yoluz
        
    def DuvarKonumGuncelle(self, koordinat_listesi, wall_coordinates ):
        for koordinat in koordinat_listesi:
            if koordinat in wall_coordinates:
                wall_coordinates.remove(koordinat)

    def EngelleriYerlestir(self, engel_yerlestirici, engel_listesi,
                            screen, obstacles_coordinates, fridge_wall_coordinates,wall_size_pixel, wall_coordinates):

        engel_yerlestirici.clear()
        yerlestirilen_koordinatlar = []

        for engel in engel_listesi.keys():
            screen.register_shape(engel)

        for koordinat in obstacles_coordinates:
            x = koordinat[0][0]
            y = koordinat[0][1]

            if koordinat[1] == "0":
                continue

            elif koordinat[1] == "1" and (x, y) not in fridge_wall_coordinates :
                engel = self.EngelSec("1", engel_listesi)
                engel_yerlestirici.shape(engel)
                engel_yerlestirici.goto(x, y)
                engel_yerlestirici.stamp()
                yerlestirilen_koordinatlar.append((x, y))

            elif koordinat[1] == "2" and (x, y) not in yerlestirilen_koordinatlar:
                engel = self.EngelSec("2", engel_listesi)
                engel_index = list(engel_listesi.keys()).index(engel)
                engel_boyut = engel_listesi[engel][0]

                if engel_boyut.prod() ==2 and engel_boyut[0] == 1: # Boyut = 1x2
                    engel_yerlestirici.shape(engel)
                    engel_yerlestirici.goto(x, y)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x, y))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+1])
                    engel_yerlestirici.goto(x+ wall_size_pixel, y)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel, y))

                    yerlestirilen_koordinatlar.append((x, y - wall_size_pixel))
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel, y - wall_size_pixel))

                    # engeller yerleştirildikten sonraki arta kalan kısımlar yeşil alanları 
                    # duvar koordinatlarından çıkarma
                    self.DuvarKonumGuncelle([(x, y - wall_size_pixel),
                                                (x + wall_size_pixel, y - wall_size_pixel)], wall_coordinates)

                elif engel_boyut.prod() ==2 and engel_boyut[0] == 2:# Boyut = 2x1
                    engel_yerlestirici.shape(engel)
                    engel_yerlestirici.goto(x, y)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x, y))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+1])
                    engel_yerlestirici.goto(x, y - wall_size_pixel)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x, y - wall_size_pixel))

                    yerlestirilen_koordinatlar.append((x + wall_size_pixel, y))
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel, y - wall_size_pixel))


                    # engeller yerleştirildikten sonraki arta kalan kısımlar yeşil alanları 
                    # duvar koordinatlarından çıkarma
                    self.DuvarKonumGuncelle([(x + wall_size_pixel, y),
                                                (x + wall_size_pixel, y - wall_size_pixel)], wall_coordinates)

                elif engel_boyut.prod() == 4:  # Boyut = 2x2
                    engel_yerlestirici.shape(engel)
                    engel_yerlestirici.goto(x, y)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x, y))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+1])
                    engel_yerlestirici.goto(x + wall_size_pixel, y)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel, y))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+2])
                    engel_yerlestirici.goto(x, y - wall_size_pixel)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x, y - wall_size_pixel))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+3])
                    engel_yerlestirici.goto(x + wall_size_pixel, y - wall_size_pixel)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel, y - wall_size_pixel))


            elif koordinat[1] == "3" and (x, y) not in yerlestirilen_koordinatlar:
                engel = self.EngelSec("3", engel_listesi)
                engel_index = list(engel_listesi.keys()).index(engel)
                engel_boyut = engel_listesi[engel][0]

                if engel_boyut.prod() ==3 and engel_boyut[0] == 1: # Boyut = 1x3
                    engel_yerlestirici.shape(engel)
                    engel_yerlestirici.goto(x, y)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x, y))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+1])
                    engel_yerlestirici.goto(x+ wall_size_pixel, y)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel, y))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+2])
                    engel_yerlestirici.goto(x+ wall_size_pixel*2, y)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel*2, y))

                    yerlestirilen_koordinatlar.append((x, y - wall_size_pixel))
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel , y - wall_size_pixel))
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel*2 , y - wall_size_pixel))

                    yerlestirilen_koordinatlar.append((x, y - wall_size_pixel*2))
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel , y - wall_size_pixel*2))
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel*2 , y - wall_size_pixel*2))

                    # engeller yerleştirildikten sonraki arta kalan kısımlar yeşil alanları 
                    # duvar koordinatlarından çıkarma

                    self.DuvarKonumGuncelle([(x, y - wall_size_pixel),
                                                (x + wall_size_pixel , y - wall_size_pixel),
                                                (x + wall_size_pixel*2 , y - wall_size_pixel),
                                                (x, y - wall_size_pixel*2),
                                                (x + wall_size_pixel , y - wall_size_pixel*2),
                                                (x + wall_size_pixel*2 , y - wall_size_pixel*2)], wall_coordinates)


                if engel_boyut.prod() ==3 and engel_boyut[0] == 3: # Boyut = 3x1 
                    engel_yerlestirici.shape(engel)
                    engel_yerlestirici.goto(x, y)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x, y))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+1])
                    engel_yerlestirici.goto(x, y -  wall_size_pixel)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x, y - wall_size_pixel))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+2])
                    engel_yerlestirici.goto(x, y - wall_size_pixel*2)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x, y - wall_size_pixel*2))

                    yerlestirilen_koordinatlar.append((x + wall_size_pixel, y))
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel*2, y))
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel, y - wall_size_pixel))

                    yerlestirilen_koordinatlar.append((x + wall_size_pixel*2, y - wall_size_pixel))
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel, y - wall_size_pixel*2))
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel*2, y - wall_size_pixel*2))

                    # engeller yerleştirildikten sonraki arta kalan kısımlar yeşil alanları 
                    # duvar koordinatlarından çıkarma
                    self.DuvarKonumGuncelle([(x + wall_size_pixel, y),
                                                (x + wall_size_pixel*2, y),
                                                (x + wall_size_pixel, y - wall_size_pixel),
                                                (x + wall_size_pixel*2, y - wall_size_pixel),
                                                (x + wall_size_pixel, y - wall_size_pixel*2),
                                                (x + wall_size_pixel*2, y - wall_size_pixel*2)
                                                ], wall_coordinates)

                if engel_boyut.prod() ==6 and engel_boyut[0] == 3: # Boyut 3x2

                    engel_yerlestirici.shape(engel)
                    engel_yerlestirici.goto(x, y)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x, y))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+1])
                    engel_yerlestirici.goto(x + wall_size_pixel, y)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel, y))


                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+2])
                    engel_yerlestirici.goto(x, y - wall_size_pixel)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x, y - wall_size_pixel))


                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+3])
                    engel_yerlestirici.goto(x + wall_size_pixel, y -wall_size_pixel )
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel, y -wall_size_pixel))


                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+4])
                    engel_yerlestirici.goto(x , y -  wall_size_pixel*2)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x, y - wall_size_pixel*2))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+5])
                    engel_yerlestirici.goto(x + wall_size_pixel, y - wall_size_pixel*2)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel, y - wall_size_pixel*2))

                    yerlestirilen_koordinatlar.append((x + wall_size_pixel*2, y))
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel*2, y - wall_size_pixel))
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel*2, y - wall_size_pixel*2))

                    # engeller yerleştirildikten sonraki arta kalan kısımlar yeşil alanları 
                    # duvar koordinatlarından çıkarma
                    self.DuvarKonumGuncelle([(x + wall_size_pixel*2, y),
                                                (x + wall_size_pixel*2, y - wall_size_pixel),
                                                (x + wall_size_pixel*2, y - wall_size_pixel*2)], wall_coordinates)

                if engel_boyut.prod() ==6 and engel_boyut[0] == 2: # Boyut 2x3
                    
                    engel_yerlestirici.shape(engel)
                    engel_yerlestirici.goto(x, y)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x, y))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+1])
                    engel_yerlestirici.goto(x + wall_size_pixel, y)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel, y))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+2])
                    engel_yerlestirici.goto(x+ wall_size_pixel*2, y )
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x+ wall_size_pixel*2, y ))


                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+3])
                    engel_yerlestirici.goto(x, y -wall_size_pixel )
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x, y -wall_size_pixel ))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+4])
                    engel_yerlestirici.goto(x + wall_size_pixel , y -  wall_size_pixel)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel , y -  wall_size_pixel))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+5])
                    engel_yerlestirici.goto(x + wall_size_pixel*2, y - wall_size_pixel)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel*2, y - wall_size_pixel))

                    yerlestirilen_koordinatlar.append((x, y - wall_size_pixel*2))
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel, y - wall_size_pixel*2))
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel*2, y - wall_size_pixel*2))


                    # engeller yerleştirildikten sonraki arta kalan kısımlar yeşil alanları 
                    # duvar koordinatlarından çıkarma
                    self.DuvarKonumGuncelle([(x, y - wall_size_pixel*2),
                                                (x + wall_size_pixel, y - wall_size_pixel*2),
                                                (x + wall_size_pixel*2, y - wall_size_pixel*2)], wall_coordinates)

                if engel_boyut.prod() == 9: # Boyut 3x3
                    
                    engel_yerlestirici.shape(engel)
                    engel_yerlestirici.goto(x, y)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x, y))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+1])
                    engel_yerlestirici.goto(x + wall_size_pixel, y)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel, y))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+2])
                    engel_yerlestirici.goto(x + wall_size_pixel*2, y )
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x+ wall_size_pixel*2, y))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+3])
                    engel_yerlestirici.goto(x, y -wall_size_pixel )
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x, y -wall_size_pixel ))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+4])
                    engel_yerlestirici.goto(x + wall_size_pixel , y -  wall_size_pixel)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel , y -  wall_size_pixel))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+5])
                    engel_yerlestirici.goto(x + wall_size_pixel*2, y - wall_size_pixel)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel*2, y - wall_size_pixel))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+6])
                    engel_yerlestirici.goto(x, y - wall_size_pixel*2)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x, y - wall_size_pixel*2))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+7])
                    engel_yerlestirici.goto(x + wall_size_pixel, y - wall_size_pixel*2)
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x + wall_size_pixel, y - wall_size_pixel*2))

                    engel_yerlestirici.shape(list(engel_listesi.keys())[engel_index+8])
                    engel_yerlestirici.goto(x+ wall_size_pixel*2, y - wall_size_pixel*2 )
                    engel_yerlestirici.stamp()
                    yerlestirilen_koordinatlar.append((x+ wall_size_pixel*2, y - wall_size_pixel*2 ))


