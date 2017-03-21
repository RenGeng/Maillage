# -*- coding: utf-8 -*-

# Importation numpy et dossiers
import threading
import random
import os
import numpy
import time
from deformation_affine import deformation

# Print iterations progress
def printProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

type_deformation=input("Veuillez entrer le type de deformation souhaité ('affine','similaire' ou 'rigide'), pour les trois en même temps écrivez 'all':\n")
nom_fichier=input("Veuilez entrer le nom de la figure à modifier (sans l'extension):\n");

# Ouverture fichier
file_mesh = open("../deformation/Polytech_maillage/mesh/"+nom_fichier+".mesh","r")

#Lecture du fichier jusqu'à Vertices	
while file_mesh.readline()!="Vertices\n":		
	file_mesh.readline()

# Nombre de points du mesh
nb_point = int(file_mesh.readline())



# Initialisation de la matrice contenant les points du mesh
mat_points = numpy.zeros((nb_point,2))
os.system('clear')
for i in range(nb_point):
	printProgressBar(i,nb_point, prefix = 'Lecture de '+nom_fichier, suffix = 'Complete', decimals = 1, length = 100, fill = '█')
	ligne = file_mesh.readline().replace("\n","")	
	liste = ligne.split(" ")
	mat_points[i,0]=liste[0]
	mat_points[i,1]=liste[1]	

file_mesh.close()

# On compte le nombre de def que l'on souhaite
if type_deformation == "all":
	liste_def=["affine","similaire","rigide"]
else:
	liste_def=[type_deformation]

def application_deformation(type_deformation,nom_fichier,liste_coef_def,liste_pts_alea,nb_point,mat_points):	

	
	# Nous avons maintenant les cordonnées de chaque point dans la matrice mat_points

	V = mat_points[:,0:2] # Matrice des points sans les références
	P = numpy.zeros((5,2)) # Matrice des points de controles
	P[0,:]=V[liste_pts_alea[0],:]
	P[1,:]=V[liste_pts_alea[1],:]
	P[2,:]=V[liste_pts_alea[2],:]
	P[3,:]=V[liste_pts_alea[3],:]
	P[4,:]=V[liste_pts_alea[4],:]
	Q = numpy.zeros((5,2)) # Matrice des points après déformation
	Q[0,:]=liste_coef_def[0]*V[liste_pts_alea[0],:]
	Q[1,:]=liste_coef_def[1]*V[liste_pts_alea[1],:]
	Q[2,:]=liste_coef_def[2]*V[liste_pts_alea[2],:]
	Q[3,:]=liste_coef_def[3]*V[liste_pts_alea[3],:]
	Q[4,:]=liste_coef_def[4]*V[liste_pts_alea[4],:]

	# Calcul des points sol
	point_sol = numpy.zeros((nb_point,2))

	os.system('clear')
	# On parcourt tous les points
	for i in range(nb_point):
		printProgressBar(i,nb_point, prefix = 'Calcul des nouveaux points en déformation '+type_deformation, suffix = 'Complete', decimals = 1, length = 100, fill = '█')
		#os.system('clear')
		#print("Calcul des nouveux points\n",str(i*100//nb_point),"%\n")
		# Si le points considéré n'est pas un point à modifier on le modifie
		if V[i,0] not in P[:,0] or V[i,1] not in P[:,1]:
			point_sol[i,:]=deformation(P,V[i,:],Q,type_deformation,i)			
		# Sinon on lui associe la nouvelle coordonnée
		else:							
			for j in range(len(P)):
				
				if V[i,0]==P[j,0] and V[i,1]==P[j,1]:
					point_sol[i,:]=Q[j,:]-P[j,:]
		

	# Ecriture dans le fichier.sol
	file_sol = open("../deformation/Polytech_maillage/mesh/"+nom_fichier+".sol","w")
	file_sol.write("MeshVersionFormatted 2\n\nDimension 2\n\nSolAtVertices\n"+str(nb_point)+"\n1 2\n\n")


	for sol in point_sol:
		file_sol.write(str(sol[0])+" "+str(sol[1])+"\n")

	file_sol.write("\nEnd")
	file_sol.close()

	os.system("medit-linux ../deformation/Polytech_maillage/mesh/"+nom_fichier+".mesh &")

# On lance la fonction des deformations autant de fois que souhaité
liste_coef_def=[]
liste_pts_alea=[]
for i in range(5):
	#nb=random.random()
	liste_pts_alea.append(random.randint(0,nb_point-1))
	liste_coef_def.append(random.random())

if type_deformation=="all":
	application_deformation("affine",nom_fichier,liste_coef_def,liste_pts_alea,nb_point,mat_points)
	os.system('clear')
	application_deformation("similaire",nom_fichier,liste_coef_def,liste_pts_alea,nb_point,mat_points)
	os.system('clear')
	application_deformation("rigide",nom_fichier,liste_coef_def,liste_pts_alea,nb_point,mat_points)
	os.system('clear')

elif type_deformation=="affine" or type_deformation=="similaire" or type_deformation=="rigide":	
	application_deformation(type_deformation,nom_fichier,liste_coef_def,liste_pts_alea,nb_point,mat_points)

else:
	print("Aucune déformation correcte trouvée")

