import js
p5 = js.window

rect_x = 80
rect_y = 150
p=90
o=118
g=90
l=118
x = 0
speed = 25
angle = 0 
angle_barrel=0

r=70
t=10 

def draw_shell(): #shell
    global angle_barrel
    p5.push()
    p5.translate(g,l)
    angle_barrel += 0 
    p5.rotate(p5.radians(angle_barrel))
    p5.fill(0)
    p5.ellipse(r, t, 25, 20)
    p5.pop()


def draw_barrel(): #barrel

    global angle_barrel
    p5.rectMode(p5.CORNER)
    p5.push()
    p5.translate(p,o)
    angle_barrel += 0 
    p5.rotate(p5.radians(angle_barrel))
    p5.fill(75,83,32)
    p5.stroke(0)
    p5.rect(0,0,80,20)
    p5.rect(58,-8,25,35)
    p5.pop()

def draw_body(): #body
    p5.rectMode(p5.CENTER)
    p5.fill(75,74,32)
    p5.stroke(75,74,32)
    p5.rect(rect_x,rect_y+15,90,35)
    p5.rect(rect_x-10,rect_y-23,70,40)

def draw_frame(): #wheelframe
    p5.rectMode(p5.CENTER)
    p5.fill(0)
    p5.stroke(0)
    p5.rect(rect_x,rect_y+40,120,30)
    p5.arc(rect_x-60,rect_y+40,30,30,1.57,4.71)
    p5.arc(rect_x+60,rect_y+40,30,30,4.71,1.57)

def draw_wheel(): #wheel

    global angle    
    p5.ellipseMode(p5.CENTER)
    p5.push()
    p5.translate(rect_x-55,rect_y+40)
    angle += 0 
    p5.rotate(p5.radians(angle))
    p5.fill(255)
    p5.ellipse(0,0,22,22)
    p5.fill(100)
    p5.arc(0,0,22,22,0.4,4.71)
    p5.pop()


def draw_scope():#scope follows mouse
    p5.rectMode(p5.CENTER)
    p5.push()
    p5.translate(p5.mouseX,p5.mouseY)
    p5.fill(255,0,0)
    p5.noStroke()
    p5.rect(0,0,3,60)
    p5.rect(0,0,60,3)
    p5.strokeWeight(2)
    p5.stroke(255,0,0)
    p5.noFill()
    p5.ellipse(0,0,40,40)
    p5.pop()

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 
    p5.rectMode(p5.CENTER)


def draw():
    p5.background(255)           # white background
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 20)


    if(p5.mouseIsPressed == True):
        if (p5.mouseButton == p5.LEFT):
            global x, r, t
            x = x + speed 
            r=r+x

            
    global rect_x,rect_y,p,o,g,l
    global angle, angle_barrel 

    
    if(p5.keyIsPressed == True):  # Moving tank+wheel
        if(p5.key == 'a'):  # left 
            rect_x = rect_x - 2
            p=p-2
            g=g-2
            angle = angle -2
        elif(p5.key == 'd'):  # right
            rect_x = rect_x + 2
            angle = angle +2
            p=p+2
            g=g+2

        elif(p5.key == 'w'):  # up 
            rect_y = rect_y-2
            angle = angle +2
            o=o-2
            l=l-2
        elif(p5.key == 's'):  # down 
            rect_y = rect_y+2
            angle = angle -2
            o=o+2
            l=l+2

    if(p5.keyIsPressed == True): # barrel angle
        if(p5.key == 'e'):
            angle_barrel = anglebarrel = p5.mouseX/1.1+p5.mouseY/1.1
            x = 0 
            r=40           
            p5.push()
            p5.translate(0,0)
            draw_shell()
            p5.pop()
            
    draw_shell()
    draw_barrel()
    draw_body()
    draw_frame()

    for i in range(6): # Wheel variable
        d = 0 + i*22
        z = 0

        p5.push()
        p5.translate(d, z)
        draw_wheel()
        p5.pop()

    draw_scope()
