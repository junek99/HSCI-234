import js
p5 = js.window

program_timer = p5.millis()
program_state = 'state1'
x=0
speed = 0.75

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

def draw_something():
    p5.push()
    p5.translate(120,165)
    p5.ellipse(0,0,100,100)
    p5.pop()


def draw():
    p5.background(255)           
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)

    global program_state, program_timer

    msec = p5.millis()  
    sec = int(msec / 1000) 
    p5.fill(0)
    p5.text('milliseconds: ' + str(msec), 10, 20)
    p5.text('seconds: ' + str(sec), 10, 35)

    if program_state == 'state1':
        draw_ice()
    elif program_state == 'state2':
        draw_water()
    elif program_state == 'state3':
        draw_something()

    # Check if it is time to switch to state 2
    if program_state == 'state1' and msec - program_timer > 2000:
        program_state = 'state2'
        program_timer = msec

def keyPressed(event):
    global program_state, program_timer
    if p5.key == '1':
        program_state = 'state1'
        program_timer = p5.millis()
    elif p5.key == '2':
        program_state = 'state2'
        program_timer = p5.millis()
    elif p5.key == '3':
        program_state = 'state3'
        program_timer = p5.millis()

def keyReleased(event):
    pass

def mousePressed(event):
    global program_state,x,speed
    if program_state == 'state1':
        program_state = 'state3'
    elif program_state == 'state2':
        program_state = 'state3'

    if program_state == 'state3':
        draw_something()
