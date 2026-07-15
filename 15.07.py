# n = int(input())
# c = n//2
# k = n//2
# for i in range(n):
#     for j in range(n):
#         if abs(i - c) + abs(j - c) < k:
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print()

# n = 9
# for i in range(1,n + 1):
#     for j in range(1,n + 1):
#         if (i + j) % 2 != 0:
#             print("..", end = "")
#         else:
#             print(i * j, end = "")
#     print()

# counter = 0
# for h in range(24):
#     for m in range(60):
#         for s in range(60):
#             time = str(h) + str(m) + str(s)
#             if (len(set(time))) == 6:
#                 counter += 1
# print(counter)

# counter = 0
# for i in range(100000, 1000000):
#     s = str(i)
#     if int(s[0]) + int(s[1]) + int(s[2]) == int(s[3]) + int(s[4]) + int(s[5]) :
#         counter += 1
# print(counter)

# import math
# alphabet = 27 + 10
# nums = 3548
# memory_size = 12 * 2 ** 10
# for dlina_serin_num in range(1, 10000000):
#     bits = math.ceil(math.log2(alphabet))
#     bytes = math.ceil(dlina_serin_num * bits / 8)
#     if bytes * nums >= memory_size:
#         print(dlina_serin_num)
#         break

# import math
# alphabet = 17 + 10
# nums = 7564230
# memory_size = 31 * 2 ** 20
# for dlina_serin_num in range(1, 10000000):
#     bits = math.ceil(math.log2(alphabet))
#     bytes = math.ceil(dlina_serin_num * bits / 8)
#     if bytes * nums >= memory_size:
#          print(dlina_serin_num)
#          break

# import math
# alphabet = 52 + 10 + 1988
# nums = 1550
# memory_size = 356 * 2 ** 10
# for dlina_serin_num in range(1, 10000000):
#     bits = math.ceil(math.log2(alphabet))
#     bytes = math.ceil(dlina_serin_num * bits / 8)
#     if bytes * nums <= memory_size:
#          print(dlina_serin_num)