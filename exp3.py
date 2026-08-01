#For Loop
# 1] Write a PYTHON program to print the natural numbers up to n

n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(i) 

# 2] Write a PYTHON program to print even numbers up to n

n = int(input("Enter n: "))
for i in range(2, n + 1, 2):
    print(i)

#3] Write a PYTHON program to print odd numbers up to n

n = int(input("Enter n: "))
for i in range(1, n + 1, 2):
    print(i)

# 4] Write a PYTHON program that prints 1 2 4 8 16 32 ... up to n

n = int(input("Enter n: "))
i = 1
while i <= n:
    print(i)
    i = i * 2

#5] Write a PYTHON program to sum the given sequence 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!

n = int(input("Enter n: "))
fact = 1
sum = 1
for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (1 / fact)

print("Sum =", sum)

#6] Write a PYTHON program to compute the cosine series cos(x) = 1 – x2/2! + x4/4! – x6/6! + ... + xn/n!

x = float(input("Enter x: "))
n = int(input("Enter n: "))
sum = 1
fact = 1
sign = -1
for i in range(2, n + 1, 2):
    fact = 1
    for j in range(1, i + 1):
        fact = fact * j
    sum = sum + sign * (x ** i) / fact
    sign = sign * -1

print("Cosine series =", sum)

# 7] Write a short PYTHON program to check whether the square root of a number is prime or not

import math
n = int(input("Enter number: "))
r = int(math.sqrt(n))
c = 0
for i in range(1, r + 1):
    if r % i == 0:
        c = c + 1
if c == 2:
    print("Prime")
else:
    print("Not Prime")

# 8] Write a PYTHON program to produce the following design
# A B C
# A B C
# A B C

for i in range(3):
    print("A B C")

#9] Write a PYTHON program to produce following design
#     A
#     A B
#     A B C
#     A B C D 
#     A B C D E
#     If user enters n value as 5

n = int(input("Enter n: "))
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

# 10] Write a PYTHON program to produce following design
#A B C D E
#A B C D
#A B C
#A B
#A
#(If user enters n value as 5)

n = int(input("Enter n: "))
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

#11] Write a PYTHON program to produce following design
      #1
      #1 2
      #1 2 3
      #1 2 3 4
      #1 2 3 4 5
      #If user enters n value as 5
n = int(input("Enter n: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#12] Write a PYTHON program to produce following design
      #1
      #2 2
      #3 3 3
      #4 4 4 4 
      #5 5 5 5 5
      #If user enters n value as 5

n = int(input("Enter n: "))
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()


