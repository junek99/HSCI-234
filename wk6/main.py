import js
p5 = js.window

program_timer = p5.millis()
program_state = draw_ice()

def setup():
    p5.createCanvas(300, 300)  
    print('finished setup..')

def draw_ice():
    p5.push()
    p5.translate(110,50)
    p5.fill(0,0,255)
    p5.quad(0,60,30,90,30,140,0,110)
    p5.quad(30,90,60,60,60,110,30,140)
    p5.quad(0,60,30,30,60,60,30,90)
    p5.pop()

def draw_water():
    p5.push()
    p5.translate(120,165)
    p5.stroke(0,0,255)
    p5.fill(0,0,255)
    p5.ellipse(0,0,102,22)
    p5.ellipse(0,20,52,22)
    p5.ellipse(35,15,52,22)
    p5.ellipse(40,8,80,18)
    p5.pop()


def draw():
    p5.background(255)           
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
  

    msec = p5.millis()  # get running time in milliseconds
    sec = int(msec / 1000)  # calculate time in seconds
    p5.fill(0)
    p5.text('milliseconds: ' + str(msec), 10, 20)
    p5.text('seconds: ' + str(sec), 10, 35)

    if(p5.millis() % 2000 < 500):
        program_state = draw_water()
    else:
        program_state = draw_ice()
        



def keyPressed(event):
    print('keyPressed.. ' + str(p5.key))

def keyReleased(event):
    print('keyReleased.. ' + str(p5.key))

def mousePressed(event):
    print('mousePressed..')

def mouseReleased(event):
    print('mouseReleased..')
