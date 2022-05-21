#Game : Space Shooter
#Author : Ravi Panchal

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

#author description
def author():
    font = pygame.font.SysFont('arial', 14, 2)
    text = font.render('Developer : Ravi Panchal',True,WHITE)
    textwidth = text.get_width()
    textheight = text.get_height()
    screen.blit(text,((width) - (textwidth + 20),(height - (textheight * 2))))

#--------------dashboard------------------
#this used to render image title and box
#all operations are perform in loops event
class Dashboard:
    def __init__(self):
        self.selectedlevel = 'LOW'
        self.selectedship = 'assets/player/Ships/Small/1.png'
        self.titlewidth = 160
        self.titleheight = 30
        self.titlex = width / 2 - self.titlewidth/2
        self.titley = 10
        self.surf = pygame.surface.Surface((self.titlewidth,self.titleheight))
        self.sliderboxx = width - (width/2-75) + (width/2-100)
        self.sliderboxy = (height/2) - ((height/2 + 30)/2)
        self.slider = False
        self.helpmsgx = 0
        self.helpmsgy = 0
        self.helpmsgscrolly = 0
   
        # return Planet
    
    def StartGame(self):
        font = pygame.font.SysFont('arial',12,2)
        title = font.render('LEVEL : '+str(self.selectedlevel),True,WHITE)
        screen.blit(title, (width - title.get_width() - 5,10))

        score = font.render('SCORE : '+str(1000),True,WHITE)
        screen.blit(score,(width - title.get_width() - score.get_width() - 20 ,10))

        ship = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(self.selectedship),(20,40)), 90)
        screen.blit(ship, (width - title.get_width() - ship.get_width() - score.get_width() - 30 ,10))

    def SettingSec(self):
        self.surf.fill(DARKBLUE)
        font = pygame.font.SysFont('arial',20,2)
        title = font.render('Setting',True,WHITE)
        #display background and title
        screen.blit(setting_bg,(0,0))
        screen.blit(self.surf,(self.titlex,self.titley))
        screen.blit(title,((self.titlex + (self.titlewidth/2) - (title.get_width()/2)),(self.titley + (self.titleheight / 2) - (title.get_height() / 2))))
        
        
    def ScoreSec(self):
        self.surf.fill(DARKBLUE)
        font = pygame.font.SysFont('arial',20,2)
        title = font.render('Score Board',True,WHITE)
        #display background and title
        screen.blit(score_bg,(0,0))
        screen.blit(self.surf,(self.titlex,self.titley))
        screen.blit(title,((self.titlex + (self.titlewidth/2) - (title.get_width()/2)),(self.titley + (self.titleheight / 2) - (title.get_height() / 2))))
    
    def AboutSec(self):
        self.surf.fill(DARKBLUE)
        font = pygame.font.SysFont('arial',20,2)
        title = font.render('About Us',True,WHITE)
        #display background and title
        screen.blit(about_bg,(0,0))
        screen.blit(self.surf,(self.titlex,self.titley))
        screen.blit(title,((self.titlex + (self.titlewidth/2) - (title.get_width()/2)),(self.titley + (self.titleheight / 2) - (title.get_height() / 2))))

    def HelpSec(self):
        self.surf.fill(DARKBLUE)
        font = pygame.font.SysFont('arial',20,2)
        title = font.render('Help !',True,WHITE)
        #display background and title
        screen.blit(help_bg,(0,0))
        screen.blit(self.surf,(self.titlex,self.titley))
        screen.blit(title,((self.titlex + (self.titlewidth/2) - (title.get_width()/2)),(self.titley + (self.titleheight / 2) - (title.get_height() / 2))))

    def ChooseShipSec(self):
        self.surf.fill(DARKBLUE)
        font = pygame.font.SysFont('arial',20,2)
        title = font.render('Spaceship',True,WHITE)
        #display background and title
        screen.blit(about_bg,(0,0))
        screen.blit(self.surf,(self.titlex,self.titley))
        screen.blit(title,((self.titlex + (self.titlewidth/2) - (title.get_width()/2)),(self.titley + (self.titleheight / 2) - (title.get_height() / 2))))

        


#create dashboard object
db = Dashboard()

#init.. True for loop
run = True
#start loop
while run:
    clock.tick(FPS)

    #if game is not start then we are on dashboard
    if startgame == False and dashboard == True:
        screen.fill(DARKBLUE)
        screen.blit(dashboard_bg,(0,0))
        author()
        #show title and selectd ship for player ===> Player Ship
        db.PlayerShipAndLevel()
        
        #score slider display
        db.ScoreSlider()
        #setup menu
        #start button
        start.msg(screen,'To Start Game Click Here',12)

        if start.draw(screen):
            startgame = True
            setting_sec = False
            score_sec = False
            help_sec = False
            about_sec = False 
            dashboard = False
            chooseship_sec = False

        #setting button
        setting.msg(screen,'Choose a best settings',12)
        if setting.draw(screen):
            startgame = False
            setting_sec = True
            score_sec = False
            help_sec = False
            about_sec = False 
            dashboard = False
            chooseship_sec = False

        #score button
        score.msg(screen,'Show Score',12)
        if score.draw(screen):
            startgame = False
            setting_sec = False
            score_sec = True
            help_sec = False
            about_sec = False 
            dashboard = False
            chooseship_sec = False

        #about button
        about.msg(screen,'Know more',12)
        if about.draw(screen):
            startgame = False
            setting_sec = False
            score_sec = False
            help_sec = False
            about_sec = True 
            dashboard = False
            chooseship_sec = False

        #help button
        Help.msg(screen,'Click to Get Tips',12)
        if Help.draw(screen):
            startgame = False
            setting_sec = False
            score_sec = False
            help_sec = True
            about_sec = False 
            dashboard = False
            chooseship_sec = False
        
        #chooseship button
        chooseship.msg(screen,'select your space-ship',12)
        if chooseship.draw(screen):
            startgame = False
            setting_sec = False
            score_sec = False
            help_sec = False
            about_sec = False 
            dashboard = False
            chooseship_sec = True

        #exit button
        if Exit.draw(screen):
            run = False
    #open setting section
    elif setting_sec:
        screen.fill(LIGHTGREEN)
        db.SettingSec()
        if back.draw(screen):
            startgame = False
            setting_sec = False
            score_sec = False
            help_sec = False
            about_sec = False
            dashboard = True
            chooseship_sec = False

    #open score section
    elif score_sec:
        screen.fill(LIGHTGREEN)
        db.ScoreSec()
        if back.draw(screen):
            startgame = False
            setting_sec = False
            score_sec = False
            help_sec = False
            about_sec = False
            dashboard = True
            chooseship_sec = False

    #open about section
    elif about_sec:
        screen.fill(RED)
        db.AboutSec()
        if back.draw(screen):
            startgame = False
            setting_sec = False
            score_sec = False
            help_sec = False
            about_sec = False
            dashboard = True
            chooseship_sec = False
        
    #open help section
    elif help_sec:
        screen.fill(BLACK)
        db.HelpSec()
        # if btup.draw(screen):
        #     db.helpmsgy += 10
        # if btdown.draw(screen):
        #     db.helpmsgy -= 10
        if back.draw(screen):
            startgame = False
            setting_sec = False
            score_sec = False
            help_sec = False
            about_sec = False
            dashboard = True
            chooseship_sec = False
    
    #open chooseship section
    elif chooseship_sec:
        screen.fill(BLACK)
        db.ChooseShipSec()
        if back.draw(screen):
            startgame = False
            setting_sec = False
            score_sec = False
            help_sec = False
            about_sec = False
            dashboard = True
            chooseship_sec = False
        
    #it means game is started
    else:
        screen.fill(WHITE)
        
        if back.draw(screen):
            startgame = False
            setting_sec = False
            score_sec = False
            help_sec = False
            about_sec = False
            dashboard = True
            chooseship_sec = False
            

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