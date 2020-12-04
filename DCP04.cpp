public class DCP04{
	
	public static void main(int argc, char const *argv[]) {
		findSmallestMissingNumber();
		findSmallestMissingNumber();		
		return 0;
	}

	public static int findSmallestMissingNumber(int[] array) {
		
		if (array == null || array.length < 1) return 1;

		int len = array.length;
		int smallestNum = 1;
		int aux;

		for (int i = 0; i < len; ++i) {
			if (array[i] > len || array[i] < 1) break;

			while(true) {
				if(array[i] == i + 1) break;
				aux = array[i];
				a
			}

		}

		return smallestNum;

	}

}