#include "stdio.h"
#include "stdlib.h"

int main(int argc, char *argv[]) {
  if (argc == 1) printf("\n\tHello World\n\n");
  else
    for (size_t i = 1; i < argc; i++)
      printf("\t%s\n", argv[i]);

  return 0;
}
