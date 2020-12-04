# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def sumaK(lista, k):
	complemento = set()

	for elemento in lista:
		if elemento in complemento:
			print(elemento, "+", k - elemento)
			return True
		complemento.add(k - elemento)

	print("No se encontro un conjunto de elemetnos que sume ", k)
	return False

sumaK([], 3)
sumaK([1, 2, 3], 5)
sumaK([1, 5, -8, 3], -3)
