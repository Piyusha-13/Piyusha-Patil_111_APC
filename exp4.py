#1.Write a Python program to create a list of five fruits and display the list.

l1=["Apple","Orange","Cherry","Banana","Chiku"]
print(l1)

#2.	Create a list of five integers. Display:
#•	First element 
#•	Last element 
#•	Third element

l1=[10,20,30,40,50]
print("First Element=",l1[0])
print("First Element=",l1[4])
print("First Element=",l1[2])

#3.Create a list of colors. Replace the third color with another color and display the updated list.

colors = ["Red", "Blue", "Green", "Yellow"]
colors[2] = "Purple"
print("Updated list:", colors)

#4.	Create a list of numbers. Add:
#	One element at the end 
#	One element at the beginning 
#	One element at a specified position 
#   Display the updated list.
 
numbers = [10, 20, 30, 40]
numbers.append(50)
numbers.insert(0, 5)
numbers.insert(3, 25)
print("Updated list:", numbers)

#5.	Create a list of student names. Remove:
#•	First student 
#•	Last student 
#•	A specific student by name 
#Display the remaining list.

names=["Piyusha","Arya","Atharv","Aditya"]
names.pop(0)
names.pop()
names.remove("Arya")
print(names)

#6.	Write a program to find the largest and smallest number in a list without using max() or min().
numbers = [45, 12, 89, 23, 67, 5]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)

#7.	Accept 10 numbers from the user and store them in a list. Calculate:
#•	Sum 
#•	Average 

numbers = []
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)
total = 0
for i in numbers:
    total = total + i
average = total / 10
print("Sum =", total)
print("Average =", average)

#8.	Store 15 integers in a list. Count how many numbers are:
#•	Even 
#•	Odd
numbers = [2, 5, 8, 7, 10, 11]
even = 0
odd = 0
for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even =", even)
print("Odd =", odd)

#9.	Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.
l1=["Kolhapur","Satara","Sangli","Pune"]
user=input("Enter city=")
if user in l1:
    print("Exist")


#10.Write a program to reverse a list without using the reverse() method.
l1=[10,20,30,40,50]
print(l1[::-1])

#11.Create a list of 10 numbers and display:
#•	First 5 elements 
#•	Last 5 elements 
#•	Middle 4 elements 
#•	Alternate elements 
#•	Reverse list using slicing

l1=[10,20,30,40,50,60,70,80,90,100]
print(l1[0:5])
print(l1[5:])
print(l1[3:7])
print(l1[::2])
print(l1[::-1])

#12.	Display all elements present at even index positions.
n = [10,20,30,40,50,60]
print(n[::2])

# 13. Accept 10 numbers and sort them in:
# Ascending order
# Descending order

numbers = []
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)
numbers.sort()
print("Ascending:", numbers)
numbers.sort(reverse=True)
print("Descending:", numbers)

# 14. Create a list containing duplicate values
# and display only unique elements.

numbers = [10,20,10,30,20,40]
unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)

print(unique)


# 15. Find the second largest element in a list.

n1 = [10,50,30,80,60]
n1.sort()
print("Second Largest =", n1[-2])

# 16. Create a nested list storing:
# Student Name
# Roll Number
# Marks
# Display all student details.

students = [["Amit",101,85],["Riya",102,90],["Rahul",103,80]]
for s in students:
    print("Name:", s[0])
    print("Roll:", s[1])
    print("Marks:", s[2])
    print()

# 17. Create two 3 × 3 matrices
# using nested lists and perform matrix addition.

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,1,1],[1,1,1],[1,1,1]]

print(a[0][0] + b[0][0], a[0][1] + b[0][1], a[0][2] + b[0][2])
print(a[1][0] + b[1][0], a[1][1] + b[1][1], a[1][2] + b[1][2])
print(a[2][0] + b[2][0], a[2][1] + b[2][1], a[2][2] + b[2][2])

# 18. Create a shopping cart using a list.
# Perform:
# Add item
# Remove item
# Search item
# Display cart
# Count total items

list = ["Milk", "Bread", "Eggs"]
list.append("Butter")
list.remove("Bread")
name = input("Enter item name: ")
if name in list:
    print("Item Found")
else:
    print("Item Not Found")
print("Cart:", list)
print("Total Items:", len(list))

#19.	Store names of students present in class.
#Display:
#•	Total students 
#•	Search a student's attendance 
#•	Add a new student 
#•	Remove an absent student 
names = ["Amit", "Riya", "Rahul"]
print("Total Students:", len(names))
s = input("Enter student name: ")
if s in names:
    print("Present")
else:
    print("Absent")
names.append("Sneha")
names.remove("Rahul")
print("Students:", names)

#20.	Create a list of books.
#Implement:
#•	Add a new book 
#•	Search a book 
#•	Remove a book 
#•	Display all books 
#•	Count total books

b=["b1","b2","b3","b4"]
b.append("b5")
book = input("Enter book name: ")
if book in b:
    print("Book Found")
else:
    print("Book Not Found")
b.remove("b2")
print("Books:", b)
print("Total Books:", len(b))

#21.	Accept two lists and merge them into a single list.
l1=[10,20]
l2=[30,40]
print(l1+l2)

#23.	Count the frequency of each element in a list.

list1 = [1, 2, 2, 3, 1, 2]

print("1 =", list1.count(1))
print("2 =", list1.count(2))
print("3 =", list1.count(3))
#24.	Rotate a list:
#•	Left by one position 
#•	Right by one position

a = [10,20,30,40,50]
print("Left Rotate:", a[1:] + a[:1])
print("Right Rotate:", a[-1:] + a[:-1])


# 25. Remove all duplicate elements while preserving the original order.
a = [10,20,10,30,20,40,50,40]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)


# 26. Store marks of 20 students and determine:
# • Highest marks
# • Lowest marks
# • Average marks
# • Students above average
# • Students below average
# 27. Store salaries and find:
# Highest, Lowest, Average
# Above 50000 and Below 30000

a = [25000,40000,55000,70000,28000]

print("Highest:", max(a))
print("Lowest:", min(a))
print("Average:", sum(a)/len(a))
high = 0
low = 0
for i in a:
    if i > 50000:
        high += 1
    if i < 30000:
        low += 1
print("Above 50000:", high)
print("Below 30000:", low)


# 27. Store salaries of employees and determine:
# • Highest salary
# • Lowest salary
# • Average salary
# • Employees earning above ₹50000
# • Employees earning below ₹30000

a = []
for i in range(5):
    n = int(input("Enter salary: "))
    a.append(n)
avg = sum(a) / len(a)
print("Highest:", max(a))
print("Lowest:", min(a))
print("Average:", avg)

high = 0
low = 0

for i in a:
    if i > 50000:
        high += 1
    if i < 30000:
        low += 1

print("Above 50000:", high)
print("Below 30000:", low)


# 28. Store scores of a batsman in 10 matches and calculate:
# • Highest score
# • Lowest score
# • Total runs
# • Average runs
# • Number of centuries
# • Number of half-centuries

a = [45,60,120,90,150,35,75,20,55,100]

print("Highest:", max(a))
print("Lowest:", min(a))
print("Total:", sum(a))
print("Average:", sum(a)/10)
c = 0
h = 0
for i in a:
    if i >= 100:
        c = c + 1
    elif i >= 50:
        h = h + 1
print("Centuries:", c)
print("Half-centuries:", h)


# 29. Store temperature of 30 days and determine:
# • Hottest day
# • Coldest day
# • Average temperature
# • Days above average
# • Days below average

a = [30,32,35,29,31]
print("Hottest:", max(a))
print("Coldest:", min(a))
avg = sum(a)/5
print("Average:", avg)
c1 = 0
c2 = 0
for i in a:
    if i > avg:
        c1 = c1 + 1
    if i < avg:
        c2 = c2 + 1
print("Above Average:", c1)
print("Below Average:", c2)

# 30. Store patient names and ages using lists.
# Perform:
# • Add a patient
# • Delete a patient
# • Search a patient
# • Display all patients
# • Count total patients

name = ["Amit", "Riya", "Rahul"]
age = [25, 30, 22]
name.append("Sneha")
age.append(28)
name.remove("Rahul")
age.pop(2)
x = input("Enter patient name: ")
if x in name:
    print("Patient Found")
else:
    print("Patient Not Found")
for i in range(len(name)):
    print(name[i], age[i])
print("Total Patients:", len(name))

