#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>


#define MAX_LINE_SIZE 250
int main(int argc, char *argv[]) {
  int cnt = 0;
  int sum = 0;

  for (cnt =0; cnt < argc; cnt++) {
    sum = sum + atoi(argv[cnt]);
  }
  printf("sum = %d\n", sum);
}
