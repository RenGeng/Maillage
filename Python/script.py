# -*- coding: utf-8 -*-

# Importation numpy et dossiers
import os
import numpy
from deformation_affine import deformation

type_deformation=input("Veuillez entrer le type de deformation souhaité (affine,similaire ou rigide):\n")

# Ouverture fichier
file_mesh = open("../deformation/Polytech_maillage/mesh/man.mesh","r")

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
# Nous avons maintenant les cordonnées de chaque point dans la matrice mat_points

V = mat_points[:,0:2] # Matrice des points sans les références
P = numpy.zeros((5,2)) # Matrice des points de controles
P[0,:]=numpy.copy(V[99,:])
P[1,:]=numpy.copy(V[599,:])
P[2,:]=numpy.copy(V[1099,:])
P[3,:]=numpy.copy(V[1599,:])
P[4,:]=numpy.copy(V[2099,:])
Q = numpy.zeros((5,2)) # Matrice des points après déformation
Q[0,:]=0.8*numpy.copy(V[99,:])
Q[1,:]=0.8*numpy.copy(V[599,:])
Q[2,:]=0.8*numpy.copy(V[1099,:])
Q[3,:]=0.5*numpy.copy(V[1599,:])
Q[4,:]=0.1*numpy.copy(V[2099,:])

# Calcul des points sol
point_sol = numpy.zeros((nb_point,2))

# On parcourt tous les points
for i in range(nb_point):
	# Si le points considéré n'est pas un point à modifier on le modifie
	if V[i,:] not in P:
		point_sol[i,:]=deformation(P,V[i,:],Q,type_deformation)
	# Sinon on lui associe la nouvelle coordonnée
	else:
		for j in range(len(P)):
			
			if V[i,0]==P[j,0] and V[i,1]==P[j,1]:
				point_sol[i,:]=Q[j,:]-P[j,:]

# Ecriture dans le fichier.sol
file_sol = open("../deformation/Polytech_maillage/mesh/man.sol","w")
file_sol.write("MeshVersionFormatted 2\n\nDimension 2\n\nSolAtVertices\n"+str(nb_point)+"\n1 2\n\n")


for sol in point_sol:
	file_sol.write(str(sol[0])+" "+str(sol[1])+"\n")

file_sol.write("\nEnd")
file_sol.close()

os.system("medit-linux ../deformation/Polytech_maillage/mesh/man.mesh")

