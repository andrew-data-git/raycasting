import pygame
import numpy as np
import random as rd
from ray import Ray
import math


class Boundary:

    def __init__(self, surface, x1, x2, y1, y2, line_colour, width=5):
        self.surface = surface
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.line_colour = line_colour
        self.a, self.b = (self.x1, self.x2), (self.y1, self.y2)
        self.width = width

    def show(self):
        # Draw the boudary line
        pygame.draw.line(self.surface,
                         self.line_colour,
                         self.a, self.b,
                         self.width)

    @staticmethod
    def wall_maker(screen_width, screen_height, padding=0):
        x_ext1 = rd.randint(padding, screen_width - padding)
        x_ext2 = rd.randint(padding, screen_width - padding)
        y_ext1 = rd.randint(padding, screen_height - padding)
        y_ext2 = rd.randint(padding, screen_height - padding)
        return x_ext1, x_ext2, y_ext1, y_ext2


class Particle:

    def __init__(self, surface, x, y, line_colour, num_rays=36):
        self.surface = surface
        self.num_rays = num_rays
        self.pos = x, y
        self.line_colour = line_colour
        # Vector of num_rays length to populate with rays
        self.rays = [None] * self.num_rays
        for i in range(0, self.num_rays):
            # Deduce angle from num_rays
            angle = (360 / self.num_rays) * i
            angle = np.deg2rad(angle)
            self.rays[i] = Ray(self.surface, self.pos, angle, self.line_colour)

    def show(self, show_point=False, show_rays=False):
        # Draw all rays
        if show_rays:
            for _, ray in enumerate(self.rays):
                ray.show()

        if show_point:
            # Draw a point for centre of particle
            rect = (self.pos[0] - 5, self.pos[1] - 5, 10, 10)
            pygame.draw.ellipse(self.surface, "red", rect, width=5)

    def update(self, mouse_x, mouse_y):
        self.pos = (mouse_x, mouse_y)

    def look(self, walls):
        # Cast each ray, to see if collision with a boundary
        for _, ray in enumerate(self.rays):
            closest = None
            record = np.inf
            for wall in walls:
                pt = ray.cast(wall)
                if pt:
                    dist = math.dist(self.pos, pt)
                    if dist < record:
                        record = dist
                        closest = pt
            if closest:
                # TODO change the colour to reflect the distance!
                pygame.draw.line(surface=self.surface,
                                 color=self.line_colour,
                                 start_pos=(self.pos[0], self.pos[1]),
                                 end_pos=(closest[0], closest[1])
                                 )
