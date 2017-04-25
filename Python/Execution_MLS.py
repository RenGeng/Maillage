# -*- coding: utf-8 -*-

# Importation numpy et dossiers
import threading
import random
import os, sys
import numpy
import time
from deformation_MLS import deformation
################################################
P=[]
Q=[]
i=3;
next=False

while i<2*int(sys.argv[2])+1:
	if next==False and sys.argv[i]!="next":
		P.append((float(sys.argv[i]),float(sys.argv[i+1])))
		i+=1
	elif next==True and sys.argv[i]!="next":
		Q.append((float(sys.argv[i]),float(sys.argv[i+1])))
		i+=1

	elif(sys.argv[i]=="next"):
		next=True
	i+=1
###############################################
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
nom_fichier=sys.argv[1]#input("Veuilez entrer le nom de la figure à modifier (sans l'extension):\n");

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

#############################################
i=0
P_final=numpy.zeros((len(P),2))
for pos_Px,pos_Py in P:
	for posx,posy in mat_points:
		print(posx,posy)
		if abs(pos_Px-posx)<0.01 and abs(pos_Py-posy)<0.01:
			P_final[i,0]=posx
			P_final[i,1]=posy
			i+=1
			break
###############################################

# On compte le nombre de def que l'on souhaite
if type_deformation == "all":
	liste_def=["affine","similaire","rigide"]
else:
	liste_def=[type_deformation]

def application_deformation(type_deformation,nom_fichier,P,Point_Q,nb_point,mat_points):	

	
	# Nous avons maintenant les cordonnées de chaque point dans la matrice mat_points

	V = mat_points[:,0:2] # Matrice des points sans les références
	##################################################
	Q=numpy.zeros((len(Point_Q),2))

	for i in range(len(Point_Q)):		
		Q[i,0]=Point_Q[i][0]
		Q[i,0]=Point_Q[i][1]	
	###############################################
	print(P,Q)	

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
			point_sol[i,:]=deformation(P,V[i,:],Q,type_deformation)			
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
# liste_coef_def=[]
# liste_pts_alea=[]
# for i in range(5):
	# #nb=random.random()
	# liste_pts_alea.append(random.randint(0,nb_point-1))
	# liste_coef_def.append(random.random())

if type_deformation=="all":
	application_deformation("affine",nom_fichier,P_final,Q,nb_point,mat_points)
	os.system('clear')
	application_deformation("similaire",nom_fichier,P_final,Q,nb_point,mat_points)
	os.system('clear')
	application_deformation("rigide",nom_fichier,P_final,Q,nb_point,mat_points)
	os.system('clear')

elif type_deformation=="affine" or type_deformation=="similaire" or type_deformation=="rigide":	
	application_deformation(type_deformation,nom_fichier,P_final,Q,nb_point,mat_points)

else:
	print("Aucune déformation correcte trouvée")

