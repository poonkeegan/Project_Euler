package eulerQuestions;

public class Pythagorean_triplet {
	public static void main(String[] args) {
		for(int a = 0; a < 1000; a ++){
			
			for(int b = 0; a + b +( Math.sqrt(a*a + b*b))<=1000; b++){
				if(a+b+Math.sqrt(a*a + b*b)==1000){
					System.out.printf("%f",a*b*Math.sqrt(a*a + b*b));
					System.out.println();
				}
			}
		}
	}
}
