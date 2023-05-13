### This is a raycasting program I made with Python using pygame.
### Insert the coordinates of the points and data for the edges and render!

import pygame
import pygame.gfxdraw
import time

points = {}
edges = []
color = (255, 255, 255)

with open("points.txt", "r") as file:
    for line in file:
        line.strip()
        nameAndCoords = line.split(":")
        name = nameAndCoords[0]
        coords = nameAndCoords[1].split(",")
        points.update({name: coords})

with open("edges.txt", "r") as file:
    for line in file:
        line.strip()
        edges.append(line)

def cast(xcor, ycor, zcor, camDistance):
    xcor = int(xcor)
    ycor = int(ycor)
    zcor = int(zcor)
    x = round((xcor * camDistance) / (zcor + camDistance))
    y = round((ycor * camDistance) / (zcor + camDistance))
    return (x, y)

pygame.init()
pygame.display.set_mode((800, 800))
screen = pygame.display.get_surface()


while True:
    dist = 200
    for edge in edges:
        stPoint = cast(points[edge[0]][0], points[edge[0]][1], points[edge[0]][2], dist)
        ndPoint = cast(points[edge[1]][0], points[edge[1]][1], points[edge[1]][2], dist)
        pygame.gfxdraw.line(screen, stPoint[0], stPoint[1], ndPoint[0], ndPoint[1], color)
    pygame.display.flip()
