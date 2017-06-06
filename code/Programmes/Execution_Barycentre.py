# -*- coding: utf-8 -*-

import numpy
import os
import time
import sys
from math import sqrt
from deformation_Barycentre import *


################################################
#Décriptage des arguments#
argument=sys.argv[1].split(',')
nom_fichier_etat=True
P_etat=False
Q_etat=False
Point_P=[]
Point_Q=[]

for element in argument:
	if(nom_fichier_etat==True):
		nom_fichier=element
		nom_fichier_etat=False

	elif(element=='P'):
		P_etat=True

	elif(element=='Q'):
		Q_etat=True
	
	elif(P_etat==True and Q_etat==False):
		Point_P.append(float(element))

	elif(P_etat==True and Q_etat==True):
		Point_Q.append(float(element))

print(Point_P)
print(Point_Q)
###############################################

def printProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

os.system('clear')
ouverture=input("Veuillez indiquer le type d'ouverture que vous voulez 'medit' ou 'pygame':\n")
while(ouverture!="medit" and ouverture!="pygame"):
	ouverture=input("Saisis incorrecte veuillez recommencer 'medit' ou 'pygame':\n")

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


# Ouverture fichier
file_mesh = open("enveloppe.mesh","r")

#Lecture du fichier jusqu'à Vertices    
if(nom_fichier=="circle"):
    while file_mesh.readline()!="Vertices\r\n":
        file_mesh.readline()

else:
    while file_mesh.readline()!="Vertices\n":
        file_mesh.readline()

# Nombre de points du mesh
nb_point_env = int(file_mesh.readline())
mat_env= numpy.zeros((nb_point_env,2))
for i in range(nb_point_env):
    ligne = file_mesh.readline().replace("\n","")   
    liste = ligne.split(" ")  
    mat_env[i,0]=liste[0]
    mat_env[i,1]=liste[1]

new_mat_env=numpy.copy(mat_env)
for i in range(0,len(Point_P),2):
	for j in range(len(mat_env)):
		#time.sleep(1)
		#print("Point",i,"j=",j,"\nPoint_P[i][0]-liste_point[j][0]",Point_P[i]-mat_env[j,0],"\nPoint_P[i][1]-liste_point[j][1]",Point_P[i+1]-mat_env[j,1],"\n")

		if(abs(Point_P[i]-mat_env[j,0])<0.000001 and abs(Point_P[i+1]-mat_env[j,1])<0.000001):
			#print("trouvé")
			new_mat_env[j,0]=Point_Q[i]
			new_mat_env[j,1]=Point_Q[i+1]
			break


#Calcul point sol
point_sol = numpy.zeros((nb_point,2))
#os.system('clear')

#print("type mat_points=",type(mat_points),"type mat_env=",type(mat_env),"type new_mat_env=",type(new_mat_env),"nb_point_env = ",nb_point_env,"nb_point=",nb_point)

os.system('clear')
for i in range(nb_point):
	os.system('clear')
	printProgressBar(i,nb_point, prefix = 'Calcul des nouveaux points en déformation ', suffix = 'Complete', decimals = 1, length = 100, fill = '█')
	point_sol[i,:]=vect_new_point(mat_points[i,:],mat_env,nb_point_env,new_mat_env,ouverture)

if(ouverture=="pygame"):
	# Ecriture dans le fichier.sol
	file_sol = open("../mesh/mesh_2D/"+nom_fichier+"_new.mesh","w")
	file_sol.write("MeshVersionFormatted 2\n\nDimension 2\n\nVertices\n"+str(nb_point)+"\n")


	for sol in point_sol:
		file_sol.write(str(sol[0])+" "+str(sol[1])+"\n")
		

	file_sol.write("\nEnd")
	file_sol.close()
	os.system("python2 affichage_mesh.py "+nom_fichier+"_new,barycentre")
elif(ouverture=="medit"):
	# Ecriture dans le fichier.sol
	file_sol = open("../mesh/mesh_2D/"+nom_fichier+".sol","w")
	file_sol.write("MeshVersionFormatted 2\n\nDimension 2\n\nSolAtVertices\n"+str(nb_point)+"\n1 2\n\n")


	for sol in point_sol:
		file_sol.write(str(sol[0])+" "+str(sol[1])+"\n")
		

	file_sol.write("\nEnd")
	file_sol.close()

	os.system("./medit-linux ../mesh/mesh_2D/"+nom_fichier+".mesh &")