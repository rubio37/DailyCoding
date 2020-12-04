#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#or example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

import numpy as np

def ListaMultiplicada(lista):
	if (len(lista) < 2):
		return None

	zeros = lista.count(0)

	if(zeros > 1):
		return np.zeros(len(lista), int, 'C')

	listaProducto = []

	total = 1
	for i in lista:
		if(i != 0):
			total *= i

	if(zeros == 1):
		for i in lista:
			if(i == 0):
				listaProducto.append(total)
			else:
				listaProducto.append(0)
		return listaProducto


	for i in lista:
		listaProducto.append(total / i)

	return listaProducto

print(ListaMultiplicada([]))
print(ListaMultiplicada([1, 2, 3, 4, 5]))
print(ListaMultiplicada([3, 2, 1]))
print(ListaMultiplicada([3, 2, 1, 0]))
print(ListaMultiplicada([3, 2, 1, 0, 0]))
