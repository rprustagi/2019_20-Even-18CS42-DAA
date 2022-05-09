public class BadIncrement {
   public static void main(String[] args) {
      int num = 100;
      num = num++;
      System.out.println(num);
      num = ++num;
      System.out.println(num);
      num = num++ + num++;
      System.out.println(num);
      num = num++ + ++num;
      System.out.println(num);
   }
}
