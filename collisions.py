from settings import *

def ballPegCollision(ball, pegs):
    #peg_hit_list = pygame.sprite.spritecollide(ball, pegs, False)
    # GET RELATIVE POSITION OF BALL
    for i in pegs:
        if pygame.sprite.collide_circle(ball, i):
            if (ball.rect.x < i.rect.x and ball.xVel > 0) or (ball.rect.x > i.rect.x and ball.xVel < 0):
                ball.xVel = ball.xVel * (-1)       # CHANGE xVel and yVel depending on positions
            elif (ball.rect.y < i.rect.y and ball.yVel > 0) or (ball.rect.y > i.rect.y and ball.yVel < 0):
                ball.yVel = ball.yVel * (-1)       # CHANGE xVel and yVel depending on positions

        # Work out angle of incident and deflection using lines through the circles
        # Make new ball trajectory the angle of deflection
 

def ballWallCollision(balls):
    for i in balls:
        if i.rect.x <= 0 or i.rect.x >= screenWidth:
            i.xVel = i.xVel * (-1)
        if i.rect.y >= screenHeight:
            i.rect.y = 0
        elif i.rect.y <= 0:
            i.yVel = i.yVel * (-1)

def ballPaddleCollision():
    pass