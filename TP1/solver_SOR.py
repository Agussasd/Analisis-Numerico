import math as math
import numpy as np
import csv
import time # Para calcular el tiempo de ejecucion
import pandas as pd # Para leer las matrices

# Leo las matrices A y b y las guardo
matrizA = pd.read_csv('A_180_020.csv', header=None, index_col=None, delimiter=',', dtype=float)
A = matrizA.values
matrizB = pd.read_csv('b_180_020.csv', header=None, index_col=None, delimiter=',', dtype=float)
b = matrizB.values

w = 1.72
tol = 0.1
n = len(A) #dimension de matriz

def solver_SOR(A, b, w, hallarwoptimo = False):
	
	error = 2  * tol
	x = np.zeros(n, dtype = float)
	diferencia = np.zeros(n, dtype = float)
	iteraciones = 0
	lista_errores = []
	
	while not error <= tol:
		for i in range(0, n):
			suma = 0.0
			suma2 = 0.0
			for j in range(0, i):
				if j != i:
					suma = suma + A[i][j] * x[j]
			for j in range(i, n):
				if j != i:
					suma2 = suma2 + A[i][j] * x[j]
			R = b[i] - suma - suma2
			nuevo = x[i] * (1 - w) + (w / A[i][i]) * R
			diferencia[i] = np.abs(nuevo - x[i])
			x[i] = nuevo

		error = np.max(diferencia)
		lista_errores.append(error)
		iteraciones = iteraciones + 1 #cuento iteraciones
		lista_errores.append(error)

	df = pd.DataFrame(lista_errores)
	df.to_csv('lista_errores.csv')
	
	print("w: {} itera: {} veces\n\n".format(w, iteraciones))
	
	if hallarwoptimo:
		return iteraciones
		
def hallar_w_optimo():
	"""Ejecuta SOR para 9 w distintos, devuelve las iteraciones y cuanto tarda cada uno"""
	i = 1
	while i <= 9:
		decimal = i / 10
		w = 1 + decimal
		tiempo_inicial = time.time()
		iteraciones = solver_SOR(A, b, w, True)
		tiempo_total = time.time() - tiempo_inicial
		print("w: {} itera: {} veces y tarda: {}".format(w, iteraciones, tiempo_total))
		i += 1
	
#tiempo_inicial = time.time()
solver_SOR(A, b, w)
#tiempo_total = time.time() - tiempo_inicial
#print("\ntarda: {}".format(tiempo_total))
