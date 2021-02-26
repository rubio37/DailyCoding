def getMissingInt(array):
	if not array:
		return 1

	length = len(array)

	for i in range(length):
		while(True):
			val = array[i]
			if(val != i+1 and val <= length and val > 0):
				if(val != array[val - 1]):
					array[i] = array[val - 1]
					array[val - 1] = val
				else:
					break
			else:
				break

	print(array)

	for i in range(length):
		if(i + 1 != array[i]):
			return i + 1

	return length + 1


array = [2, 4, 6, 1]
print(getMissingInt(array))
array = [2, 4, 6, 1, 2]
print(getMissingInt(array))
array = [2, 4, 6, 1, 2, -1, 0, 5, 3, 10]
print(getMissingInt(array))
array = [2, 4, 6, 1, 2, 1, 1, 1, 1, 3, 5, 7, 8, 9, -5, 123]
print(getMissingInt(array))
array = []
print(getMissingInt(array))