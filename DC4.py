def getMissingInt(array):
	if not array:
		return 1

	array = getIntArray(array)

	for x in range(len(array)):
		if x not in array:
			return x


def getIntArray(array):
	i = 0
	j = len(array) - 1
	duplicates = set()

	while i < j:
		if(array[i] > 0 and array[j] <= 0):
			array[j] = array[i]
			i += 1
			j -= 1
		elif(array[i] > 0):
			j -= 1
		else:
			i += 1

	if array[i] > 0:
		pivot = i
	else:
		pivot = i + 1

	return array[pivot:]

array = [2, 4, 6, 1]
#print(getMissingInt(array))