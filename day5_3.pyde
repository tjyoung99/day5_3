xCoordinate = random(115, 200)
yCoordinate = random(115, 200)
speed = 2
ySpeed = 1
ellipseSize = 20

def setup():
    size(400, 400)

def draw():
    background(0)
    global xCoordinate, yCoordinate, ySpeed, speed, ellipseSize
    leftTopBoundary =ellipseSize / 2
    rightBottomBoundary = 400 - ellipseSize / 2
    
    if xCoordinate >= rightBottomBoundary or xCoordinate <= leftTopBoundary:
        print("a")
        speed = -speed
    if yCoordinate >= rightBottomBoundary or yCoordinate <= leftTopBoundary:
        print("b")
        ySpeed = -ySpeed
    if yCoordinate <= 75:
        print("c")
        ySpeed=-ySpeed
        

    xCoordinate += speed
    yCoordinate += ySpeed
    fill(255, 255, 0)
    ellipse(xCoordinate, yCoordinate, ellipseSize, ellipseSize)
