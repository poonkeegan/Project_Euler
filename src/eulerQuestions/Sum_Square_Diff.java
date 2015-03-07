package eulerQuestions;

public class Sum_Square_Diff {

	public static void main(String[] args) {
		int sumOfSq = 0;
		int sqOfSum = 0;
		for(int i = 1; i <= 100; i++){
			sumOfSq += i*i;
			sqOfSum += i;
		}
		sqOfSum *= sqOfSum;
		System.out.println(sqOfSum - sumOfSq);
	}

}
