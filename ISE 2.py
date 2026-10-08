a] def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")

    with open("students.txt", "a") as file:
        file.write(roll + "," + name + "," + course + "\n")

    print("Student record added successfully.")


def search_student():
    roll = input("Enter Roll Number to search: ")
    found = False

    with open("students.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            if data[0] == roll:
                print("Roll Number:", data[0])
                print("Name:", data[1])
                print("Course:", data[2])
                found = True
                break

    if not found:
        print("Student record not found.")


add_student()
search_student()

b]
1.string_module
def palindrome(s):
    return s == s[::-1]


def vowel_count(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count


def character_frequency(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    return freq
2.Main.py
import string_module

text = input("Enter a string: ")

if string_module.palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

print("Number of vowels:",
      string_module.vowel_count(text))

print("Character frequency:",
      string_module.character_frequency(text))

c]
def add_record():
    try:
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Student Name: ")
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))

        with open("college.txt", "a") as file:
            file.write(f"{roll},{name},{course},{marks}\n")

        print("Record added successfully.")

    except ValueError:
        print("Invalid input! Please enter correct values.")


def display_records():
    try:
        with open("college.txt", "r") as file:
            print("\nCollege Records")
            print("-" * 40)

            for line in file:
                roll, name, course, marks = line.strip().split(",")
                print("Roll No :", roll)
                print("Name    :", name)
                print("Course  :", course)
                print("Marks   :", marks)
                print("-" * 40)

    except FileNotFoundError:
        print("No records found.")


def search_record():
    try:
        roll = input("Enter Roll Number to search: ")
        found = False

        with open("college.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if data[0] == roll:
                    print("\nRecord Found")
                    print("Roll No :", data[0])
                    print("Name    :", data[1])
                    print("Course  :", data[2])
                    print("Marks   :", data[3])
                    found = True
                    break

        if not found:
            print("Record not found.")

    except FileNotFoundError:
        print("File does not exist.")


while True:
    print("\n--- COLLEGE RECORD MANAGEMENT SYSTEM ---")
    print("1. Add Record")
    print("2. Display Records")
    print("3. Search Record")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_record()
        elif choice == 2:
            display_records()
        elif choice == 3:
            search_record()
        elif choice == 4:
            print("Program terminated.")
            break
        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a number.")