from math import *


# 7.4 - 3
# text = input()
# counter = 0
# while text != "стоп" and text != "хватит" and text != "достаточно":
#     text = input()
#     counter += 1
# print(counter)

# 7.4 - 2
# text = input()
# while text != "КОНЕЦ" and text != "конец":
#     print(text)
#     text = input()
#
# 7.3 - 11
# n = int(input())
#
# count1 = 1
# count2 = 0
# for i in range(n):
#     count3 = count1
#     count1 = count3 + count2
#     count2 = count3
#     print(count3, end=" ")
#
# 7.3 - 10
# counter = 0
# for _ in range(10):
#     n = int(input())
#     if n % 2 == 0:
#         counter += 1
# if counter == 10:
#     print("YES")
# else:
#     print("NO")
#
# 7.3 - 9
# y = 0
# z = 0
# for _ in range(n):
#     x = int(input())
#     if x > y:
#         z = y
#         y = x
#     elif x > z:
#         z = x
# print(y)
# print(z)
#
# 7.3 - 8
# for i in range(1, n + 1):
#     summ += ((-1) ** (i + 1)) * i
# print(summ)
#
# 7.3 - 7
# n = int(input())
# summ = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         summ += i
# print(summ)
#
# 7.3 - 6
# total = 1
# for i in range(10):
#     n = int(input())
#     if n != 0:
#         total *= n
# print(total)
#
# 7.3 - 5
# n = int(input())
# print(factorial(n))
#
# # 7.3 - 4
# counter = 0
# n = int(input())
# for i in range(1, n + 1):
#     if (i ** 2) % 10 in {2, 5, 8}:  # Последняя цифра квадрата i
#         counter += i
# print(counter)
#
# # 7.3 - 3
# harmonic = 0
# n = int(input())
# for i in range(1, n + 1):
#     harmonic += 1 / i
# result = harmonic - log(n)
# print(result)
#
# # 7.3 - 2
# total = 0
# n = int(input())
# for _ in range(n):
#     num = int(input())
#     total += num
# print(total)
#
# # 7.3 - 1
# a, b = int(input()), int(input())
# counter = 0
# if a <= b:
#     for i in range(a, b + 1):
#         if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
#             counter += 1
# print(counter)
