
from board import boards
import pygame



pygame.init()

#Dimensions of the screen
WIDTH = 900
HEIGHT = 950
screen = pygame.display.set_mode([WIDTH,HEIGHT])

#Time running into pygame
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf',20)
level = boards


def draw_board(lvl):
    num1 = ((HEIGHT - 50)//32)
    num2 = (WIDTH //30)
    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            if level[i][j] == 1:
                # We wanted the Pac-man to eat the white circles
                pygame.draw.circle(screen,'white',(j*num2 + (0.5*num2), i*num1 + (0.5*num1)),4)
            if level[i][j] == 2:
                pygame.draw.circle(screen,'white',(j*num2 + (0.5*num2), i*num1 + (0.5*num1)),10)




run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    draw_board(level)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()

pygame.quit()