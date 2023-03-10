import js
p5 = js.window

# class definition for the Point object:
class Player:  
    # this method is automatically called when object is instantated:
    def __init__(self, x = 0, y = 0):
        self.x = x  # initialize attribute x 
        self.y = y  # initialize attribute y 

    # print Point method (function "inside" object Point):
    def print_player(self):
        print('x = ' + str(self.x) + ', y = ' + str(self.y))

    # method to move the coordinates of a Point object:
    def move_player(self, distance_x, distance_y):
        self.x += distance_x
        self.y += distance_y

    # method to set the coordinates of a Point object:
    def set_player(self, x, y):
        self.x = x
        self.y = y

    # method to draw a Point object:
    def draw(self):
        p5.fill(255)
        p5.push()
        p5.translate(self.x, self.y)
        p5.rect(0,0,40,40)
        p5.pop()

        p5.fill(255)
        p5.push()
        p5.translate(self.x, self.y-15)
        p5.rect(0,0,40,20)
        p5.pop()

        p5.fill(255)
        p5.push()
        p5.translate(self.x+4,self.y+10)
        p5.rect(0,0,10,10)
        p5.pop()

        p5.fill(255)
        p5.push()
        p5.translate(self.x+26, self.y+10)
        p5.rect(0,0,10,10)
        p5.pop()

        p5.fill(255)
        p5.push()
        p5.translate(self.x+7, self.y+25)
        p5.rect(0,0,27,8)
        p5.pop()

        p5.fill(255)
        p5.push()
        p5.translate(self.x+28, self.y+40)
        p5.rect(0,0,18,10)
        p5.pop()

        p5.fill(255)
        p5.push()
        p5.translate(self.x-6, self.y+40)
        p5.rect(0,0,18,10)
        p5.pop()

        


# create an instance of Point object and assign it to variable:
player_1 = Player()  # instantiate an object with no arguments
player_1.print_player()

player_2 = Player(x = 150, y = 150)  # instantiate with x, y arguments
player_2.print_player()

def setup():
    p5.createCanvas(300, 300)  
    
def draw():
    p5.background(255)           
    player_1.draw() 
    player_2.draw() 


def keyPressed(event):
    pass 

def keyReleased(event):
    pass
