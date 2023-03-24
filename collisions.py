# Importing necessary modules
from settings import *

# calculate bearing between 2 lines
def calculate_bearing(lat1, lon1, lat2, lon2):
    #Calculates the bearing in degrees from (lat1, lon1) to (lat2, lon2)
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    # relative longitude positions
    delta_lon = lon2 - lon1
    y = math.sin(delta_lon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(delta_lon)
    bearing = math.degrees(math.atan2(y, x))
    return (bearing + 360) % 360

def calculate_reflection_angle(ball_velocity, surface_normal):
    #Calculates the angle of reflection given the velocity of a ball and the surface normal.
    # Calculate the angle of incidence
    incidence_angle = math.atan2(ball_velocity[1], ball_velocity[0])
    
    # Calculate the angle between the incidence angle and the surface normal
    angle_between = math.atan2(surface_normal[1], surface_normal[0]) - incidence_angle
    
    # Calculate the angle of reflection
    reflection_angle = incidence_angle - 2 * angle_between
    
    return reflection_angle

def ballPegCollision(ball, pegs):
    log = ""
    #peg_hit_list = pygame.sprite.spritecollide(ball, pegs, False)
    # GET RELATIVE POSITION OF BALL
    # Treat peg like hex or octogon so that you can have multiple different trajectories off the pin but still keep it predictable and replicable
    for i in pegs:
        if ball.rect.colliderect(i):
            # Work out angle of incident and deflection using lines through the circles
            ballx = ball.rect.x
            bally = ball.rect.y 
            # calculate bearing between ball and the peg
            angle = calculate_bearing(ballx, bally, i.rect.x, i.rect.y)
            # work out approximate location
            if ball.xVel > 0:
                if ball.yVel > 0:
                    pass
                    # print("approx top right")
                else:
                    pass
                    # print("approx bottom right")
            else:
                if ball.yVel > 0:
                    pass
                    # print("approx top left")
                else:
                    pass
                    # print("approx bottom left")
                
            if angle <= 30 or angle >= 330:
                pass
                # print("left")
                pass # Ball from on top
            elif angle < 90:
                pass
                # print("top left")
                pass # ball from top right
            elif angle == 90: # ball from the right
                pass
                # ball.xVel *= -1
                # print("top")
            elif angle < 150:
                pass
                # print("top right")
                pass # ball from bottom right
            elif angle <= 210:
                pass
                # print("bottom right")
                pass # ball from bottom
            elif angle < 270:
                pass
                # print("bottom")
                pass # ball from bottom left
            elif angle == 270: # Ball from the left
                pass
                # ball.xVel *= -1
                # print("bottom")
            elif angle < 330:
                pass
                # print("bottom left")
                pass # top left


            # work out relative location and then log the result and change the relavent velocity 
            if (ballx < i.rect.x and ball.xVel > 0) or (ballx > i.rect.x and ball.xVel < 0):
                log = log + str(i.rect.x) + " " + str(i.rect.y) + " " +  str(round(ball.xVel,3)) + " " +  str(round(ball.yVel,3)) + " "
                ball.xVel = ball.xVel * (-1)       # CHANGE xVel and yVel depending on positions
            elif (bally < i.rect.y and ball.yVel > 0) or (bally > i.rect.y and ball.yVel < 0):
                log = log + str(i.rect.x) + " " +  str(i.rect.y) + " " +  str(round(ball.xVel,3)) + " " +  str(round(ball.yVel,3)) + " "
                ball.yVel = ball.yVel * (-1)       # CHANGE xVel and yVel depending on positions

        # Make new ball trajectory the angle of deflection

    # return string of peg collisions and velcity for fractal
    return log
 
# function to work out the ball and wall collisions
def ballWallCollision(balls):
    for i in balls:
        # bounce off all walls by negating the relavent velocity depending on the wall
        if i.rect.x <= 0:
            if i.xVel < 0:
                i.xVel = i.xVel * (-1)
        elif i.rect.x >= screenWidth:
            if i.xVel > 0:
                i.xVel = i.xVel * (-1)
        # if the ball hits the bottom of the screen then kill it and return true to delete it from the ball list
        if i.rect.y >= screenHeight: 
            i.kill()
            return True
        elif i.rect.y <= 0:
            if i.yVel < 0:
                i.yVel = i.yVel * (-1)
    return False

# ball paddle collisions
def ballPaddleCollision():
    pass