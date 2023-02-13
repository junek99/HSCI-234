import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.background(255)           # white background
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 20)

    p5.fill(120,90,65)#fill with brown
    p5.ellipse(98,122,60,80)
    p5.ellipse(171,60,15,20) 
    p5.triangle(260,175,282,173,253,201)
    p5.quad(104,204,122,237,139,256,105,256)# filling blanks

    p5.line(94,172,107,240)
    p5.arc(106,257,20,35,3.14,4.71)
    p5.line(97,257,110,257) #Rabbit Front Leg R

    p5.arc(264,186,40,50,5.65,1.73)
    p5.line(253,177,282,173)#Rabbit Tail

    p5.strokeWeight (1.5)
    p5.fill(120,90,65) #fill with brown
    p5.ellipse(175,182,170,125) #Rabbit Body

    p5.strokeWeight (1.5)
    p5.ellipse(215,220,110,85)
    p5.rect(172,227,35,35)
    p5.stroke(120,90,65) #brown stroke
    p5.rect(201,220,23,41)
    p5.stroke(0) #black stoke
    p5.arc(173,262,40,70,3.14,4.71)
    p5.line(153,262,173,262)
    p5.arc(222,196,85,120,5.03,0.16) #Rabbit Back Leg
    p5.line(199,262,224,262)

    p5.strokeWeight (1.5)
    p5.rect(118,185,30,75)
    p5.arc(124,185,35,120,1.54,2.51)
    p5.stroke(120,90,65) #brown stroke
    p5.rect(114,176,32,41)
    p5.stroke(0) #black stroke
    p5.arc(119,261,20,35,3.14,4.71)
    p5.line(110,260,119,260) #Rabbit Front Leg L

    p5.strokeWeight (1.5)
    p5.stroke(0) #black stoke
    p5.quad(98,39,128,36,114,80,95,77)
    p5.arc(109,40,40,55,5.34,1.17)
    p5.arc(113,48,35,65,2.5,5.05) #Rabbit Ear L
    p5.quad(160,54,188,72,139,92,116,83)
    p5.arc(170,56,80,35,5.85,0.73)
    p5.stroke(120,90,65) #brown stoke
    p5.quad(163,53,187,70,174,75,159,57)
    p5.stroke(0) #black stoke
    p5.arc(197,61,80,35,3.3,4.7) #Rabbit Ear R

    p5.fill(120,90,65)#fill with brown
    p5.stroke(0) #black stoke
    p5.strokeWeight (1.5)
    p5.arc(90,120,80,90,1.1,5.5) 
    p5.arc(104,125,90,75,5.12,1.57)
    p5.arc(80,132,80,70,1.22,3.87)
    p5.arc(96,110,100,70,4.08,6.34) #Rabbit Face

    p5.strokeWeight (1)
    p5.fill(0) #fill with black
    p5.triangle(45,134,64,137,53,144) #Rabbit Nose
    p5.ellipse(56,109,8,15)
    p5.ellipse(90,115,10,15)

    p5.fill(255) #fill with black
    p5.ellipse(57,106,3,4)
    p5.ellipse(92,113,4,5) #Rabbit Eyes

    for i in range(5):
        x = 103 + i*6
        y = 158 - i*3
        d=20
        p5.fill(120,90,65)
        p5.arc(x,y,d,d,6.13,1.1)

    for i in range(5):
        x = 215 + i*8
        y = 211
        d=20
        p5.fill(120,90,65)
        p5.arc(x,y,d,d,1.1,2.9)

    for i in range(5):
        x = 97 + i*1.5
        y = 178 + i*4
        d=20
        p5.fill(120,90,65)
        p5.arc(x,y,d,d,1.8,4)

    for i in range(5):
        x = 135 + i*2
        y = 210 - i*6
        d=25
        p5.fill(120,90,65)
        p5.arc(x,y,d,d,5.8,1.1) # furs
