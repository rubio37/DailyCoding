public class DCP04{
	
	public static void main(int argc, char const *argv[]) {
		int array[] = {2, 4, 6, 1};
		printf("\n%d"findSmallestMissingNumber(array));
		int array[] = {2, 4, 6, 1, 2};
		printf("\n%d"findSmallestMissingNumber(array));
		int array[] = {2, 4, 6, 1, 2, -1, 0, 5, 3, 10};
		printf("\n%d"findSmallestMissingNumber(array));
		int array[] = {2, 4, 6, 1, 2, 1, 1, 1, 1, 3, 5, 7, 8, 9, -5, 123};
		printf("\n%d"findSmallestMissingNumber(array));
		return 0;
	}

	public static int findSmallestMissingNumber(int[] array) {
		
		if (array == null || array.length < 1) return 1;

		int len = array.length;
		int val;

		for (int i = 0; i < len; i++) {
			while(true){
				val = array[i];
				if(val != i + 1 and val <= length and val > 0){
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

		for (int i = 0; i < len; i++){
			printf("%d", array[i]);
		}

		for (int i = 0; i < len; i++){
			if(i + 1 != array[i]){
				return i + 1;
			}
		}

		return len + 1;

	}

}