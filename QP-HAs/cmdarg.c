#include <stdio.h>
#include <stdlib.h>

/* program to multiply two numbers */
int main(int argc, char *argv[]) {
  char *filename;
  int num2 = 0;
  char buf[1000];
  FILE *fh;
  if (argc != 3) {
    printf("Usage: program <filename> <n2>\n");
    exit(0);
  }
  filename = argv[1];
  num2 = atoi(argv[2]);
  fh = fopen(filename, "r");
  // printing the read contents
  while (fgets(buf, 1000, fh) != NULL) {
    printf("%s", buf);
  }
  printf("2nd argument is %d\n", num2);
}

