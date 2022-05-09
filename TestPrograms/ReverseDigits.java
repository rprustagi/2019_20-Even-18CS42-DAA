public class ReverseDigits {
   public static void main(String[] args) {
      int num = 987654321;
      String str = "";

      while (num > 0) {
      	int digit = num % 10;
	str = str + digit;
	num = num /10;
      }
      System.out.println(str);
   }
}
