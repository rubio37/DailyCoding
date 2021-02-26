#include<stdio.h>

void printArray(int* array, int size){
	for (int i = 0; i < size; i++)
    	printf("%d", array[i]);

    printf("\n");
}

int findSmallestMissingNumber(int* array, int size) {
	
	if (size < 1) return 1;

	int val;

	for (int i = 0; i < size; i++) {
		while(true){
			val = array[i];
			if(val != i + 1 and val <= size and val > 0){
				if (val != array[val - 1]){
					array[i] = array[val - 1];
					array[val - 1] = val;
				} else{
					break;
				}
			} else{
				break;
			}
		}
	}

	printArray(array, size);

	for (int i = 0; i < size; i++){
		if(i + 1 != array[i]){
			return i + 1;
		}
	}

	return size + 1;
}

int main(int argc, char const *argv[]) {
	int array[] = {2, 4, 6, 1};
	int n = findSmallestMissingNumber(array, sizeof(array)/sizeof(array[0]));
	printf("%d\n", n);

	int array2[] = {2, 4, 6, 1, 2};
	n = findSmallestMissingNumber(array2, sizeof(array2)/sizeof(array2[0]));
	printf("%d\n", n);
	
	int array3[] = {2, 4, 6, 1, 2, -1, 0, 5, 3, 10};
	n = findSmallestMissingNumber(array3, sizeof(array3)/sizeof(array3[0]));
	printf("%d\n", n);
	
	int array4[] = {2, 4, 6, 1, 2, 1, 1, 1, 1, 3, 5, 7, 8, 9, -5, 123};
	n = findSmallestMissingNumber(array4, sizeof(array4)/sizeof(array4[0]));
	printf("%d\n", n);
	
	int array5[] = {};
	n = findSmallestMissingNumber(array4, sizeof(array5)/sizeof(array5[0]));
	printf("%d\n", n);

	return 1;
}