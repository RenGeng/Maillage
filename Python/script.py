# -*- coding: utf-8 -*-

import numpy
from deformation_affine import deformation_affine
# Ouverture fichier
file_mesh = open("../deformation/Polytech_maillage/mesh/man.mesh","r")


point = "Vertices"
msg_ignore = ""

while msg_ignore!=point:
	msg_ignore = file_mesh.readline().replace("\n","")


nb_point = int(file_mesh.readline())

mat = numpy.zeros((nb_point,3))

for i in range(nb_point):
	ligne = file_mesh.readline().replace("\n","")
	liste = ligne.split(" ")
	for j in range(3): # le range varie selon la dimension du mesh, 3 pour dimension 2 et 4 pour dimension 3
		mat[i,j] = liste[j] # Problème de précision, ne garde pas tous les décimaux
file_mesh.close()

V = mat[:,0:2] # Matrice des points sans les références
P = numpy.zeros((5,2)) # Matrice des points de controles
P[0,:]=V[100,:];
P[1,:]=V[600,:];
P[2,:]=V[1100,:];
P[3,:]=V[1600,:];
P[4,:]=V[2100,:];
print(numpy.linalg.norm(P[0,:])-V[0,:]**2)
Q = numpy.zeros((5,2)) # Matrice des points après déformation
Q[0,:]=0.2*V[100,:];
Q[1,:]=0.2*V[600,:];
Q[2,:]=0.3*V[1100,:];
Q[3,:]=0.3*V[1600,:];
Q[4,:]=0.4*V[2100,:];

a = deformation_affine(P,V[0,:],Q)

print(a)

point_sol = numpy.zeros((nb_point,2))







