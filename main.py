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

#game background

class Background:
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.bg = img
        self.rect = self.bg.get_rect()
        self.rect.topleft = (self.x,self.y)

    def draw_bg(self):
        screen.blit(self.bg, self.rect)
        screen.blit(self.bg, (self.rect.x ,self.rect.y - self.bg.get_height()))
        screen.blit(self.bg, (self.rect.x ,self.rect.y - (self.bg.get_height() * 2)))

        if self.rect.y > self.bg.get_height():
            self.rect.y = 0
        self.rect.move_ip(0,1)
        
bg = Background(0,0,star_texture)

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
   
    #this function display level and selected spaceship on dashboard
    def PlayerShipAndLevel(self):
        font = pygame.font.SysFont('arial',18,2)
        title = font.render('  PLAYER SHIP  ',True,WHITE,DARKBLUE)
        rect = title.get_rect()
        rect.topleft = (320,50)

        ship = pygame.transform.scale(pygame.image.load(self.selectedship).convert_alpha(),(60,120))
        shiprect = ship.get_rect()
        shiprect.topleft = ((rect.x + (title.get_width() / 2) - (ship.get_width() / 2),rect.y + title.get_height() + 15))

        #showing flame of ship
        flame = pygame.image.load('assets/player/flame/0 (1).png').convert_alpha()
        screen.blit(flame,(shiprect.x + ship.get_width()/2 - flame.get_width()/2,shiprect.y+ship.get_height()-10))

        #show title
        screen.blit(title,rect)
        #show ship
        screen.blit(ship,shiprect)

        #display level ===>  Level : LOW
        level = font.render('  LEVEL : '+ self.selectedlevel+'  ', True, WHITE,DARKBLUE)
        screen.blit(level,(rect.x + title.get_width() + 15,rect.y))

        # return Planet
    #score slider for dashboard
    def ScoreSlider(self):
        btText = '<'
        if self.slider:
            btText = '>'
        else:
            btText = '<'

        box = pygame.surface.Surface((width/2-80,height/2 + 30))
        box.fill(BLACK)
        pygame.Surface.set_alpha(box,150)
        boxrect = box.get_rect()
        boxrect.topleft = (self.sliderboxx,self.sliderboxy)
        screen.blit(box,boxrect)

        leftarrow = Button(self.sliderboxx-25,self.sliderboxy + (box.get_height()/2) - 17,25,35,btText,20,DARKBLUE,RED,hover=False)
        
        if self.slider == False:
            if leftarrow.draw(screen):
                self.sliderboxx = self.sliderboxx - (width/2-100)
                self.slider = True
        else:
            if leftarrow.draw(screen):
                self.sliderboxx = self.sliderboxx + (width/2-100)
                self.slider = False

        font = pygame.font.SysFont('arial',18,2)
        title = font.render('  Score Board  ',True,WHITE)
        screen.blit(title,(self.sliderboxx + (box.get_width()/2) - (title.get_width()/2),self.sliderboxy))

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
        
        #draw one box 
        boxx = ((width / 2) - ((width/2+50)/2))
        boxy = ((height / 2) - ((height/2+50)/2))
        boxwidth = width/2+50
        boxheight = height/2+50
        box = pygame.surface.Surface((boxwidth,boxheight))
        box.fill(BLACK)
        pygame.Surface.set_alpha(box,165)
        screen.blit(box,(boxx,boxy))

        #display level box title
        #draw level button to select
        levelboxtitle = font.render('Choose Level',True,WHITE)
        screen.blit(levelboxtitle,((width/2)-(levelboxtitle.get_width()/2),boxy))

        if self.selectedlevel == 'LOW':
            levelbtborder = pygame.surface.Surface((70,30))
            levelbtborder.fill(RED)
            screen.blit(levelbtborder,(boxx + 5,boxy+(boxheight/2)-25))
        elif self.selectedlevel == 'MEDIUM':
            levelbtborder = pygame.surface.Surface((70,30))
            levelbtborder.fill(RED)
            screen.blit(levelbtborder,(boxx + boxwidth/2 - 35,boxy+(boxheight/2)-25))
        elif self.selectedlevel == 'HIGH':
            levelbtborder = pygame.surface.Surface((70,30))
            levelbtborder.fill(RED)
            screen.blit(levelbtborder,(boxx + boxwidth-75,boxy+(boxheight/2)-25))

        lowbt = Button(boxx + 10,boxy+(boxheight/2)-20,60,20,'LOW',11,WHITE,YELLOW,DARKBLUE,False)
        mediumbt = Button(boxx + boxwidth/2 - 30,boxy+(boxheight/2)-20,60,20,'MEDIUM',11,WHITE,YELLOW,DARKBLUE,False)
        highbt = Button(boxx + boxwidth-70,boxy+(boxheight/2)-20,60,20,'HIGH',11,WHITE,YELLOW,DARKBLUE,False)
        
        if lowbt.draw(screen):
            self.selectedlevel = 'LOW'
        elif mediumbt.draw(screen):
            self.selectedlevel = 'MEDIUM'
        elif highbt.draw(screen):
            self.selectedlevel = 'HIGH'
        
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

        #show some content
        surf = pygame.surface.Surface((width/2, height/2 + 60))
        surf.fill(BLACK)
        pygame.Surface.set_alpha(surf,200)
        surfrect = surf.get_rect()
        surfrect.topleft=(width/2 - surf.get_width()/2,height/2 - surf.get_height()/2)
        screen.blit(surf,surfrect)
        
        helpmsg = [
            'choose low level for the first game play',
            'go to choose option to select space ship',
            'use different space ship',
            'go to setting option to select a level',
            'click on start button to start game',
            'you can see the score in the slider box',
            'you can also see score in score',
            'to know about developer go to about option',
            'click on exit to exit from the game'
        ]
        msgfont = pygame.font.SysFont('arial',14,2)

        btup = Button(surfrect.x + surf.get_width() - 20,surfrect.y,20,20,'/\\',15,LIGHTGREEN,RED,WHITE,False)
        btdown = Button(surfrect.x + surf.get_width() - 20,surfrect.y + surf.get_height() - 20,20,20,'\\/',15,LIGHTGREEN,RED,WHITE,False)

        my = self.helpmsgy + surfrect.y
        msgTotalHeight = 0
        scrollerheight = surf.get_height() - 40
        for i in range(len(helpmsg)):
            msg = msgfont.render(str(i+1)+' ) '+helpmsg[i],True,WHITE)
            if my < surfrect.y or my > (surfrect.y + surf.get_height() - msg.get_height()):
                pass
            else:
                screen.blit(msg,(surfrect.x + 25,my))
            my += msg.get_height() + 25
            msgTotalHeight += msg.get_height() + 25

        scroll = pygame.surface.Surface((5, 20))
        scrollrect = scroll.get_rect()
        scrollrect.topleft = (surfrect.x + surf.get_width() - scroll.get_width()/2 - 10,self.helpmsgscrolly+surfrect.y + 20)
        scroll.fill(WHITE)
        screen.blit(scroll,scrollrect)

        if btup.draw(screen):
            if scrollrect.y < (surfrect.y + 20):
                pass
            else:
                self.helpmsgy += 2
                self.helpmsgscrolly -= (scrollerheight * 2) / msgTotalHeight
        if btdown.draw(screen):
            if scrollrect.y > (surfrect.y + surf.get_height() - scroll.get_height() - 20):
                pass
            else:
                self.helpmsgy -= 2
                self.helpmsgscrolly += (scrollerheight * 2) / msgTotalHeight
        # print(self.helpmsgy) 

    def ChooseShipSec(self):
        self.surf.fill(DARKBLUE)
        font = pygame.font.SysFont('arial',20,2)
        title = font.render('Spaceship',True,WHITE)
        #display background and title
        screen.blit(about_bg,(0,0))
        screen.blit(self.surf,(self.titlex,self.titley))
        screen.blit(title,((self.titlex + (self.titlewidth/2) - (title.get_width()/2)),(self.titley + (self.titleheight / 2) - (title.get_height() / 2))))

        #set to choose player ships from the list of BIg medium and small ship
        surf = pygame.surface.Surface((width - 100, height- 100))
        surf.fill(BLACK)
        pygame.Surface.set_alpha(surf,100)
        screen.blit(surf,(width/2 - ((width - 100)/2),height/2 - ((height - 100)/2)))

        #Note : choose space ship by clicking onit
        note = font.render('Note : choose space-ship by clicking on it !',True,WHITE)
        pygame.Surface.set_alpha(note,150)
        screen.blit(note, (width / 2 - note.get_width() / 2,height - note.get_height() - 10)) 
        shipsizelist = ['Big','Medium','Small']

        x = 250
        y = 80
        shipheight = 0
        for i in range(3):
            selectedsize = 'assets/player/Ships/'+str(shipsizelist[i])
            sizetitle = font.render(shipsizelist[i],True,WHITE)
            screen.blit(sizetitle,(100,y))
            for j in range(1,4):
                #get mouse pointer position
                pos = pygame.mouse.get_pos()
                #get image path
                #load image and get rect for x and y setup
                #scale image
                selectimg = selectedsize+'/'+str(j)+'.png'
                img = pygame.image.load(selectimg).convert_alpha()
                scaleimg = pygame.transform.scale(img,(int(img.get_width() * 0.5),int(img.get_height() * 0.5)))
                imgrect = scaleimg.get_rect()
                imgrect.topleft = (x,y)

                #draw border on selected image
                if selectimg == self.selectedship:
                    borderbox = pygame.surface.Surface((scaleimg.get_width()+10, scaleimg.get_height()+10))
                    borderbox.fill(LIGHTGREEN)
                    screen.blit(borderbox,(imgrect.x - 5,imgrect.y - 5))

                #check collide with mouse and select ship
                if imgrect.collidepoint(pos):
                    hoverbox = pygame.surface.Surface((scaleimg.get_width()+10, scaleimg.get_height()+10))
                    hoverbox.fill(YELLOW)
                    screen.blit(hoverbox,(imgrect.x - 5,imgrect.y - 5))
                    #display image on big size
                    bigimg = pygame.transform.scale(img,(int(img.get_width() * 1.3),int(img.get_height() * 1.3)))
                    screen.blit(bigimg,((width/2 - ((width - 100)/2)) + (width - 100) - bigimg.get_width() - 20, ((height/2 - ((height - 100)/2)) + ((height-100)/2) - bigimg.get_height() / 2)))
                    #onclick ship selected
                    if pygame.mouse.get_pressed()[0] == 1:
                        self.selectedship = selectimg
                        player = Player(400,300,db.selectedship)


                screen.blit(scaleimg,imgrect)
                x += scaleimg.get_width() + 30
                shipheight = scaleimg.get_height()
            y += shipheight + 30
            x = 250

#planet enimation
class Planet(pygame.sprite.Sprite):
    def __init__(self):
        super(Planet, self).__init__()
        self.flames = []
        for i in range(1,61):
            self.flames.append(pygame.transform.scale(pygame.image.load('assets/gamebg/Moon/'+str(i)+'.png'),(90,90)))
        self.index = 0
        self.image = self.flames[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (width-300,80)

    def update(self):
        self.index += 1
        if self.index >= len(self.flames):
            self.index = 0
        time.sleep(0.04)
        self.image = self.flames[self.index]


#-------when game will started----------
#player setups here
move_left = False
move_right = False
move_up = False
move_down = False
shoot = False
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        super(Player,self).__init__()
        self.cool_down = 0
        self.img = img
        # self.last_time = pygame.time.get_ticks()
        self.reset(x,y)

        # print(self.player)
    def reset(self,x,y):
        self.x = x 
        self.y = y
        self.ship = pygame.image.load(self.img).convert_alpha()
        self.player = pygame.transform.scale(self.ship,(60,120))
        self.rect = self.player.get_rect()
        self.rect.topleft = (self.x,self.y)

    def shoot(self):
        if self.cool_down == 0:
            self.cool_down = 40
            bullet = Bullet(self.rect.centerx,self.rect.centery)
            bullet_group.add(bullet)

    def update(self):
        if self.cool_down > 0:
            self.cool_down -= 1

        #player move
        if move_up:
            self.rect.move_ip(0,-1)
        if move_down:
            self.rect.move_ip(0,1)
        if move_left:
            self.rect.move_ip(-1,0)
        if move_right:
            self.rect.move_ip(1,0)

        #collide on window edge
        if self.rect.y < 10:
            self.rect.y = 10
        if (self.rect.y+self.player.get_height()) > height - 10:
            self.rect.y = height - 10 -self.player.get_height()
        if self.rect.x < 10:
            self.rect.x = 10
        if (self.rect.x+self.player.get_width()) > width - 10:
            self.rect.x = width - 10 - self.player.get_width()
        
        screen.blit(self.player,self.rect)

#bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Bullet,self).__init__()
        self.x = x
        self.y = y
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def update(self):
        self.rect.y -= 2

        if self.rect.y < 0:
            self.kill
        

#create dashboard object
db = Dashboard()
#planet
planet = Planet()
planet_group = pygame.sprite.Group(planet)
bullet_group = pygame.sprite.Group()

#player
player = Player(400,300,db.selectedship)

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
        #show Planet
        planet_group.update()
        planet_group.draw(screen)
        #score slider display
        db.ScoreSlider()
        #setup menu
        #start button
        start.msg(screen,'To Start Game Click Here',12)

        #create player object on dashboard
        player = Player(400,300,db.selectedship)

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
        bg.draw_bg()
        db.StartGame()
        #draw bullets
        bullet_group.update()
        bullet_group.draw(screen)
        
        player.update()
        if shoot:
            player.shoot()

        if back.draw(screen):
            startgame = False
            setting_sec = False
            score_sec = False
            help_sec = False
            about_sec = False
            dashboard = True
            chooseship_sec = False
            player.reset(400,300)
            bullet_group.empty()

    #keyboard event loop start here
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            if event.key == K_UP:
                move_up = True
            if event.key == K_DOWN:
                move_down = True
            if event.key == K_LEFT:
                move_left = True
            if event.key == K_RIGHT:
                move_right = True
            if event.key == K_a:
                shoot = True
        if event.type == KEYUP:
            if event.key == K_UP:
                move_up = False
            if event.key == K_DOWN:
                move_down = False
            if event.key == K_LEFT:
                move_left = False
            if event.key == K_RIGHT:
                move_right = False
            if event.key == K_a:
                shoot = False
            
    
    #update and flip our display
    pygame.display.update()
    pygame.display.flip()

pygame.quit()