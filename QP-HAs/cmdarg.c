#include <stdio.h>
#include <stdlib.h>

/* program to multiply two numbers */
int main(int argc, char *argv[]) {
  int num1 = 0;
  int num2 = 0;
  if (argc != 3) {
    printf("Usage: program <n1> <n2>\n");
    exit(0);
  }
  num1 = atoi(argv[1]);
  num2 = atoi(argv[2]);
  printf("%d * %d = %d\n", num1, num2, num1 * num2);
}
  
