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


def main(board):
    pegs = board()
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

    if board == boardGeneration.board1:
        bkg = pygame.image.load("img/neon_L.jpg")
    elif board == boardGeneration.board2:
        bkg = pygame.image.load("img/galaxy_fractal.png")
    elif board == boardGeneration.board3:
        bkg = pygame.image.load("img/pixel_sky_bkgs/nightbackgroundwithmoon.png")
    bkg_fit = pygame.transform.scale(bkg, (screenWidth,screenHeight))
    win.blit(bkg_fit, (0,0))

    for i in pegs:
        i.draw()

    balls = pygame.sprite.Group()

    # First loop to get starting parameters
    run = True
    time.sleep(0.2)
    while run:

        clock.tick(30)

        mouse = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_k]:
            ballX = float(input("type ball x value from 0 to " + str(screenWidth)+": "))
            ballY = float(input("type ball y value from 0 to " + str(screenHeight)+": "))
            run = False
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
                run = False
        
        redrawGameWindow(bkg_fit, balls, pegs)
        win.blit(smallfont.render('To type parameters press k', True, WHITE), (screenWidth - 300, screenHeight-50))
        pygame.display.update()

        
    # second loop to get the ball velocity
    while not run:
        clock.tick(30)

        mouse = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            ballXVel, ballYVel = mouseClick2()
            run = True

        if keys[pygame.K_k]:
            ballXVel = float(input("type ball x velocity value from -10 to 10: "))
            print(" The velocity is weighted so the y Velocity is more to choose direction.")
            ballYVel = float(input("type ball y velocity value from -10 to 10: "))
            if ballYVel < 0:
                ballYVel= -math.sqrt(100-ballXVel**2)
            else:
                ballYVel = math.sqrt(100-ballXVel**2)
            run = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ballXVel, ballYVel = mouseClick2()
                run = True

        win.fill(BLACK)

        redrawGameWindow(bkg_fit, balls, pegs)
        for i in pegs:
            i.draw()
        if abs(mouse[0]) < screenWidth and abs(mouse[1]) <screenHeight:
            pygame.draw.line(win, WHITE, [ballX, ballY], mouse)
        pygame.draw.circle(win, WHITE, [ballX, ballY], 5)
        win.blit(smallfont.render('To type parameters press k', True, WHITE), (screenWidth - 300, screenHeight-50))
        
        pygame.display.update()

    # save parameters to file
    f = open("parameter_log.txt", "a")
    # close the file
    f.write(str(ballX) +  " "  + str(ballY))
    f.write(" " + str(ballXVel) + " " + str(ballYVel) + "\n")
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
        pygame.display.update()


    log.write("\n")
    log.close()
    log_to_fractal.main()