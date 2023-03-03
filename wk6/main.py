import js
p5 = js.window

program_timer = p5.millis()
program_state = 'state1'

def setup():
    p5.createCanvas(300, 300)  
    print('finished setup..')

def draw_grenade():
    p5.push()
    p5.translate(146,150)
    p5.stroke(0)
    p5.ellipse(35,-55,38,38)
    p5.fill(255)
    p5.ellipse(35,-55,33,33)
    p5.fill(49,56,69)
    p5.stroke(49,56,69)
    p5.ellipse(4,0,100,100)
    p5.rect(-10,-70,30,80)
    p5.stroke(0)
    p5.rotate(p5.radians(46))
    p5.rect(-65,-70,30,34)
    p5.rotate(p5.radians(90))
    p5.rect(-70,10,13,45)
    p5.pop()



def draw_grenade_ex():
    p5.push()
    p5.translate(146,150)
    p5.stroke(250,190,0)
    p5.fill(250,190,0)
    p5.ellipse(35,-55,38,38)
    p5.fill(255)
    p5.ellipse(35,-55,33,33)
    p5.fill(250,0,0)
    p5.stroke(250,109,0)
    p5.ellipse(4,0,100,100)
    p5.fill(250,109,0)
    p5.ellipse(4,0,80,80)
    p5.rect(-10,-70,30,80)
    p5.stroke(250,190,0)
    p5.rotate(p5.radians(46))
    p5.rect(-65,-70,30,34)
    p5.rotate(p5.radians(90))
    p5.rect(-70,10,13,45)
    p5.pop()

def draw_something():
    p5.push()
    p5.translate(150,150)
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
        draw_grenade()
    elif program_state == 'state2':
        draw_grenade_ex()
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
    global program_state
    if program_state == 'state1':
        program_state = 'state3'
    elif program_state == 'state2':
        program_state = 'state3'
