counter = 0
for _ in range(10):
    n = int(input())
    if n % 2 == 0:
        counter += 1
if counter == 10:
    print("YES")
else:
    print("NO")