#include <stdio.h>
#include <stdlib.h>

int main() {
int sum = 0;

  for (int i = 1; i <= 100; i++) {
    int random_number = rand() % 101;
    printf("%d: %d\n", i, random_number);
    sum += random_number;
  }

  printf("average: %.3f\n", sum / 100.000);

  return 0;
}
