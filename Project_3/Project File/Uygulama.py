import tkinter
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import turtle
import random

from Izgaralar import P1Izgara, P2Izgara
from Robotlar import Robot,  Engel_Yerlestirici, Hedef, Duvar, Duman
from Engeller import Engel


from P1Fonksiyonlar import P1Fonksiyonlar
from P2Fonksiyonlar import P2Fonksiyonlar

URLListesi = ["http://bilgisayar.kocaeli.edu.tr/prolab2/url1.txt",
              "http://bilgisayar.kocaeli.edu.tr/prolab2/url2.txt"]

URLkontrol = 0
IzgaraKontrol_1 = 0
IzgaraKontrol_2 = 0

class Uygulama(P1Fonksiyonlar, P2Fonksiyonlar):   
    def __init__(self):
        P1Fonksiyonlar().__init__()
        P2Fonksiyonlar().__init__()

        self.root = tkinter.Tk()
        self.root.title("Drawing GUI")
        
        self.root.geometry("970x680")
        self.root.minsize(970, 680)
        self.root.maxsize(970, 680)
        self.root.config(bg = "black")

        self.canvas = tkinter.Canvas(self.root, width = 600, height=600, highlightthickness=1, highlightbackground="white", background="darkgrey")
        self.canvas.pack()
        self.canvas.place(x = 5, y = 5 )
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("black")

        self.SonucTextArea = ScrolledText(self.root,width=29, height=15, 
                                          highlightthickness=1, highlightbackground="black", background="dimgrey")

        self.SonucTextArea.pack()
        self.SonucTextArea.place(x = 700, y = 425)

        # -------------------------------- LAYOUTS-------------------------------------------
        self.p1layout = tkinter.Frame(self.root,  width=240, height=200,  highlightthickness=1, highlightbackground="black", background="dimgrey" )
        self.p1layout.pack()
        self.p1layout.place(x = 700, y = 5)

        self.p2layout = tkinter.Frame(self.root,  width=240, height=200,highlightthickness=1, highlightbackground="black", background="dimgrey")
        self.p2layout.pack()
        self.p2layout.place(x = 700, y = 215)

        # ----------------------------- PROBLEM 1 LABEL-------------------------------------
        self.p1Label = ttk.Label(self.p1layout, text = "PROBLEM 1", font = ("arial 12 bold"), background="dimgrey")
        self.p1Label.pack()
        self.p1Label.place(x = 70, y = 15)

        # ----------------------------- PROBLEM 2 LABEL-------------------------------------
        self.p2Label = ttk.Label(self.p2layout, text = "PROBLEM 2", font = ("arial 12 bold"), background="dimgrey")
        self.p2Label.pack()
        self.p2Label.place(x = 70, y = 5)

        # -----------------------------PROBLEM 1 BUTTONS-------------------------------------

        self.p1btnURLDegistir = tkinter.Button(self.p1layout, text="URL DEĞİŞTİR", bg="black",
                                                fg="white", width=13, font = ("arial 10 bold"), command=lambda:[self.URLGetir()])
        self.p1btnURLDegistir.pack()
        self.p1btnURLDegistir.place(x = 5, y = 75)

        self.p1btnCalistir = tkinter.Button(self.p1layout, text="ÇALIŞTIR", bg="black",
                                             fg="white", width=13, font = ("arial 10 bold"),
                                              state = "disabled", command=lambda:[self.P1Calistir()])
        self.p1btnCalistir.pack()
        self.p1btnCalistir.place(x = 5, y = 105)

        self.p1btnSonucGoster = tkinter.Button(self.p1layout, text="SONUÇ GÖSTER", bg="black",
                                                fg="white", width=13, font = ("arial 10 bold"),
                                                 state = "disabled", command=lambda:[self.P1SonucGoster()])
        self.p1btnSonucGoster.pack()
        self.p1btnSonucGoster.place(x = 5, y = 135)

        self.p1btnRHartir = tkinter.Button(self.p1layout, text="Robot Hız (+)", bg="black",
                                                fg="white", width=13, font = ("calibri 10 bold"), command=lambda:[self.RobotHizArtir(self.robot)],
                                                state="disabled")
        self.p1btnRHartir.pack()
        self.p1btnRHartir.place(x = 120, y = 75)

        self.p1btnRHazalt = tkinter.Button(self.p1layout, text="Robot Hız (-)", bg="black",
                                                fg="white", width=13, font = ("calibri 10 bold"), command=lambda:[self.RobotHizAzalt(self.robot)],
                                                state="disabled")
        self.p1btnRHazalt.pack()
        self.p1btnRHazalt.place(x = 120, y = 105)

        # -----------------------------PROBLEM 2 BUTTONS-------------------------------------
        self.p2btnLABDegistir = tkinter.Button(self.p2layout, text="LAB DEĞİŞTİR", bg="black",
                                                fg="white", width=13, font = ("arial 10 bold"), command=lambda:[self.LABDegistir()])
        self.p2btnLABDegistir.pack()
        self.p2btnLABDegistir.place(x = 5, y = 100)

        self.p2btnCalistir = tkinter.Button(self.p2layout, text="ÇALIŞTIR", bg="black",
                                             fg="white", width=13, font = ("arial 10 bold"),
                                              state="disabled", command=lambda:[self.P2Calistir()])
        self.p2btnCalistir.pack()
        self.p2btnCalistir.place(x = 5, y = 130)

        self.p2btnSonucGoster = tkinter.Button(self.p2layout, text="SONUÇ GÖSTER", bg="black", fg="white",
                                                width=13, font = ("arial 10 bold"),
                                                 state = "disabled", command=lambda:[self.P2SonucGoster()])
        self.p2btnSonucGoster.pack()
        self.p2btnSonucGoster.place(x = 5, y = 160)


        self.p2btnRHartir = tkinter.Button(self.p2layout, text="Robot Hızı (+)", bg="black",
                                                fg="white", width=13, font = ("calibri 10 bold"), command=lambda:[self.RobotHizArtir(self.robot2)],
                                                state="disabled")
        self.p2btnRHartir.pack()
        self.p2btnRHartir.place(x = 120, y = 100)

        self.p2btnRHazalt = tkinter.Button(self.p2layout, text="Robot Hızı (-)", bg="black",
                                                fg="white", width=13, font = ("calibri 10 bold"), command=lambda:[self.RobotHizAzalt(self.robot2)],
                                                state="disabled")
        self.p2btnRHazalt.pack()
        self.p2btnRHazalt.place(x = 120, y = 130)

        # -----------------------------SPİNS-------------------------------------        
        self.p2LabelSatir = ttk.Label(self.p2layout, text = "Satır: ", font = ("arial 10 bold"), background="dimgrey")
        self.p2LabelSatir.pack()
        self.p2LabelSatir.place(x = 5, y = 55)

        self.p2SpinSatir = ttk.Spinbox(self.p2layout, from_=0,  to=50, width=3, values= list(range(1,50)),  font = ("arial 10 bold"),)
        self.p2SpinSatir.pack()
        self.p2SpinSatir.set(15)
        self.p2SpinSatir.place(x = 45, y = 55)

        self.p2LabelSutun = ttk.Label(self.p2layout, text = "Sütun: ", font = ("arial 10 bold"), background="dimgrey")
        self.p2LabelSutun.pack()
        self.p2LabelSutun.place(x = 85, y = 55)

        self.p2SpinSutun = ttk.Spinbox(self.p2layout, from_=0,  to=50, width=3, values= list(range(1,50)),  font = ("arial 10 bold"),)
        self.p2SpinSutun.pack()
        self.p2SpinSutun.set(15)
        self.p2SpinSutun.place(x = 130, y = 55)

        self.root.mainloop()

    def URLGetir(self):
        self.SonucTextArea.delete("1.0",tkinter.END)
        self.p1btnRHartir["state"] = "disabled"
        self.p1btnRHazalt["state"] = "disabled"

        global URLkontrol
        global IzgaraKontrol_1
        global IzgaraKontrol_2

        if IzgaraKontrol_1 != 0:

            self.screen.clearscreen()
            self.robot.clear()
            self.hedef.clear()
            self.duvar.clear()
            self.duman.clear()
            self.engel_yerlestirici.clear()

            self.robot.clearstamps()
            self.hedef.clearstamps()
            self.duvar.clearstamps()
            self.duman.clearstamps()
            self.engel_yerlestirici.clearstamps()

            del self.robot
            del self.hedef
            del self.duvar
            del self.duman
            del self.engel_yerlestirici

        if IzgaraKontrol_2 != 0:
            
            self.robot2.clear()
            self.duvar2.clear()

            self.robot2.ht()

            self.robot2.clearstamps()
            self.duvar2.clearstamps()



            del self.robot2
            del self.duvar2

        self.screen.bgcolor("black")
        self.screen.tracer(0)

        if URLkontrol % 2 == 0:
            self.izgara = P1Izgara(URLListesi[0])
            self.canvas.config(width=self.izgara.maze_cols*self.izgara.wall_size_pixel+1,
                                  height=self.izgara.maze_rows*self.izgara.wall_size_pixel+1)
        else:
            self.izgara = P1Izgara(URLListesi[1])
            self.canvas.config(width=self.izgara.maze_cols*self.izgara.wall_size_pixel+1,
                                  height=self.izgara.maze_rows*self.izgara.wall_size_pixel+1)
            

        self.robot = Robot(self.screen, self.izgara.wall_size_geometry)
        self.hedef = Hedef(self.screen, self.izgara.wall_size_geometry)
        self.duvar = Duvar(self.screen, self.izgara.wall_size_geometry)
        self.duman = Duman(self.screen, self.izgara.wall_size_geometry)
        self.engel_yerlestirici = Engel_Yerlestirici(self.screen, self.izgara.wall_size_geometry)


        self.robot_start_coordinates, self.hedef_start_coordinates = self.RobotHedefYerlestir(self.robot, self.hedef, self.izgara.road_coordinates)
        
        self.DuvarYerlestir(self.izgara.all_coordinates, self.izgara.wall_coordinates, self.izgara.fridge_coordinates, self.izgara.road_coordinates,
                             self.robot_start_coordinates, self.hedef_start_coordinates, self.duvar,1)
        
        self.EngelleriYerlestir(Engel_Yerlestirici(self.screen, self.izgara.wall_size_geometry), Engel(self.izgara.wall_size_pixel).engel_cesitleri, 
                               self.screen, self.izgara.obstacles_coordinates, self.izgara.fridge_coordinates, self.izgara.wall_size_pixel, self.izgara.wall_coordinates)


        URLkontrol +=1
        IzgaraKontrol_1 +=1
        IzgaraKontrol_2 = 0

        self.p1btnCalistir["state"] = "normal"

    def P1Calistir(self):

        self.SonucTextArea.delete("1.0",tkinter.END)
        self.p1btnRHartir["state"] = "normal"
        self.p1btnRHazalt["state"] = "normal"

        self.p1btnSonucGoster["state"] = "normal"
        self.p1btnCalistir["state"] = "disabled"
        self.p1btnURLDegistir["state"] = "disabled" 

        self.stamp_koordinat = []
        self.stamp_id = []
        self.Dumanla(self.stamp_koordinat, self.stamp_id, self.duman, self.izgara.wall_size_pixel, self.izgara.all_coordinates)
        self.DumanTemizle(self.robot.xcor(), self.robot.ycor(), self.duman, self.izgara.wall_size_pixel, self.stamp_id, self.stamp_koordinat )
        
        self.screen.tracer(1)
        adim_sayisi,gecen_sure = self.LabirentDolas(self.canvas, self.robot, self.robot_start_coordinates, 
                      self.hedef_start_coordinates, self.duman, self.izgara.wall_size_pixel,
                      self.izgara.wall_coordinates, self.izgara.fridge_coordinates,
                      self.stamp_koordinat, self.stamp_id)
        
        self.screen.tracer(0)
        enkisayol = self.EnKisaYol(self.robot, self.robot_start_coordinates, self.izgara.wall_size_pixel, self.izgara.wall_coordinates, self.hedef_start_coordinates)
        self.EnKisaYol(self.robot, self.robot_start_coordinates, self.izgara.wall_size_pixel, self.izgara.wall_coordinates, self.hedef_start_coordinates)

        result = self.BilgileriAl(self.SonucTextArea, self.izgara.maze_rows, self.izgara.maze_cols,
                          self.robot_start_coordinates, self.hedef_start_coordinates, adim_sayisi, enkisayol, gecen_sure)
        
        with open('Sonuclar.txt', 'w') as f:
            f.write(result)

        self.p1btnURLDegistir["state"] = "normal"
        self.p1btnSonucGoster["state"] = "disable"
        self.p1btnRHartir["state"] = "disable"
        self.p1btnRHazalt["state"] = "disable"

    def P1SonucGoster(self):
        self.screen.tracer(0)
        
    def LABDegistir(self):
        self.SonucTextArea.delete("1.0",tkinter.END)
        self.p2btnRHartir["state"] = "disabled"
        self.p2btnRHazalt["state"] = "disabled"
        self.p2btnCalistir["state"] = "normal"

        global IzgaraKontrol_1
        global IzgaraKontrol_2


        self.izgara2 = P2Izgara(int(self.p2SpinSatir.get()), int(self.p2SpinSutun.get()))
        self.canvas.config(width=self.izgara2.maze_cols*self.izgara2.wall_size_pixel+1,
                                  height=self.izgara2.maze_rows*self.izgara2.wall_size_pixel+1)

        if IzgaraKontrol_1 != 0:

            self.screen.clearscreen()
            self.robot.clear()
            self.hedef.clear()
            self.duvar.clear()
            self.duman.clear()
            self.engel_yerlestirici.clear()

            self.robot.clearstamps()
            self.hedef.clearstamps()
            self.duvar.clearstamps()
            self.duman.clearstamps()
            self.engel_yerlestirici.clearstamps()

            del self.robot
            del self.hedef
            del self.duvar
            del self.duman
            del self.engel_yerlestirici

        if IzgaraKontrol_2 !=0:
            
            self.robot2.clear()
            self.duvar2.clear()

            self.robot2.clearstamps()
            self.duvar2.clearstamps()

            del self.robot2
            del self.duvar2


        self.robot2 = Robot(self.screen, self.izgara2.wall_size_geometry)
        self.duvar2 = Duvar(self.screen, self.izgara2.wall_size_geometry)
        
        self.screen.bgcolor("black")
        self.DuvarYerlestir(self.izgara2.all_coordinates, self.izgara2.wall_coordinates, self.izgara2.fridge_coordinates, self.izgara2.road_coordinates,
                             self.izgara2.start_coordinate, self.izgara2.aim_coordinate, self.duvar2,2)
        
        IzgaraKontrol_2 +=1
        IzgaraKontrol_1 = 0

    def P2Calistir(self):

        self.SonucTextArea.delete("1.0",tkinter.END)
        self.p2btnLABDegistir["state"] = "disabled"
        self.p2btnSonucGoster["state"] = "normal"
        self.p2btnRHartir["state"] = "normal"
        self.p2btnRHazalt["state"] = "normal"
        self.p2btnCalistir["state"] = "disabled"

        if IzgaraKontrol_2 !=0:
            
            self.robot2.clear()
            self.robot2.clearstamps()
           
        
        self.screen.tracer(1)
        self.RobotBaslangicaDon(self.robot2, self.izgara2.start_coordinate)

        
        adim_sayisi,gecen_sure = self.LabirentDolas2(self.robot2, self.izgara2.start_coordinate, self.izgara2.wall_size_pixel, self.izgara2.wall_coordinates,
                            self.izgara2.fridge_coordinates, self.izgara2.aim_coordinate, self.canvas)
        
        self.screen.tracer(0)
        enkisayol = self.EnKisaYol(self.robot2, self.izgara2.start_coordinate, self.izgara2.wall_size_pixel, self.izgara2.wall_coordinates, self.izgara2.aim_coordinate)
        self.EnKisaYol(self.robot2, self.izgara2.start_coordinate, self.izgara2.wall_size_pixel, self.izgara2.wall_coordinates, self.izgara2.aim_coordinate)
        self.robot2.ht()
        self.robot2.clearstamps()

        result = self.BilgileriAl(self.SonucTextArea, self.izgara2.maze_rows - 2, self.izgara2.maze_cols - 2,
                          self.izgara2.start_coordinate, self.izgara2.aim_coordinate, adim_sayisi, enkisayol, gecen_sure)
        
        with open('Sonuclar.txt', 'w') as f:
            f.write(result)
        
        self.p2btnRHartir["state"] = "disabled"
        self.p2btnRHazalt["state"] = "disabled"
        self.p2btnSonucGoster["state"] = "disabled"
        self.p2btnLABDegistir["state"] = "normal"

    def P2SonucGoster(self):
        self.screen.tracer(0)



uyg = Uygulama()