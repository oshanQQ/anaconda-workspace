#include <stdio.h>
#include <stdlib.h>

int main() {
  for (int i = 1; i <= 100; i++) {
    printf("%d: %d\n", i, rand() % 101);
  }

  return 0;
}
