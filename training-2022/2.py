import random

sum = 0

for i in range(1, 101):
  random_number = random.randint(1, 100)
  print(random_number)
  sum += random_number

average = sum / 100
print(round(average, 3))
