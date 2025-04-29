import math

harmonic = 0
n = int(input())
for i in range(1, n + 1):
    harmonic += 1 / i
result = harmonic - math.log(n)
print(result)