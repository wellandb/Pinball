from settings import *
from peg import *

# Board Generation
pegs = pygame.sprite.Group()

def drawLine(pegs, number, start, end):
    changeX = int((end[0]-start[0]))/number
    changeY = int((end[1]-start[1]))/number
    for i in range(number):
        pegs.add(peg((start[0])+(i*(changeX)), (start[1])+(i*(changeY)), 7, WHITE))

def drawShape(pegs, number, start, shape):
    pass

def drawDiamond(p):
    drawLine(p, 20, [screenWidth/2, 0], [0, screenHeight/2])
    drawLine(p, 20, [screenWidth/2, 0], [screenWidth, screenHeight/2])
    drawLine(p, 20, [screenWidth/2, screenHeight], [0, screenHeight/2])
    drawLine(p, 20, [screenWidth/2, screenHeight], [screenWidth, screenHeight/2])

def board1():
    for j in range(5):
        drawLine(pegs, 15-(abs(2-j)*2), [150 + abs(2-j)*50, 200+ 50*j], [screenWidth-(150 + abs(2-j)*50), 200+ 50*j])
    
    drawDiamond(pegs)

for j in range(5):
    drawLine(pegs, 15-(abs(2-j)*2), [150 + abs(2-j)*50, 200+ 50*j], [screenWidth-(150 + abs(2-j)*50), 200+ 50*j])

drawDiamond(pegs)
