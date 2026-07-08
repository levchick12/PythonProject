# while условие:
#     тело цикла

# break

# итерируемый - list, tupple, dict, set, str

# for элемент in последовательность:
#     тело цикла

# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
# d = "hello world"
# for i in d:
#     print(i)

# start - начало последовательности
# stop - конец последовательноти (не включительно)
# step -  интервал последовательности
# s = range(start, stop, step)

# s =  list(range(1,100,1))
# print(s)

# for i in range(100):
#     print(i)

# s = "hello world"
# for i in range(5):
#     print(s[i])

# for i in range(2,11,2):
#     print(i)

# for i in range(10,1,-2):
#     print(i)

# for i in range(1,3):
#     print("Значение внешнего цикла", i)
#     for j in range(1,3):
#         print(print("Значение внутреннего цикла", j))
#     print()

# for i in range(1,5):
#     for j in range(1,11):
#         print(i,'*',j,'=',i*j)
#     print()

# i = 0
# j = 0
# while i < 10:
#     i = i + 1
#     j = 0
#     while j < 10:
#         j = j + 1
#         print(i,'*',j,'=',i*j)
#     print()

# for i in range(1,5):
#     j = 0
#     while j < 10:
#         j = j + 1
#         print(i,'*',j,'=',i*j)
#     print()


# for i in range(5,0,-1):
#      print("*" * i)

# for i in range(5,0,-1):
#     s = ""
#     for j in range(i):
#         s += "*"
#     print(s)

# print("Hello","World", sep="", end="")
# print("123")

# n = 5
# for i in range(n):
#      print(" " * (n - i -1), "#" * (2 * i + 1), sep=" ")

# n = 5
# for i in range(n):
#     for j in range(n - i -1):
#         print(" ", end=" ")
#     for j in range(2 * i + 1):
#         print("#", end=" ")
#     print()