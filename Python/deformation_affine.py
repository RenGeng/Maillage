# -*- coding: utf-8 -*-

import numpy

def deformation_affine(P,V,Q):
	alpha = 1
	n = P.shape[0] # Donne le nombre de ligne de P
	w = numpy.zeros((1,n))

	for i in range (n):
		w[0,i] = 1/numpy.linalg.norm(P[i,:]-V)**(2*alpha)

	px = numpy.zeros((1,2))
	qx = numpy.zeros((1,2))
	somwipi = numpy.mat("[0 0]")
	somwiqi = numpy.mat("[0 0]")
	somwi = 0;

	for i in range(n):
		somwipi = w[0,i]*P[i,:]+somwipi
		somwiqi = w[0,i]*P[i,:]+somwiqi
		somwi = w[0,i] + somwi

	px = somwipi/somwi
	qx = somwiqi/somwi

	pchap = numpy.zeros((n,2))
	qchap = numpy.zeros((n,2))

	for i in range(n):
		pchap[i,:] = P[i,:] - px
		qchap[i,:] = Q[i,:] - qx

	M1 = numpy.zeros((2,2))
	M2 = numpy.zeros((2,2))

	for i in range(n):
		M1 = numpy.transpose(pchap[i,:]) * w[0,i] * pchap[i,:]+M1
		M2 = w[0,i] * numpy.transpose(pchap[i,:]) * qchap[i,:]+M2

	#M1 = numpy.linalg.inv(M1)
	print("M1=",M1)

	f1 = (V-px)*M1*M2+qx

	return f1-V



	