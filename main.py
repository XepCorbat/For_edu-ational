n = int(input())
y = 0
z = 0
for _ in range(n):
    x = int(input())
    if x > y:
        z = y
        y = x
    elif x > z:
        z = x
print(y)
print(z)
