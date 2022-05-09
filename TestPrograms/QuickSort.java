import java.util.*;
import java.io.*;
public class QuickSort
{
    static int a[];
    static int n;
    static boolean flag=true;

    public static void quickSort(int a[], int low, int high)
    {
        int i=low, j=high, temp;
        int pivot=a[(low+high)/2];
    System.out.println("Start, low=" + low + ", high=" + high);
        if(flag) {
            while(i<=j) {
                while(a[i]<pivot) {
                    i++;
                }
                while(a[j]>pivot) {
                    j--;
                }
                if(i<=j) {
                    temp=a[i];
                    a[i]=a[j];
                    a[j]=temp;

                    i++;
                    j--;
                }
            }
      System.out.println("i=" + i + ", j=" + j);

            if(low<j) {
                quickSort(a,low,j);
            }
            if(i<high) {
                quickSort(a,i,high);
            }
            System.out.println("Done, low=" + low + ", high=" + high);
        } else {
            while(i<=j) {
        while(a[i]>pivot) {
          i++;
        }
        while(a[j]<pivot) {
          j--;
        }
                if(i<=j) {
          temp=a[i];
          a[i]=a[j];
          a[j]=temp;

          i++;
          j--;
        }
      }
      System.out.println("i=" + i + ", j=" + j);
      if(low<j) {
        quickSort(a,low,j);
      }
      if(i<high) {
        quickSort(a,i,high);
      }
    }
    }

    public static void main(String args[])throws IOException
    {
        int i;
        long st,et;
/*
        Random random = new Random();
        Scanner read = new Scanner(System.in);

        PrintWriter out = new PrintWriter(new File("random.txt"));

        System.out.println("Enter the number of elements (>5000)");
        n=read.nextInt();
        a=new int[n];
        for(i=0;i<n;i++)
        {
            a[i]=random.nextInt(n)+1;
            out.print(a[i]+"\t");
        }
        out.close();
*/
    int a[] = {4,5,2,3, 7,6,1,8};
    int n = a.length;
        st=System.nanoTime();
        quickSort(a,0,n-1);
        et=System.nanoTime()-st;
        PrintWriter outA = new PrintWriter(new File("ascending.txt"));
        for(i=0;i<n;i++)
            outA.print(a[i]+"\t");
        outA.close();
/*
        System.out.println("The time complexity for WORST CASE is = "+(et/1000000000.0)+" secs");

        st=System.nanoTime();
                quickSort(a,0,n-1);
                et=System.nanoTime()-st;
        System.out.println("The time complexity for BEST CASE is = "+(et/1000000000.0)+" secs");

        flag=false;

        st=System.nanoTime();
                quickSort(a,0,n-1);
                et=System.nanoTime()-st;
        PrintWriter outD = new PrintWriter(new File("descending.txt"));
        for(i=0;i<n;i++)
                        outD.print(a[i]+"\t");
                outD.close();
                System.out.println("The time complexity for AVERAGE CASE is = "+(et/1000000000.0)+" secs");
*/
 
}


