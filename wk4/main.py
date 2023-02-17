import js
p5 = js.window

rect_x = 80
rect_y = 150

x = 0
speed = 10
angle = 0 


def draw_barrel():
    p5.rectMode(p5.CENTER)
    p5.fill(75,83,32)
    p5.stroke(0)
    p5.rect(rect_x+50,rect_y-23,80,20)

def draw_body():
    p5.rectMode(p5.CENTER)
    p5.fill(75,74,32)
    p5.stroke(75,74,32)
    p5.rect(rect_x,rect_y+15,90,35)
    p5.rect(rect_x-10,rect_y-23,70,40)

def draw_frame():
    p5.rectMode(p5.CENTER)
    p5.fill(0)
    p5.stroke(0)
    p5.rect(rect_x,rect_y+40,120,30)
    p5.arc(rect_x-60,rect_y+40,30,30,1.57,4.71)
    p5.arc(rect_x+60,rect_y+40,30,30,4.71,1.57)

def draw_wheel():
    
    for i in range(6):
        x = rect_x-55 + i*22
        y = rect_y+40
        d=22
        
        
        global angle    
        p5.ellipseMode(p5.CENTER)
        p5.push()
        p5.translate(0,0)
        p5.rotate(p5.radians(angle))
        angle += 0 
        p5.fill(255)
        p5.ellipse(x,y,d,d)
        p5.fill(100)
        p5.arc(x,y,d,d,0.4,4.71)
        p5.pop()

def draw_scope():
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


    if (p5.mouseIsPressed == True):
        if (p5.mouseButton == p5.LEFT):
            global x
            x = x + speed  # increment x
            p5.ellipse(p5.mouseX+x, p5.mouseY, 20, 20)

    global rect_x, rect_y
    global angle    

    
    if(p5.keyIsPressed == True):
        if(p5.key == 'a'):  # left 
            rect_x = rect_x - 1
            angle = angle -1
        elif(p5.key == 'd'):  # right
            rect_x = rect_x + 1
            angle = angle +1

        elif(p5.key == 'w'):  # up 
            rect_y = rect_y - 1
        elif(p5.key == 's'):  # down 
            rect_y = rect_y + 1

    draw_barrel()
    draw_body()
    draw_frame()
    draw_wheel()
    draw_scope()
