import numpy as np
import math
from matplotlib import pyplot as plt

def FX(x, y):
	"""dVx/dt"""
	ecuacion_resuelta = (6.674e-11) * ((5972e+21)/(-4.670e+6-x)**2 + ((-y)**2)) * (math.cos(math.atan2(-y, (-4.670e+6 - (x)))))
	return ecuacion_resuelta

def FY(x, y):
	"""dVy/dt"""
	ecuacion_resuelta = (6.674e-11) * ((5972e+21)/(((-4.670e+6-x)**2) + ((-y)**2))) * (np.sin(np.arctan2(-y, -4.670e+6 - x)))
	return ecuacion_resuelta

def metodo_de_euler(h, tf):
	"""Recibe h que es el tamaño de pasos, y tf que es el tiempo final (periodo) y grafica x, y"""
	
	n = (tf / h) 
	n = int(n)
	vx = np.zeros(n)
	vy = np.zeros(n)
	x = np.zeros(n)
	y = np.zeros(n)

	x[0] = -11646000
	y[0] = 0
	vx[0] = 0
	vy[0] = 7558.746225

	for i in np.arange(0, n - 1):
		vx[i + 1] = vx[i] + h * FX(vx[i], vy[i])
		vy[i + 1] = vy[i] + h * FY(vx[i], vy[i])
		x[i + 1] = x[i] + h * vx[i + 1]
		y[i + 1] = y[i] + h * vy[i + 1]

	plt.plot(x, y)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Trayectoria')
	plt.show()

metodo_de_euler(1, 5798.779242)
