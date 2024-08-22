import random

from elements import Boundary, Particle
import pygame
from pygame.locals import *
import sys

# Initial conditions
WIDTH = 1000
HEIGHT = 800
screen_colour = (0, 0, 0)
line_colour = (255, 255, 255)
line_width = 3
num_walls = 10
num_rays = 100
# TODO make the source wiggle gently around the cursor, or like it follows it slowly
# x_noise = 0.5
# y_noise = 0.1

# Instantiate elements
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
main_clock = pygame.time.Clock()
walls = [0] * num_walls
for i, wall in enumerate(walls):
    wall_elements = Boundary.wall_maker(WIDTH, HEIGHT)
    walls[i] = Boundary(window, wall_elements[0], wall_elements[1], wall_elements[2], wall_elements[3], line_colour, line_width)

# Add boundaries to the edges
walls.append(Boundary(window, 0, 0, WIDTH, 0, line_colour, width=0))
walls.append(Boundary(window, 0, HEIGHT, 0, 0, line_colour, width=0))
walls.append(Boundary(window, WIDTH, HEIGHT, 0, HEIGHT, line_colour, width=0))
walls.append(Boundary(window, WIDTH, 0, WIDTH, HEIGHT, line_colour, width=0))

# Game loop -------------------------
run = True
while run:
    # Draw --------------------------
    # TODO experiment with other colourations
    window.fill(screen_colour)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    particle = Particle(window, mouse_x, mouse_y, line_colour, num_rays)
    particle.update(mouse_x, mouse_y)
    for i, wall in enumerate(walls):
        walls[i].show()
    particle.look(walls)
    particle.show(show_point=True, show_rays=False)

    # Run ----------------------------
    pygame.display.update()
    main_clock.tick(600)

    # Buttons ------------------------
    for event in pygame.event.get():
        # TODO make it so there is mouse acceleration, and maybe asteroid - mapping
        if event.type == MOUSEBUTTONDOWN:
            pygame.quit()
            sys.exit()
