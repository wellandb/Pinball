# Import necessary modules and classes
from settings import * # initialize the settings and window
from ball import *
from paddle import *
from peg import *
from collisions import *
import math
import boardGeneration
import log_to_fractal
import time

# Define the function for redrawing the game window
def redrawGameWindow(bkg,balls,pegs):
    win.fill(BLACK) # fill the screen with black
    win.blit(bkg, (0,0)) # place the background on the screen
    for i in pegs: # draw all the pegs
       i.draw(win)
    for i in balls: # draw the balls
        i.draw(win)
        i.move()

# main function run that takes in the board function and starts the pinball simulation
def main(board):
    pegs = board() # run the board function to get the pegs

    # Function to get ball x and y values from mouse click
    def mouseClick():
        ballX = mouse[0]
        ballY = mouse[1]
        return ballX, ballY

    # Function to get ball x velocity and y velocity from second mouse click
    def mouseClick2():
        weight = 10/math.sqrt((mouse[0]-ballX)**2 + (mouse[1] - ballY)**2)
        ballXVel = (mouse[0]-ballX)*weight
        ballYVel = (mouse[1] - ballY)*weight
        return ballXVel, ballYVel

    # Initialization
    win.fill(BLACK)

    # get background based off of the board chosen
    if board == boardGeneration.board1:
        bkg = pygame.image.load("img/neon_L.jpg")
    elif board == boardGeneration.board2:
        bkg = pygame.image.load("img/galaxy_fractal.png")
    elif board == boardGeneration.board3:
        bkg = pygame.image.load("img/pixel_sky_bkgs/nightbackgroundwithmoon.png")
    # fit the background to the screen
    bkg_fit = pygame.transform.scale(bkg, (screenWidth,screenHeight))
    win.blit(bkg_fit, (0,0)) # draw the background

    for i in pegs: # draw the pegs
        i.draw(win)

    balls = pygame.sprite.Group() # create a group to store the balls

    # First loop to get starting parameters
    run = True
    # sleep so that previous inputs don't affect the ball starting position
    time.sleep(0.2)
    while run:

        clock.tick(30) # frame rate

        # get mouse position
        mouse = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed() # get current state of keyboard

        # if k is pressed then input the parameters you want into the terminal
        if keys[pygame.K_k]:
            ballX = float(input("type ball x value from 0 to " + str(screenWidth)+": "))
            ballY = float(input("type ball y value from 0 to " + str(screenHeight)+": "))
            run = False
        # if keys[pygame.K_SPACE]:
        #     ballX, ballY = mouseClick()
        #     f.write(str(ballX) +  " "  + str(ballY))
        #     run = False

        # get events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if close then stop run through
                run = False
            # if mouse click then set ball start position
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ballX, ballY = mouseClick()
                run = False
        
        # redraw the game window
        redrawGameWindow(bkg_fit, balls, pegs)
        # draw the controls onto the screen
        win.blit(smallfont.render('To type parameters press k', True, WHITE), (screenWidth - 300, screenHeight-50))
        pygame.display.update() # display the updates of the screen

        
    # second loop to get the ball velocity
    while not run:
        clock.tick(30) # frame rate

        mouse = pygame.mouse.get_pos() # get mouse position
        keys = pygame.key.get_pressed() # get keyboard states
        if keys[pygame.K_SPACE]: # if space is pressed then act as if mouse has been clicked
            ballXVel, ballYVel = mouseClick2()
            run = True

        if keys[pygame.K_k]: # if k is pressed then allow entering of parameters into terminal
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
            i.draw(win)
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

    # log for route tracker to give to the fractal
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