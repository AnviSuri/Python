# print("Q. 1")
# print("Hello, World!")
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 2")
# # Valid identifiers
# name = "Alice"
# _age = 20
# # Invalid identifiers (will cause error)
# # 1name = "Bob"
# # my-name = "Charlie"
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 3")
# import keyword
# print(keyword.kwlist)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 4")
# if True:
#     print("Proper indentation")
# # Improper indentation would cause IndentationError
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 5")
# # Single-line comment
# print("Hello") # Inline comment
# """
# Multi-line
# comment
# """
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 6")
# name = input("Enter your name: ")
# print("Hello,", name)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 7")
# a = 10 # int
# b = 3.14 # float
# c = "Hello" # str
# d = True # bool
# print(type(a), type(b), type(c), type(d))
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 8")
# x = 0b1010 # binary literal
# print(x)
# print(bin(10))
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 9")
# print(len("Hello"))
# print(abs(-5))
# print(max(3, 7, 2))
# print(min([4, 2, 9]))
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 10")
# a, b = 5, 10
# print(a, b)
# # Method 1: using temp
# temp = a
# a = b
# b = temp
# print(a, b)
# # Method 2: tuple unpacking
# a, b = b, a
# print(a, b)
# # Method 3: arithmetic ops
# a = a + b
# b = a - b
# a = a - b
# print(a, b)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 11")
# a, b, c = 1, 2, 3
# # Using tuple unpacking
# a, b, c = c, a, b
# print(a, b, c)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 12")
# name = input("Enter name: ")
# cls = input("Enter class: ")
# roll = int(input("Enter roll: "))
# age = int(input("Enter age: "))
# print(f"Name: {name}, Class: {cls}, Roll: {roll}, Age: {age}")
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 13")
# from datetime import date
# birth_year = int(input("Enter birth year: "))
# current_date = date.today()
# age = current_date.year - birth_year
# print("Age is:", age)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 14")
# year = int(input("Enter year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not Leap Year")
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 15")
# n = int(input("Enter number: "))
# sum_div = sum(i for i in range(1, n) if n % i == 0)
# print("Perfect" if sum_div == n else "Not Perfect")
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 16")
# n = int(input("Enter number: "))
# num = n
# power = len(str(n))
# sum_digits = sum(int(d)**power for d in str(n))
# print("Armstrong" if sum_digits == num else "Not Armstrong")
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 17")
# n = int(input("Enter number: "))
# if n > 1:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not Prime")
#             break
#     else:  # this else belongs to the for loop
#         print("Prime")
# else:
#     print("Not Prime")
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 18")
# # Prime
# for num in range(1, 101):
#     if num > 1 and all(num % i != 0 for i in range(2, num)):
#         print("Prime:", num)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# # Perfect
# for n in range(1, 101):
#     if sum(i for i in range(1, n) if n % i == 0) == n:
#         print("Perfect:", n)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# # Armstrong
# for n in range(1, 1000):
#     power = len(str(n))
#     if sum(int(d) ** power for d in str(n)) == n:
#         print("Armstrong:", n)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

print("Q. 19")
count = 0
for year in range(1, 2026):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)
        count += 1
print("Total Leap Years:", count)
print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 20")
# count = 0
# for n in range(1, 2026):
#     if sum(i for i in range(1, n) if n % i == 0) == n:
#         print(n)
#         count += 1
# print("Total Perfect Numbers:", count)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 21")
# for i in range(5):
#     print(i)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 22")
# for i in range(3):
#     for j in range(2):
#         print(i, j)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 23")
# squares = [x ** 2 for x in range(6)]
# print(squares)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 24")
# lst = ["a", "b", "c"]
# for idx, val in enumerate(lst):
#     print(idx, val)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 25")
# # Pattern 1: Increasing Triangle
# for i in range(1, 6):
#     print("*" * i)
# print()

# # Pattern 2: Decreasing Triangle
# for i in range(5, 0, -1):
#     print("*" * i)
# print()

# # Pattern 3: Right-aligned Triangle
# for i in range(1, 6):
#     print(" " * (5 - i) + "*" * i)
# print()

# # Pattern 4: Left-aligned Inverted Triangle
# for i in range(5, 0, -1):
#     print(" " * (5 - i) + "*" * i)
# print()

# # Pattern 5: Pyramid
# for i in range(1, 6):
#     print(" " * (5 - i) + "*" * (2 * i - 1))
# print()

# # Pattern 6: Inverted Pyramid
# for i in range(5, 0, -1):
#     print(" " * (5 - i) + "*" * (2 * i - 1))
# print()

# # Pattern 7: Diamond
# for i in range(1, 6):
#     print(" " * (5 - i) + "*" * (2 * i - 1))
# for i in range(4, 0, -1):
#     print(" " * (5 - i) + "*" * (2 * i - 1))
# print()

# # Pattern 8: Square
# for i in range(5):
#     print("* " * 5)
# print()

# # Pattern 9: Hollow Square
# for i in range(5):
#     for j in range(5):
#         if i == 0 or i == 4 or j == 0 or j == 4:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# print()

# # Pattern 10: Right Diagonal
# for i in range(5):
#     for j in range(5):
#         if i == j:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# print()

# # Pattern 11: Left Diagonal
# for i in range(5):
#     for j in range(5):
#         if i + j == 4:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# print()

# # Pattern 12: X Pattern
# for i in range(5):
#     for j in range(5):
#         if i == j or i + j == 4:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 26")
# a, b, c = input("Enter values: ").split()
# print(a, b, c)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 27")
# lst = list(map(int, input("Enter numbers: ").split()))
# print(lst)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 28")
# a, b, c = input("Enter values separated by comma: ").split(",")
# print(a, b, c)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 29")
# n = int(input("Enter number: "))
# print("Last digit:", n % 10)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 30")
# income = int(input("Enter income: "))
# tax = 0
# if income <= 250000:
#     tax = 0
# elif income <= 500000:
#     tax = (income - 250000) * 0.05
# elif income <= 1000000:
#     tax = 12500 + (income - 500000) * 0.10
# elif income <= 2000000:
#     tax = 62500 + (income - 1000000) * 0.20
# elif income <= 3000000:
#     tax = 262500 + (income - 2000000) * 0.30
# else:
#     tax = 562500 + (income - 3000000) * 0.40
# print("Tax:", tax)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 31")
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 32")
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 33")
# s = "hello"
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 34")
# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 35")
# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 36")
# i = 0
# while i < 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 37")
# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Division by zero!")
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 38")
# try:
#     x = 10 / 2
# except ZeroDivisionError:
#     print("Division by zero!")
# else:
#     print("Success:", x)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 39")
# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Error")
# finally:
#     print("Finally executed")
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 40")
# try:
#     x = 10 / 2
# except ZeroDivisionError:
#     print("Error")
# else:
#     print("Success:", x)
# finally:
#     print("Finally executed")
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 41")
# try:
#     with open("file.txt") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File not found")
# finally:
#     print("Done")
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 42")
# lst = [1, 2, 3]
# lst.append(4)
# print(lst)
# lst[0] = 10
# print(lst)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 43")
# lst = [0, 1, 2, 3, 4, 5]
# print(lst[1:4])
# print(lst[:3])
# print(lst[::2])
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 44")
# nums = [x for x in range(10) if x % 2 == 0]
# print(nums)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 45")
# t = (1, 2, 3)
# print(t[0])
# print(t[-1])
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 46")
# t = (1, (2, 3), (4, (5, 6)))
# print(t[1][1])
# print(t[2][1][0])
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 47")
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b)  # union
# print(a & b)  # intersection
# print(a - b)  # difference
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 48")
# d = {"a": 1, "b": 2}
# d["c"] = 3
# print(d)
# d["a"] = 10
# print(d)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 49")
# d = {"a": 1, "b": 2}
# print(d["a"])
# d.pop("b")
# print(d)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 50")
# d = {"a": 1, "b": 2}
# for k, v in d.items():
#     print(k, v)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 51")
# lst = [1, 2, 3]
# it = iter(lst)
# print(next(it))
# print(next(it))
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

# print("Q. 52")
# lst = [1, 2, 3]
# for val in iter(lst):
#     print(val)
# print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

print("Q. 53")

class Count:
    def __init__(self, limit):
        self.limit = limit
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.limit:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

for x in Count(5):
    print(x)
print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

print("Q. 54")
def my_gen():
    yield 1
    yield 2
    yield 3

for x in my_gen():
    print(x)
print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

print("Q. 55")
def squares(n):
    for i in range(1, n+1):
        yield i*i

for val in squares(5):
    print(val)
print("This code is written and executed by Anvi Suri 0231BCA037\n\n")

print("Q. 56")
def gen1():
    yield from [1, 2, 3]

def gen2():
    yield from [4, 5]

def chain():
    yield from gen1()
    yield from gen2()

for x in chain():
    print(x)
print("This code is written and executed by Anvi Suri 0231BCA037\n\n")