#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int add(int x, int y){
  return x + y;
}


// Outputs x-th fibonacci number
int dothething(int x){
  if (x==0){
    return 0;
  }
  else if (x==1){
    return 1;
  }
  else {
    return add(dothething(x-1), dothething(x-2));
  }
}
