from settings import *
from ball import *
from paddle import *
from peg import *
from collisions import *
import math
import boardGeneration
import log_to_fractal
import time

def redrawGameWindow(bkg,balls,pegs):
    win.fill(BLACK)
    win.blit(bkg, (0,0))
    for i in pegs:
       i.draw()
    for i in balls:
        i.draw()
        i.move()
    pygame.display.update()


def main(board):
    pegs = board
    def mouseClick():
        ballX = mouse[0]
        ballY = mouse[1]
        return ballX, ballY

    def mouseClick2():
        weight = 10/math.sqrt((mouse[0]-ballX)**2 + (mouse[1] - ballY)**2)
        ballXVel = (mouse[0]-ballX)*weight
        ballYVel = (mouse[1] - ballY)*weight
        return ballXVel, ballYVel

    # Initialization
    win.fill(BLACK)

    bkg = pygame.image.load("img/neon_L.jpg")
    bkg_fit = pygame.transform.scale(bkg, (screenWidth,screenHeight))
    win.blit(bkg_fit, (0,0))

    for i in pegs:
        i.draw()

    balls = pygame.sprite.Group()
    # save parameters to file
    f = open("parameter_log.txt", "a")

    # First loop to get starting parameters
    run = True
    time.sleep(0.2)
    while run:

        clock.tick(30)

        mouse = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     ballX, ballY = mouseClick()
        #     f.write(str(ballX) +  " "  + str(ballY))
        #     run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # if mous click then set ball start position
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ballX, ballY = mouseClick()
                f.write(str(ballX) +  " "  + str(ballY))
                run = False
        
        redrawGameWindow(bkg_fit, balls, pegs)
        pygame.display.update()

        
    # second loop to get the ball velocity
    while not run:
        clock.tick(30)

        mouse = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            ballXVel, ballYVel = mouseClick2()
            f.write(" " + str(ballXVel) + " " + str(ballYVel) + "\n")
            run = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ballXVel, ballYVel = mouseClick2()
                f.write(" " + str(ballXVel) + " " + str(ballYVel) + "\n")
                run = True

        win.fill(BLACK)

        redrawGameWindow(bkg_fit, balls, pegs)
        for i in pegs:
            i.draw()
        pygame.draw.circle(win, WHITE, [ballX, ballY], 5)
        pygame.draw.line(win, WHITE, [ballX, ballY], mouse)
        
        pygame.display.update()

    # close the file
    f.close()

    # create ball
    balls.add(ball(ballX, ballY, ballXVel, ballYVel)) # x, y, xVel, yVel: ALL NEED TO BE CHOSEN EACH RUN AT START

    log = open("route_tracker.txt", "a")
    #mainloop
    run = True
    while run:

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     pause= True
        #     while pause:
        #         leys = pygame.key.get_pressed()
        #         if leys[pygame.K_SPACE]:
        #             pause = False


        # COLLISION CHECK
        for i in balls:      
            log.write(ballPegCollision(i, pegs))
        if ballWallCollision(balls):
            run = False

        redrawGameWindow(bkg_fit, balls,pegs)


    log.write("\n")
    log.close()
    log_to_fractal.main()