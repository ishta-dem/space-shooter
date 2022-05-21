import pygame 
from pygame.locals import *
from pygame import *

#button class
class Button():
	def __init__(self,x, y,width,height,text,fontsize,bgcolor,hovercolor,fontcolor=(255,255,255),hover=True):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.text = text
		self.fontsize = fontsize
		self.fontcolor = fontcolor
		self.bgcolor = bgcolor
		self.hovercolor = hovercolor
		self.hover = hover
		self.surf = pygame.surface.Surface((width,height))
		self.surf.fill(bgcolor)
		self.rect = self.surf.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

		#temp font color
		self.tempfontcolor = fontcolor
        
	def draw(self, surface):
		action = False
		font = pygame.font.SysFont('arial',int(self.fontsize),2)
		text = font.render(str(self.text),True,self.fontcolor)
		textwidth= text.get_width()
		textheight= text.get_height()

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			self.surf.fill(self.hovercolor)
			self.fontcolor = (255,255,255)
			if self.hover:
				self.rect.x = self.x - 5
            
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True
		else:
			self.surf.fill(self.bgcolor)
			self.fontcolor = self.tempfontcolor
			self.rect.x = self.x

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button
		surface.blit(self.surf, (self.rect.x, self.rect.y))
		surface.blit(text,((self.rect.x +(self.width/2) - (textwidth/2)),(self.rect.y + (self.height/2) - (textheight/2))))
        
		# render(surface,(self.rect.x +self.width/2),self.rect.y,self.text,self.fontsize)

		return action
	def msg(self,surface,text,fontsize=14,fontcolor=(255,255,255),fontbg=(0,0,0)):
		font = pygame.font.SysFont('arial',int(fontsize),2)
		text = font.render(str(text),True,fontcolor)
		textwidth= text.get_width()
		textheight= text.get_height()

		pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(pos):
			surface.blit(text,(self.rect.x + (self.width + 10),(self.rect.y + (self.height / 2) - (textheight / 2))))
		else:
			pass