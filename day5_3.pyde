xCoordinate = 200
yCoordinate = 200
speed = 3
ySpeed =3
ellipseSize = 20

def setup():
    size(400, 400)

def draw():
    background(0)
    global xCoordinate, yCoordinate, ySpeed, speed, ellipseSize
    leftTopBoundary =ellipseSize / 2
    rightBottomBoundary = 400 - ellipseSize / 2
    brick= 50+ ellipseSize/2
    
    if xCoordinate >= rightBottomBoundary or xCoordinate <= leftTopBoundary:
        print("a")
        speed = -speed
    if yCoordinate >= rightBottomBoundary or yCoordinate <= leftTopBoundary:
        print("b")
        ySpeed = -ySpeed
    if yCoordinate < brick and xCoordinate< 100:
        print("1")
        ySpeed=-ySpeed
    elif yCoordinate < brick and xCoordinate< 200:
        print("2")
        ySpeed=-ySpeed
    elif yCoordinate < brick and xCoordinate< 300:
        print("3")
        ySpeed=-ySpeed
    elif yCoordinate < brick and xCoordinate< 400:
        print("4")
        ySpeed=-ySpeed


    xCoordinate += speed
    yCoordinate += ySpeed
    fill(255, 255, 0)
    ellipse(xCoordinate, yCoordinate, ellipseSize, ellipseSize)
    rect(0,0,100,50)
    rect(100,0,100,50)
    rect(200,0,100,50)
    rect(300,0,100,50)
