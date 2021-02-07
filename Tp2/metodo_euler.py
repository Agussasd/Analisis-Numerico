import numpy as np
import math
from matplotlib import pyplot as plt

def FX(x, y):
	"""dVx/dt"""
	ecuacion_resuelta = (6.674e-11) * ((5972e+21)/(((-4.670e+6-x)**2) + ((-y)**2))) * (np.cos(np.arctan2(-y, -4.670e+6 - x)))
	return ecuacion_resuelta

def FY(x, y):
	"""dVy/dt"""
	ecuacion_resuelta = (6.674e-11) * ((5972e+21)/(((-4.670e+6-x)**2) + ((-y)**2))) * (np.sin(np.arctan2(-y, -4.670e+6 - x)))
	return ecuacion_resuelta

def metodo_de_euler(h, tf):
	"""Recibe h que es el tamaño de pasos, y tf que es el tiempo final (periodo) y grafica x, y"""
	
	n = (tf / h) 
	n = int(n)
	x = np.zeros(n)
	y = np.zeros(n)
	x[0] = -1164600
	y[0] = 0

	for i in np.arange(0, n - 1):
		x[i + 1] = x[i] + h * FX(x[i], y[i])
		y[i + 1] = y[i] + h * FY(x[i], y[i])

	plt.plot(x, y)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Trayectoria')
	plt.show()

metodo_de_euler(1, 5798.779242)
