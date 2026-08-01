#While Loop

# Write a PYTHON program to print the natural numbers up to n

n = int(input("Enter n: "))
i = 1
while i <= n:
    print(i)
    i = i + 1

# Write a PYTHON program to print even numbers up to n

n = int(input("Enter n: "))
i = 2
while i <= n:
    print(i)
    i = i + 2

# Write a PYTHON program to print odd numbers up to n

n = int(input("Enter n: "))
i = 1
while i <= n:
    print(i)
    i = i + 2

# Write a PYTHON program to print sum of natural numbers up to n

n = int(input("Enter n: "))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i = i + 1
print("Sum =", sum)

# Write a PYTHON program to print sum of odd numbers up to n

n = int(input("Enter n: "))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i = i + 2
print("Sum =", sum)

# Write a PYTHON program to print sum of even numbers up to n

n = int(input("Enter n: "))
i = 2
sum = 0
while i <= n:
    sum = sum + i
    i = i + 2
print("Sum =", sum)

# Write a PYTHON program to print natural numbers up to n in reverse order

n = int(input("Enter n: "))
while n >= 1:
    print(n)
    n = n - 1

# Write a PYTHON program to print Fibonacci series up to n

n = int(input("Enter n: "))
a = 0
b = 1
i = 1
while i <= n:
    print(a)
    c = a + b
    a = b
    b = c
    i = i + 1

# Write a PYTHON program to find a factorial of given number

n = int(input("Enter number: "))
fact = 1
while n > 0:
    fact = fact * n
    n = n - 1
print("Factorial =", fact)

# Write a PYTHON program to check the entered number is prime or not

n = int(input("Enter number: "))
i = 1
count = 0
while i <= n:
    if n % i == 0:
        count = count + 1
    i = i + 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")

# Write a PYTHON program to find the sum of digits of given number
n = int(input("Enter number: "))
sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
print("Sum =", sum)

# Write a PYTHON program to check the entered number is palindrome or not

n = int(input("Enter number: "))
temp = n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# Write a PYTHON program to reverse the given number
n = int(input("Enter number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reverse =", rev)

# Write a PYTHON program to print the multiplication table

n = int(input("Enter number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i = i + 1

# Write a PYTHON program to print the largest of n numbers

n = int(input("How many numbers: "))
i = 1
num = int(input("Enter number: "))
largest = num
while i < n:
    num = int(input("Enter number: "))
    if num > largest:
        largest = num
    i = i + 1
print("Largest =", largest)

# Write a PYTHON program to print the smallest of n numbers

n = int(input("How many numbers: "))
i = 1
num = int(input("Enter number: "))
smallest = num
while i < n:
    num = int(input("Enter number: "))
    if num < smallest:
        smallest = num
    i = i + 1
print("Smallest =", smallest)
































