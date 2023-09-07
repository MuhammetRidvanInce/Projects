import numpy as np
import tkinter
import random 
import datetime



class OrtakFonksiyonlar():

    def RobotYuzuDon(self, robot, ilk_koordinat, ikinci_koordinat):
        x1 = ilk_koordinat[0]
        y1 = ilk_koordinat[1]

        x2 = ikinci_koordinat[0]
        y2 = ikinci_koordinat[1]

        if x2>x1:
            robot.setheading(0)
        elif x2<x1:
            robot.setheading(180)
        elif y2>y1:
            robot.setheading(90)
        elif y2<y1:
            robot.setheading(270)

    def AStar(self, robot, robot_baslangic_koordinat,wall_size, wall_coordinates, hedef_koordinat):

        self.RobotBaslangicaDon(robot, robot_baslangic_koordinat)

        visited = [(robot.xcor(), robot.ycor())]
        stack = [(robot.xcor(), robot.ycor())]

        while True:

            uygun_komsular = [komsu for komsu in self.TumKomsular(robot, wall_size, wall_coordinates)
                               if komsu not in visited and komsu not in wall_coordinates and komsu in self.ogrenilen]

            if uygun_komsular:
                if len(uygun_komsular) == 1:
                    robot.goto(uygun_komsular[0][0],uygun_komsular[0][1])
                    visited.append((robot.xcor(), robot.ycor()))
                    stack.append((robot.xcor(), robot.ycor()))
                    if self.CevreKontrol(robot, wall_size,wall_coordinates, hedef_koordinat, stack):
                        break

                else:
                    heuristic = np.inf
                    sonraki   = None
                    for komsu in uygun_komsular:
                        x_cor = komsu[0]
                        y_cor = komsu[1]
                        new_heuristic = np.sqrt((hedef_koordinat[0] - x_cor)**2 + (hedef_koordinat[1] - y_cor)**2 ) 
                        if new_heuristic < heuristic:
                            heuristic = new_heuristic
                            sonraki= (x_cor, y_cor)
                    
                    robot.goto(sonraki[0], sonraki[1])
                    visited.append((robot.xcor(), robot.ycor()))
                    stack.append((robot.xcor(), robot.ycor()))
                    if self.CevreKontrol(robot, wall_size,wall_coordinates, hedef_koordinat, stack):
                        break

            else:
                robot.color("indigo")
                robot.width(wall_size/3)
                robot.goto(stack[-1][0], stack[-1][1])
                UygunKomsular = [komsu for komsu in self.TumKomsular(robot, wall_size, wall_coordinates)
                                    if komsu not in visited and komsu in self.ogrenilen]
                if not UygunKomsular:
                    stack.pop()

        return stack
    
    def EnKisaYol(self, robot, robot_baslangic_koordinat, wall_size,wall_coordinates, hedef_koordinat):

        stack = self.AStar(robot, robot_baslangic_koordinat, wall_size, wall_coordinates, hedef_koordinat)
        if not stack:
            return
        
        self.RobotBaslangicaDon(robot, robot_baslangic_koordinat)
        
        enkisayol = []   
        while True:
            uygun_komsular = [komsu for komsu in self.TumKomsular(robot, wall_size, wall_coordinates)
                               if komsu in stack]
            
            if len(uygun_komsular) == 1:
                robot.goto(uygun_komsular[0][0], uygun_komsular[0][1])
                enkisayol.append((robot.xcor(), robot.ycor()))
                if (hedef_koordinat == (robot.xcor(), robot.ycor())):
                    break
            else:
                sonraki = uygun_komsular[0]
                max_index = stack.index(uygun_komsular[0])
                for i in uygun_komsular[1:]:
                    index = stack.index(i)
                    if index > max_index:
                        max_index = index
                        sonraki = i
                
                robot.goto(sonraki[0], sonraki[1])
                enkisayol.append((robot.xcor(), robot.ycor()))
                if (hedef_koordinat == (robot.xcor(), robot.ycor())):
                    break
        
        self.RobotBaslangicaDon(robot, robot_baslangic_koordinat)

        robot.showturtle()
        robot.down()
        robot.color("darkblue")
        robot.width(wall_size/1.5)
        for koordinat in enkisayol:
            robot.goto(koordinat[0], koordinat[1])

        return enkisayol

    def RobotBaslangicaDon(self, robot, robot_baslangic_koordinat):
        robot.ht()
        robot.up()
        robot.goto(robot_baslangic_koordinat[0], robot_baslangic_koordinat[1])

    def DuvarYerlestir(self, all_coordinates, wall_coordinates, fridge_coordinate, road_coordinate, start_coordinate,aim_coordinate, duvar, problem):
        
        for koordinat in all_coordinates:

            if koordinat == start_coordinate:
                duvar.color("green")
            elif koordinat == aim_coordinate:
                duvar.color("purple")
            elif koordinat in fridge_coordinate:
                duvar.color("brown")
            elif koordinat in wall_coordinates and problem == 1:
                duvar.color("aqua")
            elif koordinat in wall_coordinates and problem == 2:
                duvar.color("brown")
            elif koordinat in road_coordinate:
                 duvar.color("white")
                
            duvar.goto(koordinat[0], koordinat[1])
            duvar.stamp()

    def TumKomsular(self, robot, wall_size, wall_coordinates):
        robot_koordinat = (robot.xcor(), robot.ycor())
        komsular = []
        komsu_kordinat = [(0.0, wall_size), (0.0, -1*wall_size), (wall_size, 0.0),  (-1*wall_size, 0.0)]
        for dx,dy in komsu_kordinat:
            x, y = robot_koordinat[0] + dx, robot_koordinat[1] + dy
            if (x,y) not in wall_coordinates:
                komsular.append((x,y))  
        return komsular

    def GeriDon(self, robot, geri_donulen, wall_size, wall_coordinates, ziyaret_edilen, fridge_coordinates):
        robot.color("indigo")
        robot.width(wall_size/3)
        robot.goto(geri_donulen[-1][0], geri_donulen[-1][1])
        UygunKomsular = [komsu for komsu in self.TumKomsular(robot, wall_size, wall_coordinates)
                               if komsu not in ziyaret_edilen and komsu not in fridge_coordinates]
        if not UygunKomsular:
            geri_donulen.pop() 

    def CevreKontrol(self, robot, wall_size,wall_coordinates, hedef, geri_donulen):
        komsular = self.TumKomsular(robot, wall_size, wall_coordinates)
        for komsu in komsular:
            if (komsu[0], komsu[1]) == hedef:
                robot.goto(komsu[0], komsu[1])
                geri_donulen.append((robot.xcor(), robot.ycor()))
                return True
        return False

    def RobotHizArtir(self, robot):
        robot.speed(0)
    
    def RobotHizAzalt(self, robot):
        robot.speed(1)

    def BilgileriAl(self,SonucTextArea, satir, sütun, robot_baslangic, hedef_baslangic, counter, enkisayol, time):

        SonucTextArea.delete("1.0",tkinter.END)

        baslik1 = "LABIRENT BILGILERI\n----------------\n"
        satir_bilgisi  = "Satir Sayisi: {}\n".format(satir)
        sutun_bilgisi  = "Sutun Sayisi: {}\n".format(sütun)
        robot_konum = "Robot Konum: {}\n".format(robot_baslangic)
        hedef_konum = "Hedef Konum: {}\n\n".format(hedef_baslangic)
        baslik2 = "COZUM BILGILERI\n----------------\n"
        adim_sayisi = "Cozum Adim Sayisi: {}\n".format(counter)
        sure = "Gecen Sure: {} Sn\n".format(time)
        path = "En Kisa Yol Adim Sayisi: {}\n".format(len(enkisayol)) 
       
        order = 1
        en_kisa_yol_koordinatlar = ""
        for i in enkisayol:
            en_kisa_yol_koordinatlar += str(order) + " - " +   str(i) + "\n"
            order +=1

        path_coordinates = "En Kisa Yol Koordinatlar:\n{}".format(en_kisa_yol_koordinatlar) 

        result = baslik1 + satir_bilgisi + sutun_bilgisi + robot_konum + hedef_konum + baslik2 + adim_sayisi + sure + path + path_coordinates
        SonucTextArea.insert(tkinter.END, result)
        return result