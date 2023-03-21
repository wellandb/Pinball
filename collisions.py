from settings import *

def calculate_bearing(lat1, lon1, lat2, lon2):
    """Calculates the bearing in degrees from (lat1, lon1) to (lat2, lon2)."""
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    delta_lon = lon2 - lon1
    y = math.sin(delta_lon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(delta_lon)
    bearing = math.degrees(math.atan2(y, x))
    return (bearing + 360) % 360

def calculate_reflection_angle(ball_velocity, surface_normal):
    """Calculates the angle of reflection given the velocity of a ball and the surface normal."""
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
            angle = calculate_bearing(ball.rect.x, ball.rect.y, i.rect.x, i.rect.y)
            print(angle)
            if ball.xVel > 0:
                if ball.yVel > 0:
                    print("approx top right")
                else:
                    print("approx bottom right")
            else:
                if ball.yVel > 0:
                    print("approx top left")
                else:
                    print("approx bottom left")
                
            if angle <= 30 or angle >= 330:
                print("left")
                pass # Ball from on top
            elif angle < 90:
                print("top left")
                pass # ball from top right
            elif angle == 90: # ball from the right
                print("top")
                ball.xVel *= -1
            elif angle < 150:
                print("top right")
                pass # ball from bottom right
            elif angle <= 210:
                print("bottom right")
                pass # ball from bottom
            elif angle < 270:
                print("bottom")
                pass # ball from bottom left
            elif angle == 270: # Ball from the left
                print("bottom")
                ball.xVel *= -1
            elif angle < 330:
                print("bottom left")
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
        if i.rect.x <= 0:
            if i.xVel < 0:
                i.xVel = i.xVel * (-1)
        elif i.rect.x >= screenWidth:
            if i.xVel > 0:
                i.xVel = i.xVel * (-1)
        if i.rect.y >= screenHeight:
            i.kill()
            return True
        elif i.rect.y <= 0:
            if i.yVel < 0:
                i.yVel = i.yVel * (-1)
    return False

def ballPaddleCollision():
    pass