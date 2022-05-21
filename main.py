#Game : Space Shooter

import pygame
from pygame.locals import *
from pygame import *
import time
import os
from button import Button

#initialize pygame
pygame.init()

#width 900 and height 450
width = 900
height = 450

#set width & height value
screen = pygame.display.set_mode((width,height))
#set caption of our game
pygame.display.set_caption('space-shooter')

#set FPS
clock = pygame.time.Clock()
FPS = 120

#DEFINE COLORS
WHITE = (255,255,255)
BLACK = (0,0,0)
DARKGREEN = (25,65,25)
LIGHTGREEN = (25,250,25)
RED = (255,25,25)
DARKBLUE = (20,50,105)
LIGHTBLUE = (20,25,255)
YELLOW = (255,255,0)


#load flames
dashboard_bg = pygame.transform.scale((pygame.image.load('assets/background/dashboard.jpg').convert_alpha()),(width,height))
setting_bg = pygame.transform.scale((pygame.image.load('assets/background/setting.jpg').convert_alpha()),(width,height))
score_bg = pygame.transform.scale((pygame.image.load('assets/background/score.jpg').convert_alpha()),(width,height))
about_bg = pygame.transform.scale((pygame.image.load('assets/background/aboutbg.jpg').convert_alpha()),(width,height))
help_bg = pygame.transform.scale((pygame.image.load('assets/background/score.jpg').convert_alpha()),(width,height))
star_texture = pygame.transform.scale((pygame.image.load('assets/gamebg/stars_texture.png').convert_alpha()),(width,height))
galaxy = pygame.transform.scale((pygame.image.load('assets/gamebg/galaxy.png').convert_alpha()),(width,height))
bullet_img = pygame.image.load('assets/player/Laser/bullet.gif').convert_alpha()

#define a buttons
start = Button(50,50,120,25,'START',16,BLACK,RED,WHITE)
setting = Button(50,100,120,25,'SETTING',16,BLACK,RED,WHITE)
score = Button(50,150,120,25,'SCORE',16,BLACK,RED,WHITE)
about = Button(50,200,120,25,'ABOUT',16,BLACK,RED,WHITE)
Help = Button(50,250,120,25,'HELP',16,BLACK,RED,WHITE)
chooseship = Button(50,300,120,25,'CHOOSE',18,BLACK,DARKGREEN,WHITE)
Exit = Button(width-170,50,120,25,'EXIT',16,BLACK,RED,WHITE,False)
back = Button(10,10,20,20,'<',18,BLACK,DARKGREEN,WHITE,False)

#game variable 
startgame = False
setting_sec = False
score_sec = False
about_sec = False 
help_sec = False
dashboard = True
chooseship_sec = False


#init.. True for loop
run = True
#start loop
while run:
    clock.tick(FPS)

    screen.fill(DARKBLUE)
    screen.blit(dashboard_bg,(0,0))
        
    #keyboard event loop start here
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            
        if event.type == KEYUP:
            if event.key == K_UP:
                move_up = False
            
            
    
    #update and flip our display
    pygame.display.update()
    pygame.display.flip()

pygame.quit()