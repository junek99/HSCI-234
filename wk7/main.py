import js
p5 = js.window

class Player:  
    def __init__(self, x = 0, y = 0, speed=3):
        self.x = x  
        self.y = y  
        self.speed = speed  
        self.direction = 1  

    def animate_player(self):#player moves right and left, bounce if it hits the wall
        self.x += self.direction * self.speed
        if self.x < 0 or self.x > p5.width:
            self.direction *= -1
            self.x += self.direction * self.speed

    def print_player(self):
        print('x = ' + str(self.x) + ', y = ' + str(self.y))

    def move_player(self, distance_x, distance_y):
        self.x += distance_x
        self.y += distance_y

    def set_player(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        if self == player_1:
            p5.fill(255,0,0)  # red color for player_1
            p5.stroke(255,0,0)
        else:
            p5.fill(0, 0, 255)  # blue color for player_2
            p5.stroke(0,0,255) 
        
        p5.push()
        p5.translate(self.x, self.y)
        p5.rect(0,0,40,20)
        p5.pop()
        
        p5.push()
        p5.translate(self.x-10, self.y+20)
        p5.rect(0,0,60,15)
        p5.pop()
        
        p5.push()
        p5.translate(self.x, self.y-20)
        p5.rect(15,0,10,40)
        p5.pop()
       
        p5.push()
        p5.translate(self.x-35, self.y+7)
        p5.rect(15,0,10,38)
        p5.pop()
        
        p5.push()
        p5.translate(self.x+35, self.y+7)
        p5.rect(15,0,10,38)
        p5.pop()


player_1 = Player(x = 50, y = 50)  
player_1.print_player()
player_2 = Player(x = 140, y = 170)  
player_2.print_player()


def setup():
    p5.createCanvas(300, 300) 
    print('finished setup')  
    
def draw():
    p5.background(0)           
    player_1.draw() 
    player_1.animate_player()
    player_2.draw() 



def keyPressed(event): #move player_2 with keyboard
    if p5.keyCode == p5.LEFT_ARROW:
        player_2.move_player(-20, 0)
    elif p5.keyCode == p5.RIGHT_ARROW:
        player_2.move_player(20, 0)
    elif p5.keyCode == p5.UP_ARROW:
        player_2.move_player(0, -20)
    elif p5.keyCode == p5.DOWN_ARROW:
        player_2.move_player(0, 20)

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass
