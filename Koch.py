import pygame
import math
from colour import Color
import copy
import random

pygame.init()
screenWidth = 1280
screenHeight = 1024
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Fractal")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

red = Color('red')
colorRange = list(red.range_to(Color(color='purple'), 19))
colorArray = copy.deepcopy(colorRange)


def getRandColor():
    global colorArray
    if len(colorArray) == 0:
        colorArray = copy.deepcopy(colorRange)
        r = random.randint(0, len(colorArray)-1)
        color = [colorArray[r].get_red()*255, colorArray[r].get_green()*255, colorArray[r].get_blue()*255]
        colorArray.pop(r)
    else:
        r = random.randint(0, len(colorArray) - 1)
        color = [colorArray[r].get_red() * 255, colorArray[r].get_green() * 255, colorArray[r].get_blue() * 255]
        colorArray.pop(r)

    return color


def line_len(p1: list, p2: list):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)


def line_to_fract(p1: list, p2: list):
    newLines = []
    x = (p2[0]-p1[0])/3
    y = (p2[1]-p1[1])/3

    vec = [x, y]
    angle = 3.1415/3

    cs = math.cos(-angle)
    sn = math.sin(-angle)
    rx = x * cs - y * sn
    ry = x * sn + y * cs

    upVec = [rx, ry]



    cs = math.cos(angle)
    sn = math.sin(angle)
    rx = x * cs - y * sn
    ry = x * sn + y * cs

    downVec = [rx, ry]


    start = p1
    end = [start[0] + vec[0], start[1] + vec[1]]
    newLines.append([start, end])

    start = end
    end = [start[0] + upVec[0], start[1] + upVec[1]]
    newLines.append([start, end])

    start = end
    end = [start[0] + downVec[0], start[1] + downVec[1]]
    newLines.append([start, end])

    start = end
    end = [start[0] + vec[0], start[1] + vec[1]]
    newLines.append([start, end])



    for line in newLines:
        pygame.draw.line(screen, getRandColor(), line[0], line[1], width=1)

    return newLines


p1 = [400, 275]
p2 = [screenWidth - 400, 275]
p3 = [screenWidth - 400, 275+480]
p4 = [400, 275+480]

lines = [[p1, p2],
         [p2, p3],
         [p3, p4],
         [p4, p1]]

for ln in lines:
    pygame.draw.line(screen, getRandColor(), ln[0], ln[1])
pygame.display.update()

done = False
running = True
while running:
    screen.fill(BLACK)
    pygame.time.delay(1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not done:
        newLines = []
        for line in lines:
            if line_len(line[0], line[1]) < 5:
                done = True
            for fractLine in line_to_fract(line[0], line[1]):
                newLines.append(fractLine)
        lines = newLines
    else:
        for i in lines:
            pygame.draw.line(screen, getRandColor(), i[0], i[1])

    pygame.display.update()



