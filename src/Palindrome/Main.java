package Palindrome;

public class Main {

	public static void main(String[] args) {
		int greatest = 0;
		// TODO Auto-generated method stub
		for(int i = 0; i < 1000; i++){
			for(int j = 0; j < 1000; j++){
				if(palindrome(Integer.toString(i*j))){
					if(i*j > greatest){
						greatest = i*j;
					}
				}
			}
		}
		System.out.println(greatest);
	}
	
	
	public static boolean palindrome(String val){
		char[] set = val.toCharArray();
		boolean isIt = true;
		for(int i = 0, j = set.length-1; i < j; i++, j--){
			if(set[i] != set[j]){
				isIt = false;
				j = 0;
			}
		}
		return isIt;
	}

}
