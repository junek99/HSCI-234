import js
p5 = js.window


program_state = 'START'
score = 0

    
class Spaceship:  
    def __init__(self, x=150, y=250):
        self.img1 = p5.loadImage('img_ship.png');  
        self.img2 = p5.loadImage('img_ship2.png');
        self.img3 = p5.loadImage('img_ship3.png');
        self.x = x  
        self.y = y  
        self.speed = 3

        
    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.image(self.img1, 0, 0)
        p5.pop()

        if p5.keyCode == p5.UP_ARROW:
            self.img1 = p5.loadImage('img_ship2.png')
        
        elif p5.keyCode == p5.DOWN_ARROW:
            self.img1 = p5.loadImage('img_ship3.png')

        elif p5.keyCode == p5.LEFT_ARROW:
            self.img1 = p5.loadImage('img_ship.png')
        
        elif p5.keyCode == p5.RIGHT_ARROW:
            self.img1 = p5.loadImage('img_ship.png')
class Sprite:
    def __init__(self, x = 0, y = 0):
        p5.imageMode(p5.CENTER)
        self.x = x  
        self.y = p5.random(0,p5.height)  
        self.img = p5.loadImage('asteroid.png')
        self.size = p5.random(1, 5)
        self.speed = p5.random(1, 3) 
        self.direction = 1

class Asteroidsa(Sprite):    
    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.scale(self.size)
        p5.image(self.img, 0, 0,)
        p5.pop()
        self.x -= self.speed * self.direction
        if self.x < -20: # '-' because it moves from right to left   
            self.x = 320
            self.y = p5.random(0,p5.height)
            self.size = p5.random(0.8, 2)
            self.speed = p5.random(2, 4)
            increase_score()
            
class Asteroidsb(Sprite):
    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.scale(self.size)
        p5.image(self.img, 0, 0,)
        p5.pop()
        self.x -= self.speed * self.direction
        if self.x < -20: # '-' because it moves from right to left   
            self.x = 320
            self.y = p5.random(0,p5.height)
            self.size = p5.random(1.5, 4)
            self.speed = p5.random(1, 3)
            increase_score()

class Asteroidsc(Sprite):
    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.scale(self.size)
        p5.image(self.img, 0, 0,)
        p5.pop()
        self.x -= self.speed * self.direction
        if self.x < -20: # '-' because it moves from right to left   
            self.x = 320
            self.y = p5.random(0,p5.height)
            self.size = p5.random(2, 5)
            self.speed = p5.random(1.3, 3.5)
            increase_score()

class Asteroidsd(Sprite):
    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.scale(self.size)
        p5.image(self.img, 0, 0,)
        p5.pop()
        self.x -= self.speed * self.direction
        if self.x < -20: # '-' because it moves from right to left   
            self.x = 320
            self.y = p5.random(0,p5.height)
            self.size = p5.random(1, 5)
            self.speed = p5.random(1, 5)
            increase_score()

class Asteroidse(Sprite):
    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.scale(self.size)
        p5.image(self.img, 0, 0,)
        p5.pop()
        self.x -= self.speed * self.direction
        if self.x < -20: # '-' because it moves from right to left   
            self.x = 320
            self.y = p5.random(0,p5.height)
            self.size = p5.random(1, 5)
            self.speed = p5.random(0.5, 3)
            increase_score()

class Asteroidsf(Sprite):
    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.scale(self.size)
        p5.image(self.img, 0, 0,)
        p5.pop()
        self.x -= self.speed * self.direction
        if self.x < -20: # '-' because it moves from right to left   
            self.x = 320
            self.y = p5.random(0,p5.height)
            self.size = p5.random(2.5, 5)
            self.speed = p5.random(2, 3.5)
            increase_score()


class Goal:
    def __init__(self, x=0, y=0):
        self.x = x  
        self.y = y
        self.img = p5.loadImage('img_test3.png')
        self.timer = p5.millis()
    
    def update(self):
        if(p5.millis() > self.timer + 500):
            if(self.x < p5.width - self.img.width/2):
                self.x += 2
            else:
                self.x = self.img.width/2
            self.timer = p5.millis()  # update timer
       
        if self.x >= 280:
            global program_state
            program_state = 'SURVIVED'

    def draw(self):
        p5.push()
        p5.translate(0,0)
        p5.rect(0,280,300,20)
        p5.pop()

        p5.push()
        p5.translate(self.x, self.y)
        p5.image(self.img, 5, 5)
        p5.pop()
        
        p5.push()
        p5.translate(280,280)
        p5.fill(255,0,0)
        p5.rect(0,5,10,10)
        p5.pop()

class Space:
    def __init__(self, x=0,y=0):
        self.x = x  
        self.y = y  
        self.img = p5.loadImage('space.png')
        self.speed = 1
        self.direction = 1 # From right to left


    def draw(self):
        self.x -= self.speed 
        if self.x < -150: # '-' because it moves from right to left   
            self.x = 0
        p5.push()
        p5.translate(self.x, self.y)
        p5.image(self.img, 290, 140)
        p5.pop()


space = Space(0,0) 
asteroidsa = Asteroidsa(300,p5.random(0,280))
asteroidsb = Asteroidsb(300,p5.random(20,260))
asteroidsc = Asteroidsc(300,p5.random(80,240))
asteroidsd = Asteroidsd(300,p5.random(10,150))
asteroidse = Asteroidse(300,p5.random(50,250))
asteroidsf = Asteroidsf(300,p5.random(110,220))

spaceship = Spaceship(50,150)
goal = Goal(0,280)

def increase_score():
    global score
    if asteroidsa.size and asteroidsb.size and asteroidsc.size and asteroidsd.size and asteroidse.size and asteroidsf.size >= 3.5:
        score += 25
    else:
        score += 10
        
def setup():
    p5.createCanvas(300, 300) 
    print('finished setup') 
    
def draw():
    global program_state, score


    if program_state == 'START': # Start Screen
        p5.background(0)  
        asteroidsa.draw()
        p5.fill(255)
        p5.textFont('Comic Sans MS', 30)
        p5.text('Asteroid Attack', 35, 130)
        p5.textFont('Comic Sans MS', 13)
        p5.text('By June Kwak', 110, 160)
        p5.textFont('Comic Sans MS', 18)
        p5.text('press SHIFT to start', 65, 210)
        p5.push()
        p5.translate(0,-380)
        p5.scale(3)
        spaceship.draw()
        p5.pop()
        
        
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
    
        asteroidsa.draw()
        asteroidsb.draw()
        asteroidsc.draw()
        asteroidse.draw()
        asteroidsd.draw()
        asteroidsf.draw()
       
        spaceship.draw()
        goal.update()
        goal.draw()

        p5.textFont('Comic Sans MS', 10)
        p5.text('Score: ' + str(score), 10, 20)


        d = p5.dist(spaceship.x, spaceship.y, asteroidsa.x, asteroidsa.y)
        if(d < 15*asteroidsa.size/2):  
            print('ASTEROIIIIID IMPACCCCCTTTT')
            program_state = 'GAMEOVER'
        d = p5.dist(spaceship.x, spaceship.y, asteroidsb.x, asteroidsb.y)
        if(d < 15*asteroidsb.size/2):  
            print('ASTEROIIIIID IMPACCCCCTTTT')
            program_state = 'GAMEOVER'

        d = p5.dist(spaceship.x, spaceship.y, asteroidsc.x, asteroidsc.y)
        if(d < 15*asteroidsc.size/2):   
            print('ASTEROIIIIID IMPACCCCCTTTT')
            program_state = 'GAMEOVER'

        d = p5.dist(spaceship.x, spaceship.y, asteroidsd.x, asteroidsd.y)
        if(d < 15*asteroidsd.size/2):  
            print('ASTEROIIIIID IMPACCCCCTTTT')
            program_state = 'GAMEOVER'
            
        d = p5.dist(spaceship.x, spaceship.y, asteroidse.x, asteroidse.y)
        if(d < 15*asteroidse.size/2):  
            print('ASTEROIIIIID IMPACCCCCTTTT')
            program_state = 'GAMEOVER'

        d = p5.dist(spaceship.x, spaceship.y, asteroidsf.x, asteroidsf.y)
        if(d < 15*asteroidsf.size/2):   
            print('ASTEROIIIIID IMPACCCCCTTTT')
            program_state = 'GAMEOVER'
        
       

    elif(program_state == 'GAMEOVER'):
        p5.background(0)  
        p5.textFont('Comic Sans MS', 30)
        p5.fill(255)
        p5.text('GAME OVER', 65, 200)
        p5.textFont('Comic Sans MS', 15)
        p5.text('press SHIFT to replay', 75, 240)

    elif(program_state == 'SURVIVED'):
        p5.background(0)  
        p5.textFont('Comic Sans MS', 30)
        p5.fill(255)
        p5.text('YOU SURVIVED', 40, 200)
        p5.textFont('Comic Sans MS', 20)
        p5.text('Total Score:'+ str(score), 85, 238)
        p5.textFont('Comic Sans MS', 15)
        p5.text('press SHIFT to return title', 55, 270)


def keyPressed(event):
    global program_state, score, space, asteroidsa , asteroidsb, asteroidsc, asteroidsd, asteroidse, asteroidsf, spaceship
    if p5.keyCode == p5.SHIFT:
        if program_state == 'START':
            program_state = 'PLAY'  
        
        elif program_state == 'GAMEOVER':
            program_state = 'PLAY'
            score = 0
            space = Space(0,0)
            asteroidsa = Asteroidsa(300,p5.random(0,280))
            asteroidsb = Asteroidsb(300,p5.random(20,260))
            asteroidsc = Asteroidsc(300,p5.random(80,240))
            asteroidsd = Asteroidsd(300,p5.random(10,150))
            asteroidse = Asteroidse(300,p5.random(50,250))
            asteroidsf = Asteroidsf(300,p5.random(110,220))
            spaceship = Spaceship(50,150)
            goal.x = 0 
            goal.y = 280 
        
        elif program_state == 'SURVIVED':
            program_state = 'START'
            score = 0
            space = Space(0,0)
            asteroidsa = Asteroidsa(300,p5.random(0,280))
            asteroidsb = Asteroidsb(300,p5.random(20,260))
            asteroidsc = Asteroidsc(300,p5.random(80,240))
            asteroidsd = Asteroidsd(300,p5.random(10,150))
            asteroidse = Asteroidse(300,p5.random(50,250))
            asteroidsf = Asteroidsf(300,p5.random(110,220))
            spaceship = Spaceship(50,150)
            goal.x = 0 
            goal.y = 280 
            
    
def keyReleased(event):
    pass
def mousePressed(event):
    pass

def mouseReleased(event):
    pass
