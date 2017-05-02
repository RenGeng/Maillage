import threading
import random
import os, sys
import numpy
import time

argument=sys.argv[1].split(',')
nomfichier_etat=True
P_etat=False
Q_etat=False
Point_P=[]
Point_Q=[]

for element in argument:
	if(nomfichier_etat==True):
		nomfichier=element
		nomfichier_etat=False

	elif(element=='P'):
		P_etat=True

	elif(element=='Q'):
		Q_etat=True
	
	elif(P_etat==True and Q_etat==False):
		P.append(float(element))

	elif(P_etat==True and Q_etat==True):
		Q.append(float(element))


mat_points = numpy.zeros((nb_point,2))


for i in range(0,len(Point_P),2):
	for j in range(len(mat_points)):
		if(abs(Point_P[i]-mat_points[i,0])<=0.1 and abs(Point_P[i+1]-mat_points[i,1])<=0.1):
			Point_P[i]=mat_points[i,0]			
			Point_P[i+1]=mat_points[i,1]
			break

