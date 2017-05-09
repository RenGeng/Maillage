# -*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *
from decimal import Decimal
import os, sys
pygame.init()  

#Demande du fichier
nom_fichier=raw_input("Veuilez entrer le nom de la figure à modifier (sans l'extension):\n");

# Ouverture fichier
file_mesh = open("../deformation/Polytech_maillage/mesh/"+nom_fichier+".mesh","r")

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

  
# run the game loop
Point_P=[]
Point_Q=[]
pos_P=(0,0)
pos_Q=(0,0)
nombre_point=0
Boucle=True
while Boucle==True:
    for event in pygame.event.get():

        #Quitter la fenetre
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #Gestion du clic gauche
        if event.type == MOUSEBUTTONDOWN:
        	if event.button == 1 and len(Point_P)<=len(Point_Q):       
        		Point_P.append((Decimal(event.pos[0])/Decimal(800),Decimal(event.pos[1])/Decimal(800)))   
                nombre_point+=1             

        #Gestion du clic droit
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 3 and len(Point_Q)<=len(Point_P):                 
                Point_Q.append((Decimal(event.pos[0])/Decimal(800),Decimal(event.pos[1])/Decimal(800)))  

        #Gestion de la touche Entrée
        if event.type == KEYDOWN:
            if event.key == K_RETURN:                
                Boucle=False      

        #Gestion de la touche Espace    
        if event.type == KEYDOWN:
            if event.key == K_SPACE and len(Point_P)>0 and len(Point_Q)>0 and len(Point_P)==len(Point_Q):
                pos_P=Point_P.pop()
                pos_Q=Point_Q.pop() 

        #Gestion du dessin des nouveaux et anciens points
        for posx,posy in Point_P:
            pygame.draw.circle(DISPLAYSURF, RED, (posx*800,posy*800), 4, 0)
        for posx,posy in Point_Q:
            pygame.draw.circle(DISPLAYSURF, BLUE, (posx*800,posy*800), 4, 0)

        #Traçage des segments
        if len(Point_P)==len(Point_Q):
            for i in range(len(Point_P)):
                pygame.draw.line(DISPLAYSURF, GREEN, (Point_P[i][0]*800,Point_P[i][1]*800),(Point_Q[i][0]*800,Point_Q[i][1]*800), 2)

        #Suppresion de points et de segment
        pygame.draw.circle(DISPLAYSURF, BLACK, (pos_P[0]*800,pos_P[1]*800), 4, 0)
        pygame.draw.circle(DISPLAYSURF, BLACK, (pos_Q[0]*800,pos_Q[1]*800), 4, 0)
        pygame.draw.line(DISPLAYSURF, BLACK, (pos_P[0]*800,pos_P[1]*800),(pos_Q[0]*800,pos_Q[1]*800), 2)

    pygame.display.update()

print("Point_P=",Point_P)
print("Point_Q=",Point_Q)
Args=(Point_P,Point_Q)
mess="python3 Execution_MLS.py \""+nom_fichier+",P"
for posx,posy in Point_P:
    mess=mess+","+str(posx)+","+str(posy)

mess=mess+",Q"
for posx,posy in Point_Q:
    mess=mess+","+str(posx)+","+str(posy)

#mess=mess[:-1]
mess=mess+"\""

print mess
os.system(mess)





