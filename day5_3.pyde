xCoordinate = 200
yCoordinate = 200
speed = 1
ySpeed =1
ellipseSize = 20
brick= 50+ ellipseSize/2
hit1= yCoordinate >= brick and yCoordinate <= brick + 5  and xCoordinate< 100 and xCoordinate>0
hit2=yCoordinate == brick and xCoordinate< 200 and xCoordinate>100
hit3=yCoordinate == brick and xCoordinate< 300 and xCoordinate>200
hit4=yCoordinate == brick and xCoordinate< 400 and xCoordinate>300
nohit1= yCoordinate>brick
nohit2= yCoordinate>brick
nohit3= yCoordinate>brick 
nohit4= yCoordinate>brick
def setup():
    size(400, 400)

def draw():
    background(0)
    global xCoordinate, yCoordinate, ySpeed, speed, ellipseSize,hit1,hit2,hit3,hit4,nohit1,nohit2,nohit3,nohit4, brick
    leftTopBoundary =ellipseSize / 2 
    rightBottomBoundary = 400 - ellipseSize / 2
    if xCoordinate >= rightBottomBoundary or xCoordinate <= leftTopBoundary:
        speed = -speed
    if yCoordinate >= rightBottomBoundary or yCoordinate <= leftTopBoundary:
        ySpeed = -ySpeed
    if hit1:
        hit1 = True
        nohit1= False
        fill(0, 7, 68)
        rect(0,0,100,50)
    if nohit1:
        fill(255,0,0)
        rect(0,0,100,50)
    
        
    
    
    
    
   


    xCoordinate += speed
    yCoordinate += ySpeed
    fill(255, 255, 0)
    ellipse(xCoordinate, yCoordinate, ellipseSize, ellipseSize)
    
