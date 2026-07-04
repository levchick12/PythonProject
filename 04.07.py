# ЗАДАЧА 1
# a = abs(int(input()))
# k = 0
# while a:
#     k += a % 10
#     a = a // 10
# print(k)

# a = input()
# count = 0
# summ = 0
# while count < len(a):
#     summ += int(a[count])
#     count += 1
#     print(summ)

# ЗАДАЧА_2
# n = int(input())
# count = 0
# while count < n:
#     count += 1
#     if n % count == 0:
#         print(count)

# ЗАДАЧА_3
# count = 0
# flag = False
# while count < 10:
#     square = count ** 2
#     if square > 50:
#         flag = True
#         break
#     print(square)
#     count += 1
# else: //работает если не сраюотает break
#     print("все квадраты меньше 50")

# ЗАДАЧА_4
# n = int(input())
# if n >= 1:
#     j = 1
#     flag = False
#     while n - 1 > j:
#         j+=1
#         if n % j == 0:
#             print("составное")
#             break
#     else:
#         print("простое")


# ЗАДАЧА_5
# n = input()
# if len(n) >= 5:
#     count = 0
#     string = ""
#     while count < 5:
#         string+= n[count]
#         count += 1
#     print(string)
# else:
#     print("строка слишком короткая")

# ЗАДАЧА_6
# n = int(input())
# evens, odds = 0, 0
# while n:
#     if n % 2 == 0:
#         evens += 1
#     else:
#         odds += 1
#     n = n // 10
# print(evens, odds)