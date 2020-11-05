import pygame
from pygame.sprite import Sprite

class Start(Sprite):
	def __init__(self,screen):
		super().__init__()
		self.screen=screen
		self.image=pygame.image.load('images/start.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=self.screen.get_rect()
		self.rect.x=self.rect.height
		self.rect.y=self.rect.height


	def blitme(self):
		#再置顶位置绘制飞船 
		self.screen.blit(self.image,self.rect)
