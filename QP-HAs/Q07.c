#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>


#define MAX_LINE_SIZE 250
int main(int argc, char *argv[]) {
  FILE *fd;
  char *filename = argv[1];
  char line[MAX_LINE_SIZE];
  char *datestr;
  struct tm tm;
  time_t epoch;

  if (argc != 2) {
    printf("Usage: Q07 <inpfile>");
    exit(1);
    }

  if ((fd = fopen(filename, "r")) == NULL) {
    printf("Error in opening file %s\n", filename);
    exit(1);
    }
  while (fgets(line, MAX_LINE_SIZE, fd) != NULL) {
    line[strnlen(line, MAX_LINE_SIZE) - 1] = '\0';
    if (strptime(line, "%Y-%m-%d", &tm) != NULL) {
      epoch = mktime(&tm);
      printf("%s equals %ld\n", line, epoch);
    } else {
      printf("Invalid date %s in input", line);
    }
  }
}
