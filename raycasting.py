### This is a raycasting program I made with Python using pygame.
### Insert the coordinates of the points and data for the edges and render!

import pygame
import pygame.gfxdraw

coordinates = []
edges = []

with open("coordinates.txt", "r") as file:
    for line in file:
        coordinates.append(line)

with open("edges.txt", "r") as file:
    for line in file:
        edges.append(line)

pygame.init()
color = pygame.Color(255, 255, 255)
screen = pygame.display.set_mode((800, 800))
canvas = pygame.Surface((800, 800))
pygame.gfxdraw.pixel(canvas, 400, 400, color)
playFurther = True

while playFurther:
    pygame.gfxdraw.hline(canvas, 0, 800, 400, color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playFurther = False
            print(event)
        else:
            print(event)

pygame.quit()