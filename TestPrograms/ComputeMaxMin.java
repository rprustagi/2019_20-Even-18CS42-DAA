public class  ComputeMaxMin {
   public static void main(String[] args) {
      int x,y;
      x = Integer.parseInt(args[0]);
      y = Integer.parseInt(args[1]);
      System.out.println((x + y + Math.abs(x - y))/2);
      System.out.println((x + y - Math.abs(x - y))/2);
   }
}
