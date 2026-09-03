#Write a Python program to create a file named student.txt and write the student's name, roll number, branch, and semester into the file. 
name = input("Enter student's name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")
f = open("student.txt", "w")
f.write("Name: " + name + "\n")
f.write("Roll Number: " + roll + "\n")
f.write("Branch: " + branch + "\n")
f.write("Semester: " + semester + "\n")
f.close()
print("student.txt file created successfully!")

#Write a program to open a text file and display its complete contents. 
f = open("student.txt", "r")
print(f.read())
f.close()

# Write a program to append additional student information to an existing file without deleting its previous contents.
# Append additional student information without deleting old contents.
stud_id= input("Enter student's name: ")
f= open("student.txt", "a")
f.write("\nStudent ID: " + stud_id + "\n")
print("Student information added successfully!")

#Write a program to read a text file line by line and display each line separately. 
f = open("student.txt", "r")
for line in f:
    print(line)
f.close()

#Count total number of lines
f = open("student.txt", "r")
lines = f.readlines()
print("Total number of lines:", len(lines))
f.close()


#Count total number of words
f = open("student.txt", "r")
data = f.read()
words = data.split()
print("Total number of words:", len(words))
f.close()


# Count total number of characters including spaces
f = open("student.txt", "r")
data = f.read()
print("Total number of characters:", len(data))
f.close()


#Display lines in reverse order
f = open("student.txt", "r")
lines = f.readlines()
lines.reverse()
print("Lines in reverse order:")
for line in lines:
    print(line, end="")
f.close()

#Count vowels and consonants
f = open("student.txt", "r")
data = f.read()
vowels = 0
consonants = 0
for ch in data:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("\nVowels:", vowels)
print("Consonants:", consonants)

f.close()


#Count alphabets, digits, spaces and special characters
f = open("student.txt", "r")
data = f.read()
alphabets = 0
digits = 0
spaces = 0
special = 0
for ch in data:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1
print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)
f.close()

#Read a text file and find the longest word present in the file.
f = open("student.txt", "r")
data = f.read() 
words = data.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("Longest word:", longest_word)
f.close()

#Read a text file and count how many times each word occurs. Display the result using a dictionary.
f = open("student.txt", "r")
data = f.read()
words = data.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print("Word occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")
f.close()

#Accept a word from the user and search for it in a text file. Display the number of occurrences and the line numbers where it appears.
word = input("Enter a word to search for: ")
f = open("student.txt", "r")
occurrences = 0
line_numbers = []
for line_number, line in enumerate(f, start=1):
    if word in line:
        occurrences += line.count(word)
        line_numbers.append(line_number)
        
f.close()
print(f"Occurrences of '{word}': {occurrences}")
print(f"Line numbers where '{word}' appears: {line_numbers}")

#Read a text file and replace all occurrences of a specified word with another word. Save the modified text in the same file or a new file.
f = open("student.txt", "r")
data = f.read()
f.close()

old_word = input("Enter the word to be replaced: ")
new_word = input("Enter the new word: ")
data = data.replace(old_word, new_word)

f = open("student.txt", "w")
f.write(data)
f.close()
print("File updated successfully.")

#Read a Python source file and create another file after removing single-line comments.
f = open("source.py", "r")
data = f.read()
f.close()
lines = data.split('\n')
modified_lines = []
for line in lines:
    if line.strip().startswith('#'):
        continue
    modified_lines.append(line)
f = open("modified.py", "w")
f.write('\n'.join(modified_lines))
f.close()
print("File updated successfully.")

#Read a text file and create another file containing the same text in uppercase.
f = open("student.txt", "r")
data = f.read()
f.close()
data = data.upper()
f = open("student_upper.txt", "w")
f.write(data)
f.close()
print("File updated successfully.")

# Create a file containing student records in the format:
# RollNo,Name,Marks
# 101,Amit,85
# 102,Priya,92
# 103,Rahul,78
# Write a program to:
# Display all records.
# Find the student with the highest marks.
# Calculate average marks.
# Display students who scored more than 80.

f = open("students.txt", "w")
f.write("RollNo,Name,Marks\n")
f.write("101,Amit,85\n")
f.write("102,Priya,92\n")
f.write("103,Rahul,78\n")
f.close()
f = open("students.txt", "r")
lines = f.readlines()
f.close()
total = 0
highest = 0
highest_name = ""
print("All Records:")
for line in lines[1:]:
    data = line.strip().split(",")
    roll = data[0]
    name = data[1]
    marks = int(data[2])

    print(roll, name, marks)

    total = total + marks

    if marks > highest:
        highest = marks
        highest_name = name

print("Highest Marks:", highest_name, highest)
print("Average Marks:", total / (len(lines) - 1))

print("Students who scored more than 80:")
for line in lines[1:]:
    data = line.strip().split(",")
    name = data[1]
    marks = int(data[2])

    if marks > 80:
        print(name, marks)


# Store employee ID, name, department, and salary in a file.
# Write functions to:
# Display all employees.
# Find the highest-paid employee.
# Calculate average salary.
# Display employees earning above a given salary.

f = open("employees.txt", "w")
f.write("ID,Name,Department,Salary\n")
f.write("101,Amit,IT,50000\n")
f.write("102,Priya,HR,60000\n")
f.write("103,Rahul,Sales,45000\n")
f.close()


def display_employees():
    f = open("employees.txt", "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        print(line.strip())


def highest_paid():
    f = open("employees.txt", "r")
    lines = f.readlines()
    f.close()

    highest = 0
    name = ""

    for line in lines[1:]:
        data = line.strip().split(",")
        salary = int(data[3])

        if salary > highest:
            highest = salary
            name = data[1]

    print("Highest Paid Employee:", name, highest)


def average_salary():
    f = open("employees.txt", "r")
    lines = f.readlines()
    f.close()

    total = 0

    for line in lines[1:]:
        data = line.strip().split(",")
        total = total + int(data[3])

    print("Average Salary:", total / (len(lines) - 1))


def above_salary(amount):
    f = open("employees.txt", "r")
    lines = f.readlines()
    f.close()

    print("Employees earning above", amount)

    for line in lines[1:]:
        data = line.strip().split(",")
        salary = int(data[3])

        if salary > amount:
            print(data[1], salary)


display_employees()
highest_paid()
average_salary()
above_salary(50000)


# Store student attendance records in a file.
# Calculate the attendance percentage and display students having attendance below 75%.

f = open("attendance.txt", "w")
f.write("RollNo,Name,Present,Total\n")
f.write("101,Amit,80,100\n")
f.write("102,Priya,70,100\n")
f.write("103,Rahul,90,100\n")
f.close()

f = open("attendance.txt", "r")
lines = f.readlines()
f.close()

for line in lines[1:]:
    data = line.strip().split(",")

    name = data[1]
    present = int(data[2])
    total = int(data[3])

    percentage = (present / total) * 100

    print(name, "Attendance:", percentage, "%")

    if percentage < 75:
        print(name, "has attendance below 75%")


# Store deposits and withdrawals in a file.
# Read the file and calculate:
# Total deposits
# Total withdrawals
# Final balance
# Largest transaction

f = open("transactions.txt", "w")
f.write("Deposit,10000\n")
f.write("Withdrawal,2000\n")
f.write("Deposit,5000\n")
f.write("Withdrawal,1000\n")
f.close()

f = open("transactions.txt", "r")
lines = f.readlines()
f.close()

total_deposit = 0
total_withdrawal = 0
largest = 0

for line in lines:
    data = line.strip().split(",")
    transaction = data[0]
    amount = int(data[1])

    if transaction == "Deposit":
        total_deposit = total_deposit + amount
    else:
        total_withdrawal = total_withdrawal + amount

    if amount > largest:
        largest = amount

balance = total_deposit - total_withdrawal

print("Total Deposits:", total_deposit)
print("Total Withdrawals:", total_withdrawal)
print("Final Balance:", balance)
print("Largest Transaction:", largest)


# Maintain book records containing book ID, title, author, and availability status.
# Implement operations to:
# Add a book.
# Search for a book.
# Issue a book.
# Return a book.
# Display available books.

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")

    f = open("books.txt", "a")
    f.write(book_id + "," + title + "," + author + ",Available\n")
    f.close()

    print("Book added successfully")


def search_book():
    book_id = input("Enter Book ID to search: ")

    f = open("books.txt", "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        data = line.strip().split(",")

        if data[0] == book_id:
            print("Book Found:", line.strip())
            return

    print("Book not found")


def issue_book():
    book_id = input("Enter Book ID to issue: ")

    f = open("books.txt", "r")
    lines = f.readlines()
    f.close()

    f = open("books.txt", "w")

    for line in lines:
        data = line.strip().split(",")

        if data[0] == book_id and data[3] == "Available":
            data[3] = "Issued"

        f.write(",".join(data) + "\n")

    f.close()

    print("Book issued")


def return_book():
    book_id = input("Enter Book ID to return: ")

    f = open("books.txt", "r")
    lines = f.readlines()
    f.close()

    f = open("books.txt", "w")

    for line in lines:
        data = line.strip().split(",")

        if data[0] == book_id:
            data[3] = "Available"

        f.write(",".join(data) + "\n")

    f.close()

    print("Book returned")


def display_available():
    f = open("books.txt", "r")
    lines = f.readlines()
    f.close()

    print("Available Books:")

    for line in lines:
        data = line.strip().split(",")

        if data[3] == "Available":
            print(line.strip())



# Read the contents of two text files and create a third file containing the contents of both files.

f = open("file1.txt", "r")
data1 = f.read()
f.close()

f = open("file2.txt", "r")
data2 = f.read()
f.close()

f = open("file3.txt", "w")
f.write(data1)
f.write("\n")
f.write(data2)
f.close()

print("Contents of both files copied to file3.txt")


# Write a program to compare two text files and display whether their contents are identical.
# If different, identify the first line where they differ.

f1 = open("file1.txt", "r")
lines1 = f1.readlines()
f1.close()
f2 = open("file2.txt", "r")
lines2 = f2.readlines()
f2.close()
same = True

length = min(len(lines1), len(lines2))
for i in range(length):
    if lines1[i] != lines2[i]:
        print("Files are different")
        print("First different line:", i + 1)
        same = False
        break

if same:
    if len(lines1) == len(lines2):
        print("Files are identical")
    else:
        print("Files are different")
        print("First different line:", length + 1)