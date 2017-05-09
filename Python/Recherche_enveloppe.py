# -*- coding: utf-8 -*-
# Marche de Jarvis ou methode de l'emballage cadeau

import numpy
import os
import sys
import time

# Marche de Jarvis ou methode de l'emballage cadeau

#from tkinter import *

def plus_a_gauche(points):
    # trouve parmi la liste points le pt le plus a gauche
    minx=points[0][0]
    gauche=points[0]
    for p in points:
        if p[0]<minx:
            minx=p[0]
            gauche=p
    return gauche


def sens_direct(a,b,c):
    # vrai si les points a, b, et c "tournent" dans le sens trigonometrique positif
    x1 = b[0]-a[0]
    y1 = b[1]-a[1]
    x2 = c[0]-a[0]
    y2 = c[1]-a[1]
    det = x1*y2 - x2*y1
    return det>0


def jarvis(points):
    # applique la methode de Jarvis
    # en partant du point le plus a gauche, on construit les points de
    # l'enveloppe convexe les uns apres les autres. Chaque point ajoute
    # doit pouvoir etre relie au precedent en ne laissant aucun point
    # a gauche de ce segment.
    env=[]
    gauche=plus_a_gauche(points)
    env.append(gauche)
    fin=False
    i=0
    while not fin:
        p = env[i]
        q = points[0]
        if p==q :
            q = points[1]
        for r in points:
            if sens_direct(p,q,r):
                q=r
        env.append(q)
        points.remove(q)
        i += 1
        fin = (env[0]==q)
    return env                    

#Demande du fichier
nom_fichier=sys.argv[1]

# Ouverture fichier
file_mesh = open("../deformation/Polytech_maillage/mesh/"+nom_fichier+".mesh","r")

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

# enveloppe convexe
points = mat_points.tolist()
env = jarvis(points)
# for point in env:
#     print(str(point[0]),str(point[1]))


file_env = open("enveloppe.mesh","w")
file_env.write("MeshVersionFormatted 1\n\nDimension 2\n\nVertices\n"+str(len(env))+"\n")

for i in env:
    file_env.write(str(i[0]))
    file_env.write(" ")
    file_env.write(str(i[1]))
    file_env.write("\n")

file_env.write("\nEdges\n")
file_env.write(str(len(env))+"\n")

for i in range(1,len(env)):
    file_env.write(str(i)+" "+str(i+1)+" 0\n")

file_env.write("End")

file_env.close()

