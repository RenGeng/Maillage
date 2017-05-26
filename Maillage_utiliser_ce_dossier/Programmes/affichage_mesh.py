# -*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *
from decimal import Decimal
import os, sys
import math
pygame.init()  

argument=sys.argv[1].split(',')

nom_fichier=argument[0]
# Ouverture fichier
file_mesh = open("../mesh/mesh_2D/"+nom_fichier+".mesh","r")

#Lecture du fichier jusqu'à Vertices	
if(nom_fichier=="circle"):
    while file_mesh.readline()!="Vertices\r\n":
        file_mesh.readline()

else:
    while file_mesh.readline()!="Vertices\n":
        file_mesh.readline()

# Nombre de points du mesh
nb_point = int(file_mesh.readline())

# set up the window
DISPLAYSURF = pygame.display.set_mode((800, 800), 0, 32)
pygame.display.set_caption('Drawing')
  
# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)


for i in range(nb_point):
	ligne = file_mesh.readline().replace("\n","")	
	liste = ligne.split(" ")	
	pygame.draw.circle(DISPLAYSURF, WHITE, (int(round(float(liste[0])*800)),800-int(round(float(liste[1])*800))), 2, 0)

file_mesh.close()

if(len(argument)>1):
	if(argument[1]=="barycentre"):
		#On execute le programme pour chercher l'enveloppe convexe
		mess1="python3 Recherche_enveloppe.py "+nom_fichier+" 1"
		os.system(mess1)
		# Ouverture fichier
		file_mesh = open("enveloppe.mesh","r")

		#Lecture du fichier jusqu'à Vertices    
		if(nom_fichier=="circle"):
		    while file_mesh.readline()!="Vertices\r\n":
		        file_mesh.readline()

		else:
		    while file_mesh.readline()!="Vertices\n":
		        file_mesh.readline()

		# Nombre de points de l'enveloppe
		nb_point = int(file_mesh.readline())
		liste_point=[]

		for i in range(nb_point):
		    ligne = file_mesh.readline().replace("\n","")   
		    liste = ligne.split(" ")  
		    liste_point.append((float(liste[0]),float(liste[1])))  
		    pygame.draw.circle(DISPLAYSURF, RED, (int(round(float(liste[0])*800)),800-int(round(float(liste[1])*800))), 2, 0)
		    if(i>1):
		        pygame.draw.line(DISPLAYSURF, RED, (int(round(float(liste[0])*800)),800-int(round(float(liste[1])*800))),(int(round(float(point_precedent[0])*800)),800-int(round(float(point_precedent[1])*800))), 2)
		        point_precedent=liste
		    else:
		        premier_point=liste
		        point_precedent=liste

		pygame.draw.line(DISPLAYSURF, RED, (int(round(float(point_precedent[0])*800)),800-int(round(float(point_precedent[1])*800))),(int(round(float(premier_point[0])*800)),800-int(round(float(premier_point[1])*800))), 2)
		        
		file_mesh.close()


pygame.display.update()
while(1):
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()