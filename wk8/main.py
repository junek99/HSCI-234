import js
p5 = js.window

class Spaceship:  
    def __init__(self, x=150, y=250):
        self.x = x  
        self.y = y  
        self.speed = 3

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.fill(0)
        p5.rect(0, 0, 20, 10)
        p5.pop()

spaceship = Spaceship(20, 150)

def setup():
    p5.createCanvas(300, 300) 
    print('finished setup') 
    
def draw():
    p5.background(255)  
    if p5.keyIsPressed:
        if p5.keyCode == p5.UP_ARROW:
            if spaceship.y > 0:
                spaceship.y -= spaceship.speed
        elif p5.keyCode == p5.DOWN_ARROW:
            if spaceship.y < p5.height - 10:
                spaceship.y += spaceship.speed
        elif p5.keyCode == p5.LEFT_ARROW:
            if spaceship.x > 0:
                spaceship.x -= spaceship.speed
        elif p5.keyCode == p5.RIGHT_ARROW:
            if spaceship.x < p5.width - 20:
                spaceship.x += spaceship.speed
                
    spaceship.draw() 

def keyPressed(event):
    pass 

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass
