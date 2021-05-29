class Circle:
    def __init__(self ,color_,x,y):
        self.x = x
        self.y = y
        self.color_ = color_
    def draw_(self):
        fill(255,0,0)
        if self.color_:
            fill(0,255,0)
        circle(self.x , self.y , 30)
        
fc=0
sc=0
x=0
zn=0
y=0
state = 3
time=0
res=0
win=0
level=1

raund=[]

y_next = 1
x_next = 2

def setup():
    size(800,500)
    background("#38B2CE")
    textSize(70)
    frameRate(60)
    
def draw():
    global x,fc,sc,zn,y,state,time, level, res,x_next
    #time=time+1/60
    background("#38B2CE")
    fill(255)
    rect(215,290,300,70)
    
    fill(0)
    
    if state==3:
        background("#38B2CE")
        textSize(60)
        text('Math game',240,100)
        fill(255)
        rect(250,150,300,70)
        rect(250,250,300,70)
        rect(250,350,300,70)
        fill(0)
        text('Easy',330,205)
        text('Normal',300,305)
        text('Hard',330,400)
        textSize(40)
        text('level ' + str(level),650,100)
        if mouseX>250 and mouseX<550 and mouseY>150 and mouseY<220 and mousePressed:
            level=1
        elif mouseX>250 and mouseX<550 and mouseY>250 and mouseY<320 and mousePressed:
            level=2
        elif mouseX>250 and mouseX<550 and mouseY>350 and mouseY<420 and mousePressed:
            level=3
        while len(raund)!=0:
            del raund[0]
        
    
    if state == 0:
        if level==1:
            fc=floor(random(15,25))
            sc=floor(random(1,10))
        if level==2:
            fc=floor(random(25,35))
            sc=floor(random(7,20))
        if level==3:
            fc=floor(random(45,55))
            sc=floor(random(15,40))
        zn=floor(random(1,4))
        if zn==1:
            x=fc+sc
        elif zn==2:
            x=fc-sc
        elif zn==3:
            x=fc*sc
        state = 1
        
    if state == 1:
        if zn==1:
            text(str(fc)+ ' + ' + str(sc) , 250,250)
        elif zn==2:
            text(str(fc)+ ' - ' + str(sc) , 250,250)
        elif zn==3:
            text(str(fc)+ ' * ' + str(sc),250,250)
            
        text(y,250,350)
        textSize(40)
        text('round '+ str(res),570,120)
        textSize(70)
    
    if res>=15:
        x_next = 2
        y_next = 1
        state = 2
    if state == 2:
        background("#38B2CE")
        textSize(60)
        text('your result:' + str(win),200,250)
        textSize(70)
        if y==2007:
            textSize(40)
            text(';)',100,370)
    if state==2 and key==' ':
        state=3
        res=0
    if state==1:
        for circ in raund:
            circ.draw_()

def keyPressed():
    global y,x,res,state,win,x_next,y_next
    #if key >= '0' and key <= '9':
    #print(int(key))
    if key >= '0' and key <= '9' and y<=99999:
        y=10*y+int(key)
        
        
    if state==3 and key==ENTER:
        state=0
    elif key==ENTER and y==x and res<15:    
        raund.append(Circle(True,x_next*40,y_next*40))    
        x_next+= 1    
        state = 0
        res=res+1
        win=win+1
        y=0
        
    elif key==ENTER and y!=x and res<15:
        raund.append(Circle(False , x_next*40,y_next*40))
        x_next+=1
        state = 0
        res=res+1
        y=0
        
    elif key==BACKSPACE:
        y=y/10
        
