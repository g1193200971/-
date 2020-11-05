import pygame
import sys
from start import Start
from pygame.sprite import Group
from random import randint
def run():
	pygame.init()
	#设置大小 
	screen=pygame.display.set_mode((1000,800))
	#名字
	pygame.display.set_caption('星空')
	#颜色
	color=(0,0,0)

	#星星的标组
	sg=Group()

	#引入星星

	update(screen,sg)

	while True:
		#按键和鼠标监控
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()

		screen.fill(color)

		sg.draw(screen)
		# s.blitme()
		#显示

		pygame.display.flip()

def update(screen,sg):

	s=Start(screen)
	#横排放多少个
	width=int((s.screen_rect.width-2*s.rect.width)/(2*s.rect.width))
	height=int((s.screen_rect.height-2*s.rect.height)/(2*s.rect.height))
	for x in range(height):
		for y in range(width):

			st=Start(screen)
			random_number1 = randint(-20,20)
			random_number2 = randint(-20,20)
			st.rect.x=st.rect.width+(4*st.rect.width)*y+random_number2
			st.rect.y=st.rect.height+(4*st.rect.height)*x+random_number1
			sg.add(st)



run()
