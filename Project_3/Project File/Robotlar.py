import turtle


class Robot(turtle.RawTurtle):
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        super().__init__(self.screen)
        self.ht()
        self.up()
        self.shape("turtle")
        self.color("black")
        self.speed(1)
        self.shapesize(*size)

class Engel_Yerlestirici(turtle.RawTurtle):
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        super().__init__(self.screen)
        self.ht()
        self.up()
        self.shapesize(*size)

class Hedef(turtle.RawTurtle):
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        super().__init__(self.screen)
        self.ht()
        self.up()
        self.shape("circle")
        self.color("red")
        self.shapesize(*size)

class Duvar(turtle.RawTurtle):
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        super().__init__(self.screen)
        self.ht()
        self.up()
        self.shape("square")
        self.shapesize(*size)
        self.screen.tracer(0)


class Duman(turtle.RawTurtle):
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        super().__init__(self.screen)
        self.ht()
        self.up()
        self.shape("square")
        self.color("dimgrey")
        self.shapesize(*size)
        self.screen.tracer(0)
