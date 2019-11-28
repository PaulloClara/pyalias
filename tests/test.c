#include "stdio.h"
#include "stdlib.h"

int main(int argc, char *argv[]) {
  if (argv[1] == NULL) printf("\n\tHello World\n\n");
  else printf("\n\t%s\n\n", argv[1]);

  return 0;
}
