from settings import *

def ballPegCollision(ball, pegs):
    log = ""
    #peg_hit_list = pygame.sprite.spritecollide(ball, pegs, False)
    # GET RELATIVE POSITION OF BALL
    # Treat peg like hex or octogon so that you can have multiple different trajectories off the pin but still keep it predictable and replicable
    for i in pegs:
        if pygame.sprite.collide_circle(ball, i):
            

            # Work out angle of incident and deflection using lines through the circles
            angle = math.degrees(math.atan(float(ball.xVel)/float(ball.yVel)))
            if angle < 0:
                angle  = 360 + angle
            if angle <= 30 or angle >= 330:
                pass # Ball from on top
            elif angle < 90:
                pass # ball from top right
            elif angle == 90: # ball from the right
                ball.xVel *= -1
            elif angle < 150:
                pass # ball from bottom right
            elif angle <= 210:
                pass # ball from bottom
            elif angle < 270:
                pass # ball from bottom left
            elif angle == 270: # Ball from the left
                ball.xVel *= -1
            elif angle < 330:
                pass # top left


            
            if (ball.rect.x < i.rect.x and ball.xVel > 0) or (ball.rect.x > i.rect.x and ball.xVel < 0):
                log = log + str(i.rect.x) + " " + str(i.rect.y) + " " +  str(round(ball.xVel,3)) + " " +  str(round(ball.yVel,3)) + " "
                ball.xVel = ball.xVel * (-1)       # CHANGE xVel and yVel depending on positions
            elif (ball.rect.y < i.rect.y and ball.yVel > 0) or (ball.rect.y > i.rect.y and ball.yVel < 0):
                log = log + str(i.rect.x) + " " +  str(i.rect.y) + " " +  str(round(ball.xVel,3)) + " " +  str(round(ball.yVel,3)) + " "
                ball.yVel = ball.yVel * (-1)       # CHANGE xVel and yVel depending on positions

        # Make new ball trajectory the angle of deflection

    # return string of peg collisions and velcity for fractal
    return log
 

def ballWallCollision(balls):
    for i in balls:
        if i.rect.x <= 0 or i.rect.x >= screenWidth:
            i.xVel = i.xVel * (-1)
        if i.rect.y >= screenHeight:
            i.kill()
        elif i.rect.y <= 0:
            i.yVel = i.yVel * (-1)

def ballPaddleCollision():
    pass