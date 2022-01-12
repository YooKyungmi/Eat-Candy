from turtle import*
import random

from practice import collision_block

colormode(255)
score=0
location=([-325,250],[-325,200],[-175,150],[-25,50],[-325,50],
          [-325,-50],[125,50],[275,100],[-325,-150])
surface=([650,50],[500,50],[200,100],[50,100],[50,100],
         [200,100],[150,200],[50,250],[650,100])

class Background(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.ht()
        self.penup()
        self.color(0,200,200)
        self.speed(0)
        for i in range(9):
            self.goto(location[i])
            self.begin_fill()
            for j in range(2):
                self.fd(surface[i][0])
                self.rt(90)
                self.fd(surface[i][1])
                self.rt(90)
            self.end_fill()
            
class Mycar(Turtle):
    image=['car_u.gif','car_d.gif','car_l.gif','car_r.gif']
    speed=5
    def __init__(self):
        Turtle.__init__(self)
        self.ht()
        self.penup()
        for a in self.image:
            screen.register_shape(a)
        self.shape('car_r.gif')
        self.speed2=self.speed
        self.aa=10
    def up(self):
        seth(90)
        self.shape(self.image[0])
        fd(self.speed)
        self.aa=90
    def down(self):
        seth(270)
        self.shape(self.image[1])
        fd(self.speed)
        self.aa=270
    def up(self):
        seth(180)
        self.shape(self.image[2])
        fd(self.speed)
        self.aa=180
    def up(self):
        seth(0)
        self.shape(self.image[3])
        fd(self.speed)
        self.aa=0
    def move(self):
        if collision_block(self.pos()) and self.heading()==self.aa:
            self.speed=0
        else: self.speed=self.speed2
        self.score_count()
    def score_count(self):
        global score
        for a in candyList:
            if self.distance(a)<30:
                score+=50
                a.ht()
                candyList.remove(a)
                printScreen()
        
        if collision_block(self.pos()) and self.speed==0:
            if len(life):
                score-=100
                life.pop().ht()
                printScreen()
            
        
        
candyList=[]
def printCandy():
    return        
        
def collision_block(posB) :
    return 1
life=[]
def printScreen():
    return       

def play():
    my.move()
    
            
screen=Screen()
screen.setup(width=650,height=500)
screen.bgcolor(120,120,120)
back=Background()
my=Mycar()

onkey(play,"")
onkeypress(my.up,"Up")
onkeypress(my.down,"Down")
onkeypress(my.left,"Left")
onkeypress(my.right,"Right")

mainloop()