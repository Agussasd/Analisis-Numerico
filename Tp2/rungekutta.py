import numpy as np
import math
from matplotlib import pyplot as plt

h = 1

def FVX(x, y):
	"""dVx/dt"""
	alf1 = np.arctan2(-y, -4.670e+6 - x)
	ecuacion_resuelta = (6.674e-11) * ((5972e+21)/(((-4.670e+6-x)**2) + ((-y)**2))) * np.cos(alf1)
	return ecuacion_resuelta

def FVY(x, y):
	"""dVy/dt"""
	alf1 = np.arctan2(-y, -4.670e+6 - x)
	ecuacion_resuelta = (6.674e-11) * ((5972e+21)/(((-4.670e+6-x)**2) + ((-y)**2))) * np.sin(alf1)
	return ecuacion_resuelta

def rk2(h, tf):
	"""Recibe h que es el tamaño de pasos, y tf que es el tiempo final (periodo) y grafica x, y"""
	
	n = (tf / h) 
	n = int(n)
	vx_pred = np.zeros(n)
	vx = np.zeros(n)
	vy_pred = np.zeros(n)
	vy = np.zeros(n)
	x_pred = np.zeros(n)
	x = np.zeros(n)
	y_pred = np.zeros(n)
	y = np.zeros(n)
	Em = np.zeros(n - 1)

	x[0] = -11646000
	y[0] = 0
	vx[0] = 0
	vy[0] = 7558.746225

	for i in np.arange(0, n - 1):
		vx_pred[i + 1] = vx[i] + h * FVX(x[i], y[i])
		vx[i + 1] = vx[i] + h/2 * ((FVX(x[i], y[i]) + FVX(vx_pred[i + 1], y_pred[i + 1])))

		vy_pred[i + 1] = vy[i] + h * FVY(x[i], y[i])
		vy[i + 1] = vy[i] + h/2 * ((FVY(x[i], y[i]) + FVY(vx_pred[i + 1], vy_pred[i + 1])))

		x_pred[i + 1] = x[i] + h * vx[i]
		x[i + 1] = x[i] + h/2 * ((vx[i] + vx[i + 1]))

		y_pred[i + 1] = y[i] + h * vy[i]
		y[i + 1] = y[i] + h/2 * ((vy[i] + vy[i + 1]))
		#Em[i] = (1/2 * (vx[i]**2 + vy[i]**2)) - 6.674e-11 * 5972e21 / math.sqrt((-4.670e6-x[i])**2 + (-y[i])**2)

	plt.plot(x, y)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Trayectoria con h = {}'.format(h))
	plt.show()

rk2(h, 5799)