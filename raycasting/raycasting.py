### This is a raycasting program I made with Python using pygame.
### Insert the coordinates of the points and data for the edges and render!

import pygame
import pygame.gfxdraw

coordinates = []
edges = []
color = (255, 255, 255)

with open("coordinates.txt", "r") as file:
    for line in file:
        coordinates.append(line)

with open("edges.txt", "r") as file:
    for line in file:
        edges.append(line)

def cast(xcor, ycor, zcor, camDistance):
    x = round((xcor * camDistance) / (zcor + camDistance))
    y = round((ycor * camDistance) / (zcor + camDistance))
    return (x, y)

pygame.init()
pygame.display.set_mode((800, 800))

while True:
    pygame.gfxdraw.pixel(pygame.display.get_surface(), 400, 400, color)