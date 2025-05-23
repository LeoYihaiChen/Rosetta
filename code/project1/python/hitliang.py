import pygame,sys
from pygame.locals import *
white = (255,255,255)
blue  = (0,0,200)
pygame.init()
screen = pygame.display.set_mode((600,500))
myfont = pygame.font.pygame.font.Font(None,60)
textImage = myfont.render("LiangKey is foolish",True,white)
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()
    screen.fill(blue)
    screen.blit