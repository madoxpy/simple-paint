# -*- coding: utf-8 -*-

from pygame import                           *
import sys

def pencil(size,old_pos):
	if size>4:
		draw.circle(window,color,mouse.get_pos(),size)
	else:
		draw.line(window,color,old_pos,mouse.get_pos(),size)
		
		
def gumka(size,old_pos):
	if size>4:
		draw.circle(window,background,mouse.get_pos(),size)
	else:
		draw.line(window,background,old_pos,mouse.get_pos(),size)


init()
window = display.set_mode( (256+640,512) )
clock = time.Clock()


background = (255,255,255)
color = (0,0,0)


window.fill(background)

if len(sys.argv)==2:
	photo = image.load(sys.argv[1])
	photo=transform.scale(photo,(640,512))
	window.blit(photo,(256,0))


def palette():
	for j in range(256):
		for i in range(256):
			window.set_at( (j,i), (j,i,(i+j)%256) )

	for j in range(256):
		for i in range(256):
			window.set_at( (j,i+256), (i,(i+j)%256,j) )		

	draw.line( window,(0,0,0),(256,0),(256,512),3)

palette()
size = 1

end=False
while not end:
	for z in event.get():
		if z.type == QUIT :
			end = True
			
	if mouse.get_pressed()[0] == 1:
		if mouse.get_pos()[0] < 256+size:
			if mouse.get_pos()[1]<256:
				color=(mouse.get_pos()[0]%256,mouse.get_pos()[1]%256,(mouse.get_pos()[0]+mouse.get_pos()[1])%256)
			else:
				color=((mouse.get_pos()[1]-256)%256,(mouse.get_pos()[0]+mouse.get_pos()[1]-256)%256,mouse.get_pos()[0]%256)
		else:
			pencil(size,old_pos)
			
	if mouse.get_pressed()[2] == 1:			
			if mouse.get_pos()[0]>256+size:
				gumka(size,old_pos)
			
	old_pos=mouse.get_pos()
	
	keys=key.get_pressed()
	if keys[K_1]:
		tosave = Surface( (640,512) )
		tosave.blit(window,(0,0),(256,0,640+256,512))
		image.save(tosave,"obraz1.png")
	if keys[K_2]:
		tosave = Surface( (640,512) )
		tosave.blit(window,(0,0),(256,0,640+256,512))
		image.save(tosave,"obraz2.png")
	if keys[K_3]:
		tosave = Surface( (640,512) )
		tosave.blit(window,(0,0),(256,0,640+256,512))
		image.save(tosave,"obraz3.png")
	if keys[K_a]:
		size=size+1
	if keys[K_z]:
		if size<1:
			size=1
		else:
			size=size-1		
	
	
	clock.tick(100)
	display.flip()