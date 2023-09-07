
import requests
from P2Fonksiyonlar import P2Fonksiyonlar

class P1Izgara():

    def __init__(self, url):

        self.url = url
        page = requests.get(url) 
        maze = page.text
        self.maze = []
        for line in maze.splitlines():
            value = "5" + line + "5"
            self.maze.append(value)
            
        self.maze.insert(0, "5"*len(self.maze[0]))
        self.maze.append("5"*len(self.maze[0]))
        self.maze_rows = len(self.maze) 
        self.maze_cols = len(self.maze[0])
        
        self.game_space = 600 
        
        if self.maze_rows > self.maze_cols:
            self.wall_size_pixel    = round(self.game_space / self.maze_rows)  
        else:
            self.wall_size_pixel = round(self.game_space / self.maze_cols) 
      
        self.wall_size_geometry = (self.wall_size_pixel/23, self.wall_size_pixel/23, .5)

        self.all_coordinates  = []
        self.road_coordinates = []
        self.fridge_coordinates = []
        self.obstacles_coordinates = []
        self.wall_coordinates = []

        for y in range(len(self.maze)):
            for x in range(len(self.maze[0])):
                character = self.maze[y][x]
                x_coordinate = -1*self.game_space / 2 + x*self.wall_size_pixel + self.wall_size_pixel/2
                y_coordinate =    self.game_space / 2 - y*self.wall_size_pixel - self.wall_size_pixel/2

                self.all_coordinates.append((x_coordinate, y_coordinate))
                self.obstacles_coordinates.append([(x_coordinate,y_coordinate ), character])
                
                if character == "5":
                    self.fridge_coordinates.append((x_coordinate,y_coordinate))
                elif character == "0":
                    self.road_coordinates.append((x_coordinate,y_coordinate))
                else:
                    self.wall_coordinates.append((x_coordinate,y_coordinate))
        
class P2Izgara(P2Fonksiyonlar):

    def __init__(self, rows, cols):

        P2Fonksiyonlar().__init__()

        self.rows = rows
        self.cols = cols

        self.maze = self.RastgeleLabirentOlustur(self.rows, self.cols, (0,0), (self.rows-1, self.cols-1))

        self.maze_rows = len(self.maze) 
        self.maze_cols = len(self.maze[0])
        
        self.game_space = 600 
        
        if self.maze_rows > self.maze_cols:
            self.wall_size_pixel    = round(self.game_space / self.maze_rows)  
        else:
            self.wall_size_pixel = round(self.game_space / self.maze_cols) 
      
        self.wall_size_geometry = (self.wall_size_pixel/22, self.wall_size_pixel/22, self.wall_size_pixel/22)

        self.all_coordinates  = []
        self.road_coordinates = []
        self.fridge_coordinates = []
        self.obstacles_coordinates = []
        self.wall_coordinates = []
        self.start_coordinate = None
        self.aim_coordinate = None

        for y in range(len(self.maze)):
            for x in range(len(self.maze[0])):
                character = self.maze[y][x]
                x_coordinate = -1*self.game_space / 2 + x*self.wall_size_pixel + self.wall_size_pixel/2
                y_coordinate =    self.game_space / 2 - y*self.wall_size_pixel - self.wall_size_pixel/2

                self.all_coordinates.append((x_coordinate, y_coordinate))
                self.obstacles_coordinates.append([(x_coordinate,y_coordinate ), character])
        
                if character == "S":
                    self.start_coordinate = (x_coordinate,y_coordinate)
                elif character == "F":
                    self.aim_coordinate = (x_coordinate,y_coordinate )
                elif character == "5":
                    self.fridge_coordinates.append((x_coordinate,y_coordinate))
                elif character == "0":
                    self.road_coordinates.append((x_coordinate,y_coordinate))
                elif character == "1":
                    self.wall_coordinates.append((x_coordinate,y_coordinate))
   




