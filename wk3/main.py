import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.background(255)           # white background
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 20)

    draw_portrait(100,100)

    p5.push()
    p5.translate(p5.mouseX,p5.mouseY)
    p5.scale(p5.random(0.5,0.52))
    draw_portrait(100,100)
    p5.pop()

def draw_portrait(x,y):
    p5.fill(255,227,198)
    draw_base(100,100)
    draw_lips(100,110)
    draw_nose(100,110)
    p5.fill(255)
    draw_eyes_R(100,110)
    draw_eyes_L(100,110)
    draw_eyebrows(100,110)

def draw_base(x,y):
    p5.push()
    p5.translate(x-76,y-100)
    p5.scale(4)
    p5.fill(0)
    p5.rect(0,0,59,30)
    p5.pop()

    p5.push()
    p5.translate(x-65,y+80)
    p5.angleMode(p5.DEGREES) 
    p5.rotate(340)
    p5.strokeWeight(1.8)
    p5.ellipse(0, 0, 50, 80)
    p5.pop()

    p5.push()
    p5.translate(x+148,y+80)
    p5.angleMode(p5.DEGREES) 
    p5.rotate(20)
    p5.strokeWeight(1.8)
    p5.ellipse(0, 0, 50, 80)
    p5.pop()

    p5.push()
    p5.translate(x+42,y+35)
    p5.angleMode(p5.DEGREES) 
    p5.scale(6)
    p5.strokeWeight(0.6)
    p5.ellipse(0, 0, 40, 45)
    p5.pop()

    p5.push()
    p5.translate(x+42,y+100+p5.mouseY/140)
    p5.angleMode(p5.DEGREES)
    p5.scale(6)
    p5.strokeWeight(0.5)
    p5.arc(0,0,30,30,0,180)
    p5.pop()
    p5.push()
    p5.translate(x+42,y+115+p5.mouseY/160)
    p5.angleMode(p5.DEGREES)
    p5.scale(4)
    p5.strokeWeight(0.5)
    p5.arc(0,0,30,30,0,180)
    p5.pop()

def draw_eyebrows(x,y):
    p5.push()
    p5.translate(x-38,y-90+p5.mouseY/150)
    p5.fill(0)
    p5.quad(15,40,60,43,60,51,0,57)
    p5.pop()
    p5.push()
    p5.translate(x+45,y-90+p5.mouseY/150)
    p5.fill(0)
    p5.quad(15,43,60,40,75,57,15,51)
    p5.pop()


def draw_eyes_L(x,y):
    p5.push()
    p5.translate(x+93,y+4)
    p5.angleMode(p5.DEGREES)
    p5.rotate(5)
    p5.fill(255,227,198)
    p5.arc(0,0,60,30,190,340)
    p5.pop()

    p5.push()
    p5.translate(x+87,y+5)
    p5.angleMode(p5.DEGREES) 
    p5.fill(255,227,198)
    p5.arc(0,0,50,25,25,165)
    p5.pop()
    
    p5.push()
    p5.translate(x+87,y)
    p5.angleMode(p5.DEGREES)  
    p5.rotate(355)
    p5.ellipse(0, 0, 46, 20)
    p5.pop()

    p5.push()
    p5.translate(x+85+p5.mouseX/130, y-1+p5.mouseY/180)
    p5.angleMode(p5.DEGREES)  
    p5.rotate(340)
    p5.fill(0)
    p5.ellipse(0, 0, 20, 18)
    p5.pop()

    p5.push()
    p5.translate(x+92+p5.mouseX/130, y-3+p5.mouseY/180)
    p5.angleMode(p5.DEGREES)  
    p5.rotate(20)
    p5.fill(255)
    p5.ellipse(0, 0, 7, 5)
    p5.pop()

def draw_eyes_R(x,y):
    
    p5.push()
    p5.translate(x-7,y+4)
    p5.angleMode(p5.DEGREES)
    p5.rotate(355)
    p5.fill(255,227,198)
    p5.arc(0,0,60,30,200,350)
    p5.pop()

    p5.push()
    p5.translate(x,y+5)
    p5.angleMode(p5.DEGREES)
    p5.fill(255,227,198)
    p5.arc(0,0,50,25,20,160)
    p5.pop()
    
    p5.push()
    p5.translate(x,y)
    p5.angleMode(p5.DEGREES)  
    p5.rotate(5)
    p5.ellipse(0, 0, 46, 20)
    p5.pop()

    p5.push()
    p5.translate(x+3+p5.mouseX/130, y-1+p5.mouseY/180)
    p5.angleMode(p5.DEGREES)  
    p5.rotate(20)
    p5.fill(0)
    p5.ellipse(0, 0, 20, 18)
    p5.pop()

    p5.push()
    p5.translate(x+10+p5.mouseX/130, y-3+p5.mouseY/180)
    p5.angleMode(p5.DEGREES)  
    p5.rotate(20)
    p5.fill(255)
    p5.ellipse(0, 0, 7, 5)
    p5.pop()

def draw_lips(x,y):
    p5.angleMode(p5.RADIANS)
    p5.push()
    p5.translate(x+62,y+90)
    p5.arc(0,0,30,15,3.14,6.13)
    p5.pop()

    p5.push()
    p5.translate(x+25,y+90)
    p5.arc(0,0,30,15,3.30,0)
    p5.pop()

    p5.push()
    p5.translate(x+43,y+88)
    p5.strokeWeight(2)
    p5.arc(0,0,110,15,0.31,2.83)
    p5.pop()

    p5.push()
    p5.translate(x+43,y+95)
    p5.arc(0,0,70,30,0.31,2.83)
    p5.pop()

def draw_nose(x, y):
    p5.angleMode(p5.RADIANS)
    p5.push()
    p5.translate(x+30, y)
    p5.quad(0, 0, 25, 0,25,45,0,45)
    p5.pop()

    p5.push()
    p5.translate(x+2, y+10)
    p5.triangle(40, 10, 60, 40,20,40)
    p5.pop()

    p5.push()
    p5.translate(x+25,y+60)
    p5.strokeWeight(4)
    p5.arc(0,0,20,10,4.24,0)
    p5.pop()

    p5.push()
    p5.translate(x+60,y+60)
    p5.strokeWeight(4)
    p5.arc(0,0,20,10,3.14,5.18)
    p5.pop()

    p5.push()
    p5.translate(x+20,y+50)
    p5.arc(0,0,25,35,2.51,4.71)
    p5.pop()

    p5.push()
    p5.translate(x+65,y+50)
    p5.arc(0,0,25,35,4.71,0.63)
    p5.pop()

    p5.push()
    p5.translate(x+43,y+67)
    p5.arc(0,0,12,30,0,3.14)
    p5.pop()

    p5.push()
    p5.translate(x+31,y-2)
    p5.fill(255,227,198)
    p5.strokeWeight(0)
    p5.rect(0,0,23,55)
    p5.pop()
