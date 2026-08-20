# 1. Create a dictionary containing student details and display all key-value pairs
student = {
    "roll_no": 101,
    "name": "Atharv",
    "department": "CSE",
    "marks": 85
}
print(student.items())


#2. Create employee information and display value of specified key
employee = {
    "id": 1001,
    "name": "Rahul",
    "department": "IT",
    "salary": 60000
}
key = "name"
print(employee[key])


#3. Create dictionary of five products and prices, then add a new product
products = {
    "Pen": 10,
    "Book": 50,
    "Bag": 500,
    "Bottle": 200,
    "Pencil": 5
}
products["Notebook"] = 80
print(products)


# 4. Create student marks dictionary and update specified student's marks
marks = {
    "Atharv": 85,
    "Rahul": 78,
    "Amit": 90
}
marks["Rahul"] = 88
print(marks)


# 5. Create cities and populations, then remove a specified city
cities = {
    "Mumbai": 20000000,
    "Pune": 7000000,
    "Delhi": 30000000,
    "Kolhapur": 500000
}
del cities["Pune"]
print(cities)


# 6. Create employee IDs and names, then check whether an ID exists
employees = {
    101: "Atharv",
    102: "Rahul",
    103: "Amit"
}
emp_id = int(input("Enter employee ID: "))
if emp_id in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")


# 7. Create student records and find total number of key-value pairs
students = {
    "Atharv": 85,
    "Rahul": 78,
    "Amit": 90,
    "Rohit": 75
}
print("Total pairs:", len(students))


# 8. Display all keys, values and key-value pairs
data = {
    "name": "Atharv",
    "age": 20,
    "department": "CSE"
}
print("Keys:", data.keys())
print("Values:", data.values())
print("Key-Value pairs:", data.items())


#9.Create a dictionary of programming languages and their creators. Display each key and value using a loop.
languages = {
    "Python": "Guido van Rossum",
    "C": "Dennis Ritchie",
    "Java": "James Gosling",
    "C++": "Bjarne Stroustrup"
}
for key, value in languages.items():
    print(key, ":", value)


#10.Accept five student names and their marks from the user and store them in a dictionary.
students = {}
for i in range(5):
    name = input("Enter student name: ")
    mark = float(input("Enter marks: "))
    students[name] = mark
print(students)


# 11.Create a dictionary containing student names and marks. Find the student who has scored the highest marks.
students = {
    "Atharv": 85,
    "Rahul": 78,
    "Amit": 95,
    "Rohit": 88
}
highest = max(students, key=students.get)
print("Highest:", highest, students[highest])


# 12.Create a dictionary containing student names and marks. Find the student with the lowest marks.
students = {
    "Atharv": 85,
    "Rahul": 78,
    "Amit": 95,
    "Rohit": 65
}
lowest = min(students, key=students.get)
print("Lowest:", lowest, students[lowest])


# 13.Create a dictionary containing student names and marks. Calculate the average marks of all students.
students = {
    "Atharv": 85,
    "Rahul": 78,
    "Amit": 95,
    "Rohit": 65
}
average = sum(students.values()) / len(students)
print("Average:", average)


# 14.Accept a string from the user and create a dictionary containing each character and its frequency.
text = input("Enter a string: ")
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1
print(frequency)


# 15.Accept a sentence and create a dictionary containing each word and the number of times it occurs.
sentence = input("Enter a sentence: ")
frequency = {}
for word in sentence.split():
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)


# 16.Create two dictionaries and merge them into a single dictionary.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(merged)


# 17.Given two dictionaries, find the keys that are common to both dictionaries.
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 5, "c": 6, "d": 7}
common_keys = dict1.keys() & dict2.keys()
print("Common keys:", common_keys)


# 18.Given two dictionaries, identify the values that are common to both dictionaries.
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"x": 20, "y": 40, "z": 30}
common_values = set(dict1.values()) & set(dict2.values())
print("Common values:", common_values)


# 19.Create a dictionary containing duplicate values and remove duplicate values while retaining the corresponding keys where appropriate.
data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}
result = {}
for key, value in data.items():
    if value not in result.values():
        result[key] = value
print(result)


# 20.Create a dictionary and display its elements in ascending order of keys.
data = {
    4: "D",
    1: "A",
    3: "C",
    2: "B"
}
for key in sorted(data):
    print(key, ":", data[key])


#21.Create a dictionary containing numbers from 1 to 10 as keys and their squares as values.
squares = {}
for i in range(1, 11):
    squares[i] = i ** 2
print(squares)


#22.Create a dictionary containing numbers from 1 to 20 as keys and their squares as values, but include only even numbers.
squares = {}
for i in range(1, 21):
    if i % 2 == 0:
        squares[i] = i ** 2
print(squares)


#23.Given a list of numbers, create a dictionary containing each unique number and its frequency.
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
print(frequency)


# 24.Create a dictionary containing integers from 1 to 10 and their cubes.
cubes = {}
for i in range(1, 11):
    cubes[i] = i ** 3
print(cubes)


# 25.Create a dictionary containing student names and marks. Develop a program to:
#•	Add a student 
#•	Update marks 
#•	Delete a student 
#•	Search for a student 
#•	Display all students 
#•	Find the highest marks 
#•	Calculate the average

students = {
    "Atharv": 85,
    "Rahul": 78,
    "Amit": 92
}

while True:
    print("\n1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display All")
    print("6. Highest Marks")
    print("7. Average")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        students[name] = marks

    elif choice == 2:
        name = input("Enter name: ")
        if name in students:
            students[name] = float(input("Enter new marks: "))
        else:
            print("Student not found")

    elif choice == 3:
        name = input("Enter name: ")
        if name in students:
            del students[name]
        else:
            print("Student not found")

    elif choice == 4:
        name = input("Enter name: ")
        if name in students:
            print(name, ":", students[name])
        else:
            print("Student not found")

    elif choice == 5:
        print(students)

    elif choice == 6:
        name = max(students, key=students.get)
        print("Highest:", name, students[name])

    elif choice == 7:
        print("Average:", sum(students.values()) / len(students))

    elif choice == 8:
        break

    else:
        print("Invalid choice")


# 26. Employee salary analysis
employees = {
    "Atharv": 60000,
    "Rahul": 45000,
    "Amit": 75000,
    "Rohit": 52000
}

print("Highest salary:", max(employees.values()))
print("Lowest salary:", min(employees.values()))
print("Average salary:", sum(employees.values()) / len(employees))

print("Employees earning more than 50000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, salary)


# 27. Product quantity management
products = {
    "Pen": 20,
    "Book": 5,
    "Bag": 15
}

while True:
    print("\n1. Add Product")
    print("2. Update Quantity")
    print("3. Delete Product")
    print("4. Search Product")
    print("5. Products Below 10")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter product: ")
        quantity = int(input("Enter quantity: "))
        products[name] = quantity

    elif choice == 2:
        name = input("Enter product: ")
        if name in products:
            products[name] = int(input("Enter new quantity: "))
        else:
            print("Product not found")

    elif choice == 3:
        name = input("Enter product: ")
        if name in products:
            del products[name]
        else:
            print("Product not found")

    elif choice == 4:
        name = input("Enter product: ")
        if name in products:
            print(name, ":", products[name])
        else:
            print("Product not found")

    elif choice == 5:
        for name, quantity in products.items():
            if quantity < 10:
                print(name, quantity)

    elif choice == 6:
        break

    else:
        print("Invalid choice")


# 28. Contact management system
contacts = {
    "Atharv": "9876543210",
    "Rahul": "9876501234"
}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone

    elif choice == 2:
        name = input("Enter name: ")
        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("Contact not found")

    elif choice == 3:
        name = input("Enter name: ")
        if name in contacts:
            contacts[name] = input("Enter new phone: ")
        else:
            print("Contact not found")

    elif choice == 4:
        name = input("Enter name: ")
        if name in contacts:
            del contacts[name]
        else:
            print("Contact not found")

    elif choice == 5:
        print(contacts)

    elif choice == 6:
        break

    else:
        print("Invalid choice")


# 29. Book management system
books = {
    101: "Python Programming",
    102: "Data Structures",
    103: "Computer Networks"
}

while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Remove Book")
    print("4. Display All Books")
    print("5. Count Books")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book_id = int(input("Enter book ID: "))
        name = input("Enter book name: ")
        books[book_id] = name

    elif choice == 2:
        book_id = int(input("Enter book ID: "))
        if book_id in books:
            print(books[book_id])
        else:
            print("Book not found")

    elif choice == 3:
        book_id = int(input("Enter book ID: "))
        if book_id in books:
            del books[book_id]
        else:
            print("Book not found")

    elif choice == 4:
        print(books)

    elif choice == 5:
        print("Total books:", len(books))

    elif choice == 6:
        break

    else:
        print("Invalid choice")


#30.Take a dictionary containing student names and their departments; create a new dictionary that groups students according to their department.
students = {
    "Atharv": "CSE",
    "Rahul": "IT",
    "Amit": "CSE",
    "Rohit": "ECE",
    "Priya": "IT"
}
groups = {}
for name, department in students.items():
    if department not in groups:
        groups[department] = []
    groups[department].append(name)
print(groups)

#31.Take a list of words, create a dictionary where the key is the word length and the value is a list of words having that length.
words = ["cat", "dog", "apple", "book", "banana", "sun"]
groups = {}
for word in words:
    length = len(word)
    if length not in groups:
        groups[length] = []
    groups[length].append(word)

print(groups)

#32.Take a list of integers and a target value, find two numbers whose sum is equal to the target using a dictionary.
numbers = [2, 7, 11, 15]
target = 9
seen = {}
for num in numbers:
    complement = target - num
    if complement in seen:
        print("Numbers:", complement, num)
        break
    seen[num] = True

#33.Take a string, use a dictionary to find the first character that occurs only once.
text = input("Enter a string: ")
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1
for ch in text:
    if frequency[ch] == 1:
        print("First non-repeating character:", ch)
        break

#34.Take a string, use a dictionary to find the first character that occurs more than once.
text = input("Enter a string: ")
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1
for ch in text:
    if frequency[ch] > 1:
        print("First repeating character:", ch)
        break

#35.Accept a paragraph and create a dictionary where:
#•	Key = word length 
#•	Value = number of words having that length.
paragraph = input("Enter a paragraph: ")
words = paragraph.split()
length_count = {}

for word in words:
    length = len(word)
    length_count[length] = length_count.get(length, 0) + 1

print(length_count)
