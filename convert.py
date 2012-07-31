import time
import string
import pygame
import pickle

pygame.init()

def main():
	file=open('base_new2.txt','r')#4to otkrivaem
	roads=pickle.load(file)
	walls=pickle.load(file)
	file.close
	
	naim_x,naim_y=naim_x_y(roads,walls)
	roads,walls=sdvig(roads,walls,naim_x,naim_y)
	roads,walls=converted(roads,walls)
	naib_x,naib_y=naib_x_y(roads,walls)
	roads,walls=many_roads(roads,walls,naib_x,naib_y)
	converted_in_map(roads,walls,naib_x,naib_y)
	print 'complete'
	time.sleep(100)
	

def naim_x_y(roads,walls):
	i=0
	x,y=1000,1000
	while i<len(roads):
		if roads[i][0]<x:
			x=roads[i][0]
		if roads[i][1]<y:
			y=roads[i][1]
		i+=1
		
	i=0
	while i<len(walls):
		if walls[i][0]<x:
			x=walls[i][0]
		if walls[i][1]<y:
			y=walls[i][1]
		i+=1
		
	return x,y
		
def sdvig(roads,walls,naim_x,naim_y):
	i=0
	while i<len(roads):
		roads[i][0]-=naim_x
		roads[i][1]-=naim_y
		i+=1
		
	i=0
	while i<len(walls):
		walls[i][0]-=naim_x
		walls[i][1]-=naim_y
		i+=1
		
	return roads,walls
		
def converted(roads,walls):
	#sozdanie pustih spiskov
	roads_convert=[]
	walls_convert=[]
	
	#zapolnenie spiskov pustimi elementami
	i=0
	while i<=1000:
		roads_convert.append([])
		i+=1
	
	i=0
	while i<=1000:
		walls_convert.append([])
		i+=1
	
	#konvertacia
	i=0
	while i<len(walls):
		elem=walls[i]
		x=elem[0]
		y=elem[1]
		walls_convert[x].append(y)
		i+=1

	i=0
	while i<len(roads):
		elem=roads[i]
		x=elem[0]
		y=elem[1]
		roads_convert[x].append(y)
		i+=1
	
	#sortirovka
	i=0	
	while i<len(roads_convert):
		roads_convert[i].sort()
		i+=1
			
	i=0	
	while i<len(walls_convert):
		walls_convert[i].sort()
		i+=1
	
	roads=roads_convert
	walls=walls_convert
	
	return roads,walls


def naib_x_y(roads,walls):
	i=0
	x,y=0,0
	while i<len(roads):
		if i>x and roads[i]<>[]:
			x=i
		j=0
		while j<len(roads[i]):
			if roads[i][j]>y:
				y=roads[i][j]
			j+=1
		i+=1
		
	i=0
	while i<len(walls):
		if i>x and walls[i]<>[]:
			x=i
		j=0
		while j<len(walls[i]):
			if walls[i][j]>y:
				y=walls[i][j]
			j+=1
		i+=1
		
	return x,y

def poisk(x,y,list):
	list=list[x]
	i=0
	rez=False
	while i<len(list):
		if list[i]==y:
			rez=True
		i+=1
	return rez
def many_roads(roads,walls,naib_x,naib_y):
	x,y=0,0
	while x<=naib_x and y<=naib_y:	
		i=0
		rez=poisk(x,y,walls)
		if not rez:
			roads[x].append(y)
			
		if y<naib_y:
			y+=1
		else:
			x+=1
			y-=naib_y
	
	file=open('base_convert.txt','w')
	pickle.dump(roads, file)
	pickle.dump(walls, file)
	file.close
	print 'save completed'
	return roads,walls
def converted_in_map(roads,walls, naib_x,naib_y):
	map=[]
	i=0
	while i<naib_x+1:
		map.append([])
		j=0
		while j<naib_y+1:
			map[i].append(0)
			j+=1
		i+=1
	
	i=0
	while i<len(roads):
		j=0
		while j<len(roads[i]):
			map[i][roads[i][j]]=1
			j+=1
		i+=1
	
	i=0
	while i<len(walls):
		j=0
		while j<len(walls[i]):
			map[i][walls[i][j]]=2
			j+=1
		i+=1
	
	file=open('map.txt','w')
	pickle.dump(map, file)
	file.close
	print 'save completed'	
	
main()