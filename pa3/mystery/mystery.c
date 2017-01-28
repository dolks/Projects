#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "mystery.h"

// Calculates the x-th fibonacci
int main(int argc, char**argv){
  char * num = malloc(sizeof(argv[1])* strlen(argv[1]));
  strcpy(num, argv[1]);

  int fibonacciNum = atoi(num);
  if (fibonacciNum>=45){
    printf("Input too large to fit into 32-bit integer.\n");
    return 0;
  }
  if (fibonacciNum<0){
    printf("Number must be non-negative.\n");
    return 0;
  }
  fibonacciNum = dothething(fibonacciNum);

  printf("%d\n", fibonacciNum);
  free(num);
  return 0;

}
