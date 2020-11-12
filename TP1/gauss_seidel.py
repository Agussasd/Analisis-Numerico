import math as math
import numpy as np
import pandas as pd

tolerancia = 0.1

df = pd.read_csv('A_090_010.csv', header=None, index_col=None, delimiter=',', dtype=float)
A = df.values

df2 = pd.read_csv('b_090_010.csv', header=None, index_col=None, delimiter=',', dtype=float)
b = df2.values

n = len(A)

def gauss_seidel(A, b):
	x = np.zeros(n, dtype = float)
	diferencia = np.ones(n, dtype = float)
	errado = 2  * tolerancia
	iteracion = 0
	i = 0
	while not (errado <= tolerancia):
		for i in range(0, n):
			suma = 0.0
			for j in range(0, n):
				if j != i and A[i][j] != 0:
					suma = suma + A[i][j] * x[j]
			nuevo = (b[i] - suma) / A[i][i]
			diferencia[i] = np.abs(nuevo - x[i])
			x[i] = nuevo
		errado = np.max(diferencia)
		iteracion += 1
		print("El error es de: {}".format(errado))
	print(x)
	print(iteracion)

gauss_seidel(A, b)