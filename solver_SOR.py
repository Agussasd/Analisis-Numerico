import math as math
import numpy as np

K = [[4.0, -1.0, -1.0, 0.0], [-1.0, 4.0, 0.0, -1.0], [-1.0, 0.0, 4.0, -1.0], [0.0, -1.0, -1.0, 4.0]]
v = [1.0, 2.0, 0.0, 1.0]
x = [0.0, 0.0, 0.0, 0.0]
#Resultado = [0.5, 0.75, 0.25, 0.5]
tol = 0.1
w = 1.2
n = 4 #dimension de matriz

def SOR(A, b):
	error = 2  * tol
	diferencia = np.zeros(n, dtype = float)
	iteraciones = 0
	while not error <= tol:
		for i in range(0, n):
			suma = 0.0
			suma2 = 0.0
			for j in range(0, i):
				suma = suma + A[i][j] * x[j]
			for j in range(i, n):
				suma2 = suma2 + A[i][j] * x[j]
			R = b[i] - suma - suma2
			nuevo = x[i] * (1 - w)+ (w / A[i][i]) * R
			diferencia[i] = np.abs(nuevo - x[i])
			x[i] = nuevo

		error = np.max(diferencia)
		iteraciones = iteraciones + 1 #cuento iteracioneses

	print(iteraciones)
	print(x)

SOR(K, v)