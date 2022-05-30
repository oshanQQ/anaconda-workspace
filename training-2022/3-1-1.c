#include <stdio.h>

int main() {
  int numbers[100];
  for (int i = 1; i <= 100; i++) {
    numbers[i - 1] = i;
  }
  for (int i = 0; i < 100; i++) {
    printf("Numbers[%d]: %d\n", i, numbers[i]);
  }
}