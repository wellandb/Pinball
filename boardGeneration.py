from settings import *
from peg import *

# Board Generation

def drawLine(pegs, number, start, end):
    changeX = int((end[0]-start[0]))/number
    changeY = int((end[1]-start[1]))/number
    for i in range(number):
        pegs.add(peg((start[0])+(i*(changeX)), (start[1])+(i*(changeY)), 7, WHITE))

def drawShape(pegs, number, start, shape):
    pass

def drawDiamond(p,width, height, x, y):
    number = int(math.sqrt((width/2)**2+(height/2)**2)/30)
    drawLine(p, number, [x, y], [x+width/2, y+height/2])
    drawLine(p, number, [x+width/2, y+height/2], [x+width, y])
    drawLine(p, number, [x+width, y], [x+width/2, y-height/2])
    drawLine(p, number, [x+width/2, y-height/2], [x, y])

def board1():
    pegs = pygame.sprite.Group()
    for j in range(5):
        drawLine(pegs, 15-(abs(2-j)*2), [150 + abs(2-j)*50, 200+ 50*j], [screenWidth-(150 + abs(2-j)*50), 200+ 50*j])
    
    drawDiamond(pegs, screenWidth, screenHeight, 0, screenHeight/2)
    return pegs

def board2():
    pegs = pygame.sprite.Group()
    for i in range(10):
        for j in range(8):
            drawLine(pegs, int(screenWidth/50), [20+10*i%2, 100+50*j], [screenWidth-20-10*i%2, 100+50*j])
    return pegs

def board3():
    pegs = pygame.sprite.Group()
    width = screenWidth
    height = screenHeight
    for i in range(3):
        drawDiamond(pegs,width,height, i*100, screenHeight/2)
        width -= 200
        height -= 200

    return pegs

def get_boards():
    boards = [board1, board2, board3]
    return boards
