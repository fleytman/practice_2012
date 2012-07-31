import time
import string
import pygame
import pickle

pygame.init()

def main():
	screen_size = 1280, 680
	screen = pygame.display.set_mode(screen_size, pygame.DOUBLEBUF | pygame.HWSURFACE)
	
	done=False
	
	#file=open('base_convert.txt','r')#4to otkrivaem
	#roads=pickle.load(file)
	#walls=pickle.load(file)
	#file.close
	
	file=open('map.txt','r')#4to otkrivaem
	map=pickle.load(file)
	file.close
	
	zoom = 2
	pos=0,0
	move_x,move_y=0,0
	start,end=[0,0],[0,0]
	start_add,end_add=0,0
	
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done=True
			if event.type == pygame.MOUSEMOTION:
				pos=event.pos[0]/zoom*zoom,event.pos[1]/zoom*zoom,
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
					
				if event.key == 49:#1				
					start=pos[0]/zoom-move_x,pos[1]/zoom-move_y
					if start_add<>1:
						start_add=1
					else:
						start_add=0
					
				if event.key == 50:#2
					end=pos[0]/zoom-move_x,pos[1]/zoom-move_y
					if end_add<>1:
						end_add=1
					else:
						end_add=0
					
		#render
		screen.fill((127, 127, 127))
		#pygame.mouse.set_visible(0)
		i=0
		#while i<len(roads):
		#	j=0
		#	while j<len(roads[i]):
			#	pygame.draw.rect(screen,(127,255,0),((i+move_x)*zoom,(roads[i][j]+move_y)*zoom,zoom,zoom))
			#	j+=1
			#i+=1
			
		#i=0
		#while i<len(walls):
			#j=0
			#while j<len(walls[i]):
				#pygame.draw.rect(screen,(128,128,128),((i+move_x)*zoom,(walls[i][j]+move_y)*zoom,zoom,zoom))
				#j+=1
			#i+=1
			
		i=0
		
		while i<len(map):
			j=0
			while j<len(map[i]):
				if map[i][j]==2:
					pygame.draw.rect(screen,(127,255,0),((i+move_x)*zoom,(j+move_y)*zoom,zoom,zoom))
				j+=1
			i+=1
		
		if start_add==1:
			pygame.draw.rect(screen,(255,0,0),((start[0]+move_x)*zoom,(start[1]+move_y)*zoom,zoom,zoom))
		if end_add==1:
			pygame.draw.rect(screen,(0,0,255),((end[0]+move_x)*zoom,(end[1]+move_y)*zoom,zoom,zoom))
			
		
			
		font=pygame.font.Font(None,16)
		text=font.render(('Coordinate: x:'+(str(pos[0]/zoom-move_x))+' | y:'+(str(pos[1]/zoom-move_y))),1,(255,0,0))
		screen.blit(text,(screen_size[0]-135,screen_size[1]-10))	
		
		pygame.display.flip()
		
		time.sleep(0.005)

def findway(map,start,end):
	masmove=[0,-1],[-1,0],[1,0],[0,1]
	#o4ered
	open=[] #spisok to4ek kotorie nujno posetit`
	points=[] #vostanovlenie puti
	visited=[] #gde bili
	#to4ka starta
	x1,y1=start
	#to4ka konca
	x2,y2=end
   
	#kraynee kletki poseshenie
	i=0
	while i<len(map):
		visited.append([i,0])
		i+=1
	i=0
	while i<len(map):
		visited.append([i,len(map[0])])
		i+=1
	i=0
	while i<len(map[0]):
		visited.append([0,i])
		i+=1
	i=0
	while i<len(map):
		visited.append([len(map),i])
		i+=1
    
	open.append(start) #dobavlyaem v o4ered` na4al`nuu to4ku
	points.append(start) 
    
	while len(open)>0:#esli o4ered` ne pusta
		n=open.pop(0) #izvlekaem perviy element
		if n==[x2,y2]: #esli raven celi put` naiden
		#vostonavlivaem put`
			way=[]
			while n<>[0,0]: #esli to4ka ne nacal`naya
				way.append(n) #dobavlyaem v put`
				way.append(start) #start v put`
							
				return way #rezult
        
		else: #esli ne raven celi
			for i in masmove: #perebiraem sosednie kletki        
				if mas[n[0]+i[0]][n[1]+i[1]]==1: #esli nelzya proyti
					pass 
				elif  visited.count([n[0]+i[0],n[1]+i[1]]): #esli bili
					pass 
				else: #esli net
					visited.append([n[0]+i[0],n[1]+i[1]]) #dobavlyaem s poseshennie
					n1=n[0]+i[0],n[1]+i[1] #sozdaem sled to4ku
                    
			#dobavlyaem v o4ered
			open.append(n1)
                    
			points.append(n1)
    
	#esli perebrali vse
	print 'not found'
main()