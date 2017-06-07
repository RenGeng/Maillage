# -*- coding: utf-8 -*-

# Importation numpy et dossiers
import threading
import random
import os, sys
import numpy
import time
from deformation_MLS import deformation

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
os.system('clear')
type_deformation=input("Veuillez entrer le type de deformation souhaité ('affine','similaire' ou 'rigide'), pour les trois en même temps écrivez 'all':\n")
while(type_deformation!="affine" and type_deformation!="rigide" and type_deformation!="similaire" and type_deformation!="all"):
	type_deformation=input("Saisis incorrecte veuillez recommencer ('affine','similaire' ou 'rigide'), pour les trois en même temps écrivez 'all':\n")

os.system('clear')
ouverture=input("Veuillez indiquer le type d'ouverture que vous voulez 'medit-linux' ou 'pygame':\n")
while(ouverture!="medit-linux" and ouverture!="pygame"):
	ouverture=input("Saisis incorrecte veuillez recommencer 'medit-linux' ou 'pygame':\n")

# Ouverture fichier
file_mesh = open("../mesh/mesh_2D/"+nom_fichier+".mesh","r")

#Lecture du fichier jusqu'à Vertices

while (file_mesh.readline()!="Vertices\r\n" and file_mesh.readline()!="Vertices\n"):
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

for i in range(0,len(Point_P),2):
	for j in range(len(mat_points)):
		if(abs(Point_P[i]-mat_points[j,0])<=0.0001 and abs(Point_P[i+1]-mat_points[j,1])<=0.0001):
			Point_P[i]=mat_points[j,0]			
			Point_P[i+1]=mat_points[j,1]
			break

# On compte le nombre de def que l'on souhaite
if type_deformation == "all":
	liste_def=["affine","similaire","rigide"]
else:
	liste_def=[type_deformation]

def application_deformation(type_deformation,nom_fichier,Point_P,Point_Q,nb_point,mat_points,ouverture):	

	
	# Nous avons maintenant les cordonnées de chaque point dans la matrice mat_points

	V = mat_points[:,0:2] # Matrice des points sans les références

	P=numpy.zeros((len(Point_P),2))
	for i in range(0,len(Point_P),2):
		P[i,0]=Point_P[i]
		P[i,1]=Point_P[i+1]


	Q=numpy.zeros((len(Point_Q),2))
	for i in range(0,len(Point_Q),2):
		Q[i,0]=Point_Q[i]
		Q[i,1]=Point_Q[i+1]

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
			point_sol[i,:]=deformation(P,V[i,:],Q,type_deformation,ouverture)			
		# Sinon on lui associe la nouvelle coordonnée
		else:							
			for j in range(len(P)):
				
				if V[i,0]==P[j,0] and V[i,1]==P[j,1]:
					point_sol[i,:]=Q[j,:]-P[j,:]
		

	if(ouverture=='pygame'):
		# Ecriture dans le fichier
		file_sol = open("../mesh/mesh_2D/"+nom_fichier+"_new.mesh","w")
		file_sol.write("MeshVersionFormatted 2\n\nDimension 2\n\nVertices\n"+str(nb_point)+"\n")


		for sol in point_sol:
			file_sol.write(str(sol[0])+" "+str(sol[1])+"\n")

		file_sol.write("\nEnd")
		file_sol.close()

		os.system("python2 affichage_mesh.py "+nom_fichier+"_new")
	elif(ouverture=='medit-linux'):
		# Ecriture dans le fichier.sol
		file_sol = open("../mesh/mesh_2D/"+nom_fichier+".sol","w")
		file_sol.write("MeshVersionFormatted 2\n\nDimension 2\n\nSolAtVertices\n"+str(nb_point)+"\n1 2\n\n")


		for sol in point_sol:
			file_sol.write(str(sol[0])+" "+str(sol[1])+"\n")

		file_sol.write("\nEnd")
		file_sol.close()

		os.system("./medit-linux ../mesh/mesh_2D/"+nom_fichier+".mesh &")


if type_deformation=="all":
	application_deformation("affine",nom_fichier,Point_P,Point_Q,nb_point,mat_points,ouverture)
	os.system('clear')
	application_deformation("similaire",nom_fichier,Point_P,Point_Q,nb_point,mat_points,ouverture)
	os.system('clear')
	application_deformation("rigide",nom_fichier,Point_P,Point_Q,nb_point,mat_points,ouverture)
	os.system('clear')

elif type_deformation=="affine" or type_deformation=="similaire" or type_deformation=="rigide":	
	application_deformation(type_deformation,nom_fichier,Point_P,Point_Q,nb_point,mat_points,ouverture)

else:
	print("Aucune déformation correcte trouvée")

