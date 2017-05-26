# -*- coding: utf-8 -*-

import numpy
import time
from math import sqrt

def vect_new_point(p,Q,nb_cote_Q,new_Q,ouverture):
	sumW=0
	liste_alpha=[]

	#Initialisation de W avec des 0
	W=[]
	for j in range(nb_cote_Q):
		W.append(0)
		liste_alpha.append(0)

	for j in range(nb_cote_Q-1):	
		#print("j=",j,"\n","Q[0,:],Q[len(Q)-1,:]",Q[0,:],Q[len(Q)-1,:])
		if(j==0):
			W[j]=(cotangent(p,Q[0,:],Q[len(Q)-2,:])+cotangent(p,Q[0,:],Q[1,:]))/(numpy.linalg.norm(p-Q[0,:])**2)
		else:
			W[j]=(cotangent(p,Q[j,:],Q[j-1,:])+cotangent(p,Q[j,:],Q[j+1,:]))/(numpy.linalg.norm(p-Q[j,:])**2)

		sumW+=W[j]

		
	for i in range(nb_cote_Q):
		liste_alpha[i]=W[i]/sumW

	new_p=numpy.zeros((1,2))

	for j in range(nb_cote_Q):	
		new_p=new_Q[j,:]*liste_alpha[j]+new_p

	if(ouverture=="pygame"):
		return new_p
	elif(ouverture=="medit-linux"):
		return new_p-p

def cotangent(a,b,c):
	ba=numpy.zeros((1,2))
	bc=numpy.zeros((1,2))
	ba=a-b
	bc=c-b
	#time.sleep(1)
	#print("numpy.linalg.norm(numpy.cross(bc,ba)))=",numpy.linalg.norm(numpy.cross(bc,ba)),"bc=",bc,"ba=",ba)
	return((ba[0]*bc[0]+ba[1]*ba[1])/numpy.linalg.norm(numpy.cross(bc,ba)))


