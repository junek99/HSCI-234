import js
p5 = js.window

x=0
y=0
alpha=0

random_size=int(p5.random(25,125))
random_size2=int(p5.random(0,100))
random_size3=int(p5.random(30,200))
random_size4=int(p5.random(60,300))

def random_square(size):
    p5.line(random_size,random_size,random_size+random_size,random_size)
    p5.line(random_size,random_size,random_size,random_size+random_size)
    p5.line(random_size,random_size+random_size,random_size+random_size,random_size+random_size)
    p5.line(random_size+random_size,random_size,random_size+random_size,random_size+random_size)

def random_square2(size):

    p5.stroke
    p5.line(random_size2,random_size2,random_size2+random_size2,random_size2)
    p5.stroke
    p5.line(random_size2,random_size2,random_size2,random_size2+random_size2)
    p5.stroke
    p5.line(random_size2,random_size2+random_size2,random_size2+random_size2,random_size2+random_size2)
    p5.stroke
    p5.line(random_size2+random_size2,random_size2,random_size2+random_size2,random_size2+random_size2)

def random_square3(size):
    global alpha
    p5.stroke(17, 0, 212,alpha)
    p5.line(random_size3,random_size3,random_size3+random_size3,random_size3)
    p5.stroke(171, 123, 111,alpha)
    p5.line(random_size3,random_size3,random_size3,random_size3+random_size3)
    p5.stroke(142, 54, 93,alpha)
    p5.line(random_size3,random_size3+random_size3,random_size3+random_size3,random_size3+random_size3)
    p5.stroke(154, 38, 64,alpha)
    p5.line(random_size3+random_size3,random_size3,random_size3+random_size3,random_size3+random_size3)
    alpha=alpha+1

def random_square4(size):
    p5.stroke(200)
    p5.line(random_size4,random_size4,random_size4+random_size4,random_size4)
    p5.stroke(200)
    p5.line(random_size4,random_size4,random_size4,random_size4+random_size4)
    p5.stroke(200)
    p5.line(random_size4,random_size4+random_size4,random_size4+random_size4,random_size4+random_size4)
    p5.stroke(200)
    p5.line(random_size4+random_size4,random_size4,random_size4+random_size4,random_size4+random_size4)


def random_square_at(x,y,size):
    p5.stroke(127, 0, 255,alpha)
    p5.line(random_size,random_size,random_size+random_size,random_size)
    p5.stroke(255, 127, 54)
    p5.line(random_size,random_size,random_size,random_size+random_size)
    p5.stroke(127, 200, 0)
    p5.line(random_size,random_size+random_size,random_size+random_size,random_size+random_size)
    p5.stroke(255, 0, 127)
    p5.line(random_size+random_size,random_size,random_size+random_size,random_size+random_size)


def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 
    print('finished setup')

def draw():
    p5.background(255)           # white background
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
    p5.strokeWeight(2)  # set stroke thickness

    global random_size,random_size2,random_size3,random_size4
    global x,y,d
    
    p5.line(random_size,random_size,random_size+random_size,random_size)
    p5.line(random_size,random_size,random_size,random_size+random_size)
    p5.line(random_size,random_size+random_size,random_size+random_size,random_size+random_size)
    p5.line(random_size+random_size,random_size,random_size+random_size,random_size+random_size)

    p5.push()
    p5.translate(x,y)
    random_square(random_size)
    p5.pop()

    p5.push()
    p5.translate(x-60,y-60)
    random_square_at(x,y,random_size)
    p5.pop()

    if(p5.mouseIsPressed == True):
        p5.push()
        p5.translate(x,y)
        random_square2(random_size2)
        p5.pop()

    p5.push()
    p5.translate(x,y)
    random_square3(random_size3)
    p5.pop()

    

    if(p5.mouseX < random_size4):
        p5.stroke(140,123,125)
    else:
        p5.stroke(200)
    p5.push()
    p5.translate(x,y)
    random_square4(random_size4)
    p5.pop()
