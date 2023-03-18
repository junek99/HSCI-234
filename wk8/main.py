import js
p5 = js.window


program_state = 'START'
score = 0


class Space:
    def __init__(self, x=150, y=250):
        self.x = x  
        self.y = y  
        self.speed = 1
        self.direction = 1 # From right to left


    def draw(self):
        self.x -= self.speed 
        if self.x < -300: # '-' because it moves from right to left   
            self.x = -150 
        for i in range(12): 
            d = self.x + i*50
            p5.push()
            p5.translate(d, self.y)
            p5.fill(112,116,165)
            p5.rect(0,0,10,300)
            p5.pop()
    
class Spaceship:  
    def __init__(self, x=150, y=250):
        self.img = p5.loadImage('img_test.png')
        self.x = x  
        self.y = y  
        self.speed = 3
        
        
    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.image(self.img, 0, 0)
        p5.pop()


class Asteroids:
    def __init__(self, x = 0, y = 0):
        self.x = x  
        self.y = y  
        self.size = p5.random(10, 30)
        self.speed = p5.random(1, 5) 
        self.direction = 1  
     
    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.rect(0,0, self.size, self.size)
        p5.pop()
        self.x -= self.speed * self.direction
        
space = Space(0,0) 
asteroids = Asteroids(300,150)
spaceship = Spaceship(50,150)



def setup():
    p5.createCanvas(300, 300) 
    print('finished setup') 
    
def draw():
    global program_state, score


    if program_state == 'START': # Start Screen
        p5.background(0)  
        p5.fill(255)
        p5.textFont('Comic Sans MS', 30)
        p5.text('Asteroid Attack', 35, 130)
        p5.textFont('Comic Sans MS', 13)
        p5.text('By June Kwak', 110, 160)
        p5.textFont('Comic Sans MS', 18)
        p5.text('click SHIFT to start', 65, 210)
        
        
    elif program_state == 'PLAY': # Game Play
        p5.background(141,143,181)  
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
        
        space.draw()
        asteroids.draw()
        spaceship.draw()


        p5.textFont('Comic Sans MS', 10)
        p5.text('Score: ' + str(score), 10, 20)


        d = p5.dist(spaceship.x, spaceship.y, asteroids.x, asteroids.y)
        if(d < 20):  
            print('ASTEROIIIIID IMPACCCCCTTTT')
            program_state = 'GAMEOVER'
       

    elif(program_state == 'GAMEOVER'):
        p5.background(0)  
        p5.textFont('Comic Sans MS', 30)
        p5.fill(255)
        p5.text('GAME OVER', 60, 150)
        p5.textFont('Comic Sans MS', 15)
        p5.text('press BACKSPACE to play', 60, 190)


def keyPressed(event):
    global program_state, score, space, asteroids, spaceship
    if p5.keyCode == p5.SHIFT:
        if program_state == 'START':
            program_state = 'PLAY'  
    elif p5.keyCode == p5.BACKSPACE:
        if program_state == 'GAMEOVER':
            program_state = 'PLAY'
            score = 0
            space = Space(0,0)
            asteroids = Asteroids(300,150)
            spaceship = Spaceship(50,150)
            
def keyReleased(event):
    pass


def mousePressed(event):
    pass


def mouseReleased(event):
    pass
