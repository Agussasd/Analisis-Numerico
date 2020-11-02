import math as math
import numpy as npy

Padron = 99999# Padrn de un integrante del grupo

Thot = Padron / 100 + 300 #C
Tamb = 20 # temperatura ambiente en C

ni = 90 #nodos coordenada angular
nj = 20 #nodos coordenada radial
n = ni * nj # nodos totales

rext = 0.250 # radio externo del tubo en metros
wt = 0.015 # espesor de la pared del tubo en metros
rint = rext - wt # radio interno del tubo en metros
dr = wt / (nj - 1) # delta r de la malla en metros

ncc = round(0.04 * (ni - 1) / (2 * math.pi * rint)) #variable entera auxiliar

T = npy.zeros((ni, nj))
b = npy.zeros((n, 1) )
A = npy.zeros((n, n))

for i in range(0, ni):

	# Aplico condiciones de contorno
	# j=1 - nodos internos
	kx = 1 + nj * (i - 1)
	A[kx][kx] = 1
	if (i <= ncc or i > ni - ncc + 1):
		b[kx] = Thot * 0.931
	else:
		b[kx] = Tamb

	for j in range(1, nj):

		# Indices de los coeficientes de las ecuaciones
		kx = j + nj * (i - 1)
		kn = j + 1 + nj * (i - 1)
		ks = j - 1 + nj * (i - 1)
		ke = j + nj * i
		kw = j + nj * (i - 2)
		if ke > n:
			ke = ke - n
		if kw < 0:
			kw = kw + n

		# Coeficientes de las ecuaciones
		rj = rint + dr * (j - 1)
		df = 2 * math.pi * rj / (ni - 1)
		cn = 1 / dr ** 2 + 1 / (2 * dr * rj)
		ce = 1 / (rj ** 2 * df ** 2)
		cs = 1 / dr ** 2 - 1 / (2 * dr * rj)
		cw = 1 / (rj ** 2 * df ** 2)
		cx = -2 / dr ** 2 - 2 / (rj ** 2 * df ** 2)
		ci = 0

		#Matriz del sistema
		if ke < kx:
			A[kx][ke] = ce
		if kw < kx:
			A[kx][kw] = cw

		A[kx][ks] = cs
		A[kx][kx] = cx
		A[kx][kn] = cn


		if ke > kx:
			A[kx][ke] = ce

		if kw > kx:
			A[kx][kw] = cw

		#Vector terminos independientes
		b[kx] = ci


	# Aplico condiciones de contorno
	# j=nj - nodos externos
	kx = nj + nj * (i - 1)
	A[kx][kx] = 1
	if (i <= ncc or i > ni - ncc + 1):
		b[kx] = Thot
	else:
		b[kx] = Tamb