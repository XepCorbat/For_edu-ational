import math

counter = 0
n = int(input())
for i in range(1, n + 1):
    if (i ** 2) % 10 in {2, 5, 8}:  # Последняя цифра квадрата i
        counter += i
print(counter)