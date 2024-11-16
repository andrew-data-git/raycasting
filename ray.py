import pygame
import numpy as np


class Ray:
    def __init__(self, surface, pos, angle, line_colour, width=1):
        self.surface = surface
        self.pos = pos
        self.dir = [np.sin(angle), np.cos(angle)]
        self.line_colour = line_colour
        self.width = width

    def show(self):
        # Draw a line of length x on the canvas in direction dir
        x = 30
        line = np.add(self.pos, np.multiply(self.dir, x))
        pygame.draw.line(self.surface,
                         self.line_colour,
                         self.pos,
                         line,
                         self.width*2)

    def return_ray(self):
        return self.pos

    def cast(self, boundary):
        # Cast a ray along direction dir
        # Using line-line intersection, if intersection return coordinate, otherwise None
        x1 = boundary.a[0]
        y1 = boundary.a[1]
        x2 = boundary.b[0]
        y2 = boundary.b[1]

        x3 = self.pos[0]
        y3 = self.pos[1]
        x4 = self.pos[0] + self.dir[0]
        y4 = self.pos[1] + self.dir[1]

        den = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
        if den == 0:
            return

        t = np.divide((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4), den)
        u = - np.divide((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3), den)

        if 0 < t < 1 and u > 0:
            x_int = x1 + t*(x2 - x1)
            y_int = y1 + t*(y2 - y1)
            return x_int, y_int  # Return the point of intersection given above criteria

        else:
            return
