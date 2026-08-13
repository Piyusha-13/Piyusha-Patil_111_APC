#.1Write a Python program to create a tuple of five integers and display it.
t1=(10,20,30,40,50)
print(t1)

#2.	Create a tuple containing five city names. Display:
#•	First city 
#•	Last city 
#•	Third city
t1=("Kolhapur","Sangli","Satara")
print(t1[0])
print(t1[1])
print(t1[2])

#.3Create a tuple of student names and display the total number of students using the len() function.
t1=("Piyusha","Arya","Atharv","Prajal")
print(len(t1))

#4.	Create a tuple of colors. Check whether a given color exists in the tuple

c = ("Red", "Blue", "Green", "Yellow", "Black")
n = input("Enter a color: ")
if n in c:
    print(n, "exists in the tuple.")
else:
    print(n, "does not exist in the tuple.")

#5.	Create a tuple of fruits and display each fruit using a loop.
f=("Mango","Orange","Chikku")
for i in f:
    print(i)

#6.	Create a tuple with repeated numbers and count how many times a particular number appears.
n = (2,2,1,3,4,5,6,6,8,8,8,8,9)
num = int(input("Enter a number: "))
count = n.count(num)
print(num, "appears", count, "times.")


#7.	Create a tuple of employee IDs and find the index of a given ID.
t1= (101, 102, 103, 104, 105)
emp_id = int(input("Enter employee ID: "))
if emp_id in t1:
    print("Index of", emp_id, "is", t1.index(emp_id))
else:
    print("Employee ID not found.")

#8.	Create two tuples of numbers and concatenate them into a single tuple.
t1=(1,2,3,4,5)
t2=(6,7,8,9)
print(t1+t2)

#9.	Create a tuple containing three elements and repeat it four times.
t1=(10,20,30)
r=t1*3
print(r)

#10.	Create a tuple of 10 numbers and display:
#•	First five elements 
#•	Last five elements 
#•	Middle four elements 
#•	Alternate elements 
#•	Reverse tuple

t1=(10,20,30,40,50,60,70,80,90,11)
print(t1[0:5])
print(t1[5:11])
print(t1[3:7])
print(t1[::2])
print(t1[::-1])

# 11. Convert a tuple into a list and add a new element.

a = (10, 20, 30, 40)
b = list(a)
b.append(50)
print("Tuple:", a)
print("List after adding new element:", b)

# 12. Accept five numbers from the user, store them in a list, and convert the list into a tuple.
a = []
for i in range(5):
    n = int(input("Enter a number: "))
    a.append(n)
b = tuple(a)
print("List:", a)
print("Tuple:", b)

# 13. Modify a tuple by converting it into a list and then back into a tuple.
a = (10, 20, 30, 40)
b = list(a)
b[1] = 50
a = tuple(b)
print("Modified tuple:", a)

# 14. Create a tuple and delete it completely.
a = (10, 20, 30, 40)
print("Tuple:", a)
del a
print("Tuple deleted successfully.")

# 15. Create a nested tuple containing student details and display each record.
students = (
    (1, "Rahul", 18),
    (2, "Amit", 19),
    (3, "Priya", 18)
)
for student in students:
    print(student)

#16.	Store ten numbers in a tuple and calculate their sum.
t1=(1,2,3,4,5,6,7,8,9,10)
print(sum(t1))

# 17. Find the largest and smallest number in a tuple without using max() and min().

a = (10, 25, 5, 40, 15)
large = a[0]
small = a[0]
for n in a:
    if n > large:
        large = n

    if n < small:
        small = n
print("Largest number:", large)
print("Smallest number:", small)

#18. Calculate the average of elements stored in a tuple.

a = (10, 20, 30, 40, 50)
total = 0
for n in a:
    total = total + n
average = total / len(a)
print("Average:", average)

# 19. Store 15 integers in a tuple and count:
# Even numbers
# Odd numbers

a = (10, 15, 22, 31, 40, 55, 62, 71, 80, 95, 12, 27, 34, 49, 50)
even = 0
odd = 0
for n in a:
    if n % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Even numbers:", even)
print("Odd numbers:", odd)

# 20. Accept a number from the user and determine whether it exists in the tuple.
a = (10, 20, 30, 40, 50)
n = int(input("Enter a number: "))
if n in a:
    print("Number exists in the tuple.")
else:
    print("Number does not exist in the tuple.")

#21.	Store student details in a tuple:
#•	Roll Number 
#•	Name 
#•	Department 
#•	Marks 
#Display all the details.

student = (101, "Rahul", "Computer", 85)
print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])

# 22. Create tuples containing:
# Employee ID
# Name
# Salary
# Display all employee information.
employee_id = (101, 102, 103)
name = ("Piyusha", "Arya", "Priya")
salary = (25000, 30000, 28000)

for i in range(3):
    print("Employee ID:", employee_id[i])
    print("Name:", name[i])
    print("Salary:", salary[i])
    print()


# 23. Store item prices in a tuple and calculate:
# Total bill
# Average price
# Highest-priced item
# Lowest-priced item
price = (100, 250, 150, 300, 200)
total = 0
for n in price:
    total = total + n
average = total / len(price)
high = price[0]
low = price[0]
for n in price:
    if n > high:
        high = n

    if n < low:
        low = n

print("Total bill:", total)
print("Average price:", average)
print("Highest-priced item:", high)
print("Lowest-priced item:", low)


# 24. Store temperatures of seven days in a tuple and determine:
# Maximum temperature
# Minimum temperature
# Average temperature
temp = (32, 35, 30, 33, 36, 31, 34)
total = 0
high = temp[0]
low = temp[0]
for n in temp:
    total = total + n

    if n > high:
        high = n

    if n < low:
        low = n

average = total / len(temp)
print("Maximum temperature:", high)
print("Minimum temperature:", low)
print("Average temperature:", average)


# 25. Store runs scored in 10 matches and calculate:
# Total runs
# Highest score
# Lowest score
# Average score
runs = (45, 60, 32, 75, 50, 80, 25, 55, 70, 40)
total = 0
high = runs[0]
low = runs[0]
for n in runs:
    total = total + n

    if n > high:
        high = n

    if n < low:
        low = n
average = total / len(runs)
print("Total runs:", total)
print("Highest score:", high)
print("Lowest score:", low)
print("Average score:", average)

# 26. Create two tuples and find the common elements between them.
a = (10, 20, 30, 40, 50)
b = (30, 40, 50, 60, 70)
common = ()
for n in a:
    if n in b:
        common = common + (n,)
print("Common elements:", common)


# 27. Merge two tuples and remove duplicate elements.
a = (10, 20, 30, 40)
b = (30, 40, 50, 60)
c = a + b
result = ()
for n in c:
    if n not in result:
        result = result + (n,)
print("Merged tuple without duplicates:", result)


# 28. Count the frequency of each element in a tuple.
a = (10, 20, 10, 30, 20, 10, 40, 30)
done = ()
for n in a:
    if n not in done:
        count = 0

        for x in a:
            if x == n:
                count = count + 1
        print(n, "appears", count, "times")
        done = done + (n,)


# 29. Convert a tuple into a sorted tuple in ascending and descending order.

a = (40, 10, 30, 20, 50)
b = sorted(a)
c = sorted(a, reverse=True)
b = tuple(b)
c = tuple(c)
print("Ascending order:", b)
print("Descending order:", c)



# 30. Create a tuple containing patient records:
# Patient ID
# Name
# Age
# Blood Group
# Perform the following operations:
# Display all records
# Search for a patient by ID
# Count the total number of patients
# Display patients with a specific blood group

patients = (
    (101, "Rahul", 20, "A+"),
    (102, "Amit", 25, "B+"),
    (103, "Priya", 22, "O+"),
    (104, "Neha", 24, "A+")
)
print("All Patient Records:")
for p in patients:
    print("ID:", p[0])
    print("Name:", p[1])
    print("Age:", p[2])
    print("Blood Group:", p[3])
    print()
n = int(input("Enter Patient ID: "))
for p in patients:
    if p[0] == n:
        print("Patient Found")
        print("ID:", p[0])
        print("Name:", p[1])
        print("Age:", p[2])
        print("Blood Group:", p[3])
print("Total Patients:", len(patients))
g = input("Enter Blood Group: ")
print("Patients with", g, "blood group:")
for p in patients:
    if p[3] == g:
        print(p)




