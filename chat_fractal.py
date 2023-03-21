import pygame
import math

# Initialize Pygame
pygame.init()

# Set the screen size
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)

# Set the background color
background_color = (0, 0, 0)

# Set the polygon color
polygon_color = (208, 203, 79)

# Set the color change values
color_change = 7

# Set the polygon sides
sides = 3

# Set the polygon rotation angle
angle = 3.54933836749317

# Set the fractal depth
depth = 1

# Set the fractal scale
scale = 1.3333333333333333

# Define the function to draw the fractal
def draw_fractal(x, y, size, angle, depth):
    # Draw the polygon
    polygon_points = []
    for i in range(sides):
        point_x = x + size * math.cos(math.radians(angle + i * 360 / sides))
        point_y = y + size * math.sin(math.radians(angle + i * 360 / sides))
        polygon_points.append((point_x, point_y))
    pygame.draw.polygon(screen, polygon_color, polygon_points)

    # Recursively draw the fractal
    if depth > 0:
        for i in range(sides):
            new_x = x + size * math.cos(math.radians(angle + i * 360 / sides))
            new_y = y + size * math.sin(math.radians(angle + i * 360 / sides))
            new_size = size * scale
            new_angle = angle + i * 360 / sides
            draw_fractal(new_x, new_y, new_size, new_angle, depth - 1)

# Set the initial position and size of the fractal
start_x = screen_size[0] / 2
start_y = screen_size[1] / 2
start_size = 200

# Draw the fractal
draw_fractal(start_x, start_y, start_size, 0, depth)

# Update the screen
pygame.display.flip()

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Change the polygon color
    polygon_color = tuple((c + color_change) % 255 for c in polygon_color)

    # Redraw the fractal with the new color
    screen.fill(background_color)
    draw_fractal(start_x, start_y, start_size, 0, depth)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
