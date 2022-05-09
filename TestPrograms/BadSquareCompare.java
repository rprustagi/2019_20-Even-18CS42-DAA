public class BadSquareCompare {
   public static void main(String[] args) {
      //System.out.println((int)(Math.sqrt(2) * Math.sqrt(2)) == 2.0);
      int x = 32768; // 2^15
      long y = x * x;
      System.out.println( 32768 * 65536 - 1  );
   }
}
