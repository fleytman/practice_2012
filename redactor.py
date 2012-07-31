###################
#mode(on keyboard):
#0) passive
#1) create road
#2) create wall
#3) delete
#4) delete 9 cells
###################
#Press S to save map
###################
import time
import string
import pygame
import pickle

pygame.init()

def main():
	screen_size = 640, 640
	screen = pygame.display.set_mode(screen_size, pygame.DOUBLEBUF | pygame.HWSURFACE)
	
	done=False
	
	file=open('base_new.txt','r')#4to otkrivaem
	roads=pickle.load(file)
	walls=pickle.load(file)
	file.close
	
	i=0	
	mode=0
	
	#print 'walls :' 
	#print walls
	#print 'roads :'
	#print roads
	print '###################'
	print '#mode(on keyboard):'
	print '#0) passive'
	print '#1) create road'
	print '#2) create wall'
	print '#3) delete'
	print '#4) delete 9 cells'
	print '#5)add 25 road_cells'
	print '###################'
	print '#Press S to save map'
	print '###################'
	
	zoom = 8
	pos=0,0
	move_x,move_y=0,0
	
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done=True
			if event.type == pygame.MOUSEMOTION:
				pos=event.pos[0]/zoom*zoom,event.pos[1]/zoom*zoom,
				if mode==1:
					x=pos[0]/zoom-move_x
					y=pos[1]/zoom-move_y
					
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
						
				if mode==2:
					x=pos[0]/zoom-move_x
					y=pos[1]/zoom-move_y
					
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
						
				if mode==3:
					x=pos[0]/zoom-move_x
					y=pos[1]/zoom-move_y
					
					i=0					
					while i<len(roads):						
						if roads[i]==[x,y]:
							roads.pop(i)						
						i+=1
					
					i=0					
					while i<len(walls):						
						if walls[i]==[x,y]:
							walls.pop(i)
						i+=1
						
				if mode ==4:
					x_start=pos[0]/zoom-move_x
					y_start=pos[1]/zoom-move_y
					
					x=x_start-1
					y=y_start-1
					while x<=x_start+1 and y<=y_start+1:	
						i=0
						while i<len(walls):
							if walls[i]==[x,y]:
								print 'xxxxx'
								walls.pop(i)
							i+=1
						if y<y_start+1:
							y+=1
						else:
							x+=1
							y-=2
							
					x=x_start-1
					y=y_start-1
					while x<=x_start+1 and y<=y_start+1:	
						i=0
						while i<len(roads):
							if roads[i]==[x,y]:
								print 'xxxxx'
								roads.pop(i)
							i+=1
						if y<y_start+1:
							y+=1
						else:
							x+=1
							y-=2				
					
						
				if mode ==5:
					x_start=pos[0]/zoom-move_x
					y_start=pos[1]/zoom-move_y
					
					x=x_start-2
					y=y_start-2
					while x<=x_start+2 and y<=y_start+2:
						i=0
						while i<len(walls):
							if walls[i]==[x,y]:
								walls.pop(i)
							i+=1
						if y<y_start+2:
							y+=1
						else:
							x+=1
							y-=4
					
					x=x_start-2
					y=y_start-2
					while x<=x_start+2 and y<=y_start+2:
						j=0
						dubl=False					
						while j<len(roads):						
							if roads[j]==[x,y]:
								dubl=True
							j+=1
						if not dubl:
							roads.append([x,y])
						if y<y_start+2:
							y+=1
						else:
							x+=1
							y-=4
				
				if mode ==6:
					x_start=pos[0]/zoom-move_x
					y_start=pos[1]/zoom-move_y
					
					x=x_start-4
					y=y_start-4
					while x<=x_start+4 and y<=y_start+4:	
						i=0
						while i<len(walls):
							if walls[i]==[x,y]:
								print 'xxxxx'
								walls.pop(i)
							i+=1
						if y<y_start+4:
							y+=1
						else:
							x+=1
							y-=8
							
					x=x_start-4
					y=y_start-4
					while x<=x_start+4 and y<=y_start+4:	
						i=0
						while i<len(roads):
							if roads[i]==[x,y]:
								print 'xxxxx'
								roads.pop(i)
							i+=1
						if y<y_start+4:
							y+=1
						else:
							x+=1
							y-=8
											
			if event.type == 5:
				if event.button == 4:#+
					if zoom<=32:
						zoom*=2	
						move_x-=(640/(zoom*2))
						move_y-=(640/(zoom*2))
						
				if event.button == 5:#-
					if zoom>=4:
						zoom/=2
						move_x+=(640/(zoom*4))
						move_y+=(640/(zoom*4))
						
			if event.type == pygame.KEYDOWN:
				print event.key
				if event.key == 273:#top
					move_y+=5
				if event.key == 274:#bot
					move_y-=5
				if event.key == 275:#right
					move_x-=5
				if event.key == 276:#left
					move_x+=5
				
				
				if event.key == 48:#0_passive
					mode=0
					
				if event.key == 49:#1_add_road
					mode=1	
					
				if event.key == 50:#2_add_wall
					mode=2
					
				if event.key == 51:#3_del
					mode=3
					
				if event.key == 52:#4_hard_del
					mode=4
					
				if event.key == 53:#4_hard_road
					mode=5
					
				if event.key == 54:#4_hard_road
					mode=6
					
					
				if event.key == 115:#s_save
					file=open('base_new.txt','w')
					pickle.dump(roads, file)
					pickle.dump(walls, file)
					file.close
					print 'save completed'
					
				if event.key == 99:#c_create - nomer lvla vvodim ru4kami tut=\
					file=open('main_base.txt','w')
					roads_level_=roads
					walls_level_=walls
					pickle.dump(roads_level_, file)
					pickle.dump(walls_level_, file)
					file.close
					print 'save level competed'					
		#render
			screen.fill((255, 255, 255))
			pygame.mouse.set_visible(0)
			
			i=0
			while i<len(walls):
				pygame.draw.rect(screen,(128,128,128),((walls[i][0]+move_x)*zoom,(walls[i][1]+move_y)*zoom,zoom,zoom))
				i+=1
				
			i=0
			while i<len(roads):
				pygame.draw.rect(screen,(127,255,0),((roads[i][0]+move_x)*zoom,(roads[i][1]+move_y)*zoom,zoom,zoom))
				i+=1
				
			if mode==0:#little black cell 
				pygame.draw.rect(screen,(0,0,0),(pos[0],pos[1],zoom,zoom))
				
			if mode==1:#little green cell 
				pygame.draw.rect(screen,(127,255,0),(pos[0],pos[1],zoom,zoom))
				
			if mode==2:#little grey cell 
				pygame.draw.rect(screen,(128,128,128),(pos[0],pos[1],zoom,zoom))
			
			if mode==3:#little red cell 
				pygame.draw.rect(screen,(255,0,0),(pos[0],pos[1],zoom,zoom))
				
			if mode==4:#big red cell
				pygame.draw.rect(screen,(255,0,0),(pos[0]-zoom,pos[1]-zoom,zoom*3,zoom*3))
				
			if mode==5:#big green cell
				pygame.draw.rect(screen,(127,255,0),(pos[0]-zoom*2,pos[1]-zoom*2,zoom*5,zoom*5))
				
			if mode==6:#very_big red cell
				pygame.draw.rect(screen,(255,0,0),(pos[0]-zoom*4,pos[1]-zoom*4,zoom*9,zoom*9))
				
			
			font=pygame.font.Font(None,16)
			text=font.render(('Coordinate: x:'+(str(pos[0]/zoom-move_x))+' | y:'+(str(pos[1]/zoom-move_y))),1,(0,0,255))
			screen.blit(text,(505,630))
				
			pygame.display.flip()
			time.sleep(0.005)
main()