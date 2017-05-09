# -*- coding: utf-8 -*-

import numpy
from math import sqrt

def vect_new_point(p,Q,nb_cote_Q,new_Q):
	sumW=0
	liste_alpha=[]

	#Initialisation de W avec des 0
	W=[]
	for j in range(nb_cote_Q):
		W.append(0)

	for j in range(1,nb_cote_Q+1):	
		#Calcul de 1 à n-1 et le dernier est 0	
		prec=(j+nb_cote_Q-1)%nb_cote_Q
		suiv=(j+1)%nb_cote_Q
		#print("suiv=",suiv,"prec=",prec,"j=",j,"Q[j:b_cote_Q,:]=",Q[j%nb_cote_Q,:],"Q[prec,:]=",Q[prec,:],"Q[suiv,:]=",Q[suiv,:])
		W[j%nb_cote_Q]=((cotangent(p,Q[j%nb_cote_Q,:],Q[prec,:])+cotangent(p,Q[j%nb_cote_Q,:],Q[suiv,:]))/(numpy.linalg.norm(p-Q[j%nb_cote_Q,:])**2))
		#print("\n----------------------\n")
		sumW+=W[j%nb_cote_Q]

	if(numpy.linalg.norm(p-Q[j%nb_cote_Q,:])**2==0):
		print("*******************************************")
		print("NORM",numpy.linalg.norm(p-Q[j%nb_cote_Q,:])**2)
		print("*******************************************")
	#print("W=",W,"sumW=",sumW)

	for weight in W:
		liste_alpha.append(weight/sumW)


	new_p=numpy.zeros((1,2))

	for j in range(nb_cote_Q):		
		new_p=new_Q[j,:]*liste_alpha[j]+new_p

	#print("p=",p,"\nnew_p=",new_p,"\n\n")
	return new_p-p

def cotangent(a,b,c):
	ba=numpy.zeros((1,2))
	bc=numpy.zeros((1,2))
	# print("*******************************************")
	# print("a=",a,"b=",b,"c=",c)
	# print("*******************************************")
	ba=a-b
	bc=c-b
	# print("*********************************************************")
	# print("ba=",ba,"bc=",bc,"norm=",numpy.linalg.norm(numpy.cross(bc,ba)))
	# print("*********************************************************")
	# print("\n \n \n \n ")
	# print("ba[0]:",ba[0])
	return((ba[0]*bc[0]+ba[1]*ba[1])/numpy.linalg.norm(numpy.cross(bc,ba)))


