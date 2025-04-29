n = int(input())

count1 = 1
count2 = 0
for i in range(n):
    count3 = count1
    count1 = count3 + count2
    count2 = count3
    print(count3, end=" ")
