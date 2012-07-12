import time
import string
import pygame

pygame.init()

def main():
	screen_size = 640, 640
	screen = pygame.display.set_mode(screen_size, pygame.DOUBLEBUF | pygame.HWSURFACE)
	
	done=False
	
	file=open('base.txt','r')
	base=file.readlines()
	leny=len(base)
	
	i=0	
	roads=[]
	walls=[]
	create=0
	
	while i<leny:
		now_line=base[i].split(' ')
		lenght=len(now_line)
		j=0
		while j<lenght:
			if int(now_line[j])==1:
				roads.append([j,i])
			if int(now_line[j])==2:
				walls.append([j,i])
			j+=1
		i+=1
		
	print 'walls :' 
	print walls
	print 'roads :' 
	print roads
	
	zoom = 10
	pos=0,0
	
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done=True
			if event.type == pygame.MOUSEMOTION:
				pos=event.pos[0]/zoom*zoom,event.pos[1]/zoom*zoom,
			if event.type == 5:
				if event.button == 4:#+
					if zoom<=100:
						zoom*=2					
				if event.button == 5:#-
					if zoom>=5:
						zoom/=2
						
			if event.type == pygame.KEYDOWN:					
				if event.key == 49:#1_add_road
					create=1
					x=pos[0]/zoom
					y=pos[1]/zoom
					
					i=0					
					while i<len(walls):						
						if walls[i]==[x,y]:
							walls.pop(i)
						i+=1
					
					j=0
					dubl=False					
					while j<len(roads):						
						if roads[j]==[x,y]:
							dubl=True
						j+=1
					if not dubl:
						roads.append([x,y])
					
				if event.key == 50:#2_add_wall
					create=2
					x=pos[0]/zoom
					y=pos[1]/zoom
					
					i=0					
					while i<len(roads):						
						if roads[i]==[x,y]:
							roads.pop(i)
						i+=1
					
					j=0
					dubl=False					
					while j<len(walls):						
						if walls[j]==[x,y]:
							dubl=True
						j+=1
					if not dubl:
						walls.append([x,y])
		#if create==1:
			
		#if create==2:
		#render
			screen.fill((255, 255, 255))
			
			i=0
			while i<len(walls):
				pygame.draw.rect(screen,(255,0,0),(walls[i][0]*zoom,walls[i][1]*zoom,zoom,zoom))
				i+=1
				
			i=0
			while i<len(roads):
				pygame.draw.rect(screen,(0,255,0),(roads[i][0]*zoom,roads[i][1]*zoom,zoom,zoom))
				i+=1
			pygame.draw.rect(screen,(100,100,100),(pos[0],pos[1],zoom,zoom))
			pygame.display.flip()
		time.sleep(0.02)
main()