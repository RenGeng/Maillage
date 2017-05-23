# -*- coding: utf-8 -*-

import numpy
from math import sqrt

def deformation(P,V,Q,deformation):
	alpha = 1
	n = len(P)
	w = numpy.zeros((1,n))


	for i in range(n):
		
		w[0,i] = 1./(numpy.linalg.norm(P[i,:]-V)**(2*alpha))

	px = numpy.zeros((1,2))
	qx = numpy.zeros((1,2))
	somwipi = numpy.mat("[0 0]")
	somwiqi = numpy.mat("[0 0]")
	somwi = 0;

	for i in range(n):
		somwipi = w[0,i]*P[i,:]+somwipi
		somwiqi = w[0,i]*Q[i,:]+somwiqi
		somwi = w[0,i] + somwi

	px = somwipi/float(somwi)
	qx = somwiqi/float(somwi)
	

	pchap = numpy.zeros((n,2))
	qchap = numpy.zeros((n,2))

	for i in range(n):
		pchap[i,:] = P[i,:] - px
		qchap[i,:] = Q[i,:] - qx

	if deformation=="affine":

		M1 = numpy.zeros((2,2))
		M2 = numpy.zeros((2,2))
		
		for i in range(n):
			
			M1 = numpy.transpose(numpy.mat(pchap[i,:])) * w[0,i] * pchap[i,:]+M1
			M2 = w[0,i] * numpy.transpose(numpy.mat(pchap[i,:])) * qchap[i,:]+M2
		
		M1 = numpy.linalg.inv(M1)
		f1 = (V-px)*M1*M2+qx

	elif deformation=="similaire":

		nu=0
		for i in range(n):
			nu=w[0,i]*pchap[i,:]*numpy.transpose(numpy.mat(pchap[i,:]))+nu

		A2=numpy.zeros((2,2))
		A2[0,:]=V-px		
		A2[1,:]=-ortho(A2[0,:])
		A2=numpy.transpose(numpy.mat(A2))
		f1=numpy.zeros((1,2))

		for i in range(n):
			A1=numpy.zeros((2,2))
			A1[0,:]=pchap[i,:]
			A1[1,:]=-ortho(pchap[i,:])
			f1=numpy.mat(qchap[i,:])*(1/float(nu))*w[0,i]*numpy.mat(A1)*numpy.mat(A2)+f1

		f1=f1+qx

	elif deformation=="rigide":
		A2=numpy.zeros((2,2))
		A2[0,:]=V-px		
		A2[1,:]=-ortho(A2[0,:])
		A2=numpy.transpose(numpy.mat(A2))
		fr1=numpy.zeros((1,2))

		for i in range(n):
			A1=numpy.zeros((2,2))
			A1[0,:]=pchap[i,:]
			A1[1,:]=-ortho(pchap[i,:])
			fr1=numpy.mat(qchap[i,:])*w[0,i]*numpy.mat(A1)*numpy.mat(A2)+fr1

		f1=(numpy.linalg.norm(V-px)*fr1/numpy.linalg.norm(fr1))+qx

	return f1-V

def ortho(V):
	#x,y => -y,x
	vect=numpy.zeros((1,2))
	V=numpy.mat(V)
	vect[0,0]=-V[0,1]
	vect[0,1]=V[0,0]
	return vect

