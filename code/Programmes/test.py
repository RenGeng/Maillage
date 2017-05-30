# -*- coding: utf-8 -*-

import numpy
import os
import time
from math import sqrt
from test_bary import *

def printProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

#Demande du fichier
nom_fichier=input("Veuilez entrer le nom de la figure à modifier (sans l'extension):\n");

# Ouverture fichier
file_mesh = open("../mesh/mesh_2D/"+nom_fichier+".mesh","r")

#Lecture du fichier jusqu'à Vertices	
while file_mesh.readline()!="Vertices\n":	

	file_mesh.readline()

# Nombre de points du mesh
nb_point = int(file_mesh.readline())

# Initialisation de la matrice contenant les points du mesh
mat_points = numpy.zeros((nb_point,2))

for i in range(nb_point):
	ligne = file_mesh.readline().replace("\n","")	
	liste = ligne.split(" ")
	mat_points[i,0]=liste[0]
	mat_points[i,1]=liste[1]	

file_mesh.close()

#Initialisation de Q en faisant un carré autour de la figure
max_x=numpy.max(mat_points[:,0])+0.1
min_x=numpy.min(mat_points[:,0])-0.1
max_y=numpy.max(mat_points[:,1])+0.1
min_y=numpy.min(mat_points[:,1])-0.1

mess="["+str(min_x)+" "+str(max_y)+";"+str(max_x)+" "+str(max_y)+";"+str(max_x)+" "+str(min_y)+";"+str(min_x)+" "+str(min_y)+"]"
Q=numpy.mat(mess)
nb_cote_Q=len(Q)
new_Q=numpy.copy(Q)
new_Q[1,:]=new_Q[1,:]*1.5
new_Q[3,:]=new_Q[3,:]*0.5

#Calcul point sol
point_sol = numpy.zeros((nb_point,2))
os.system('clear')
for i in range(nb_point):
	printProgressBar(i,nb_point, prefix = 'Calcul des nouveaux points', suffix = 'Complete', decimals = 1, length = 100, fill = '█')
	point_sol[i,:]=vect_new_point(mat_points[i,:],Q,nb_cote_Q,new_Q)

# Ecriture dans le fichier.sol
file_sol = open("../mesh/mesh_2D/"+nom_fichier+".sol","w")
file_sol.write("MeshVersionFormatted 2\n\nDimension 2\n\nSolAtVertices\n"+str(nb_point)+"\n1 2\n\n")


for sol in point_sol:
	file_sol.write(str(sol[0])+" "+str(sol[1])+"\n")

file_sol.write("\nEnd")
file_sol.close()

os.system("medit-linux ../mesh/mesh_2D/"+nom_fichier+".mesh &")