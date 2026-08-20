#1.	Write a Python program to create a set containing five integers and display all its elements.
s={1,2,3,4,5}
print(s)

#2.	Create a list containing duplicate values. Convert the list into a set and display the resulting set.
s = [10, 20, 10, 30, 20, 40, 30]
r = set(s)
print(r)

# 3. Create a list of colors. Replace the third color with another color and display the updated list.
colors = ["Red", "Blue", "Green", "Yellow", "Black"]
colors[2] = "Purple"
print("Updated Colors:", colors)

#4.	Create a set of numbers and remove a specified number from the set.
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print("Updated Set:", numbers)

#5.	Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
students = {"Alice", "Bob", "Charlie", "David"}
name = input("Enter a student name: ")
if name in students:
    print("Student exists in the set.")
else:
    print("Student does not exist in the set.")

#6.	Create a set of cities and determine the total number of cities using an appropriate function.
cities = {"New York", "Los Angeles", "Chicago", "Houston", "Phoenix"}
total_cities = len(cities)
print("Total number of cities:", total_cities)

#7.	Create a set of programming languages and display each language using a for loop.
languages = {"Python", "Java", "C++", "JavaScript"}
print("Programming languages:")
for lang in languages:
    print(lang)

#8.	Create a list containing duplicate numbers, use a set to remove the duplicates.
numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
unique_numbers = set(numbers)
print("Unique numbers:", unique_numbers)


#9.	Create two sets of integers and find their union.
s1={1,2,4,4,6,7,8}
s2={3,4,5,1,3,8,9}
print(s1|s2)

#10.Create two sets and find the elements common to both sets.
s1={1,2,4,4,6,7,8}
s2={3,4,5,1,3,8,9}
print(s1-s2)

#11.Create two sets and find:
#•	Elements present in the first set but not the second 
#•	Elements present in the second set but not the first
s1={1,2,4,4,6,7,8}
s2={3,4,5,1,3,8,9}
print("Elements present in the first set but not the second:", s1 - s2)
print("Elements present in the second set but not the first:", s2 - s1)

#12.Create two sets of numbers and find the elements that are present in either set but not in both.
s1={1,2,4,4,6,7,8}
s2={3,4,5,1,3,8,9}
print("Elements=:", s1 ^ s2)

#13.Create two sets and determine whether the first set is a subset of the second set.
s1={1,2,4,4,6,7,8}
s2={3,4,5,1,3,8,9}
print("Present or not=", s1.issubset(s2))

#14.Create two sets and determine whether the first set is a superset of the second set.
s1={1,2,4,4,6,7,8}
s2={3,4,5,1,3,8,9}
print("Is s1 a superset of s2?", s1.issuperset(s2))

#15.Write a program to determine whether two sets have no elements in common.
s1={1,2,4,4,6,7,8}
s2={3,4,5,1,3,8,9}
print("Common elements=", s1.isdisjoint(s2))

#16.Create two sets and check whether they are equal.
s1={1,2,4,4,6,7,8}
s2={3,4,5,1,3,8,9}
print("Equal=", s1 == s2)

#17.Two students have selected different subjects. Store their subjects in two sets and determine the subjects studied by both students.
student1 = {"Math", "Science", "English"}
student2 = {"Science", "History", "English"}
common_subjects = student1.intersection(student2)
print("Subjecta=:", common_subjects)

#18.Accept a sentence from the user and use a set to display all unique words.
s = input("Enter a sentence: ")
words = s.split()
unique_words = set(words)
print("Unique words:", unique_words)

#19.Create two sets:
#•	Students present in the morning session 
#•	Students present in the afternoon session 
##Find:
#•	Students present in both sessions 
#•	Students present only in the morning 
#•	Students present only in the afternoon 
#•	Students present in at least one session
s1={"Alice", "Bob", "Charlie", "David" }
s2={"Charlie", "David", "Eve", "Frank" }
print(" both sessions:", s1.intersection(s2))
print("only in the morning:", s1 - s2)
print(" only in the afternoon:", s2 - s1)
print("present in at least one session:", s1.union(s2))

#20.Create sets representing students enrolled in:
#•	Python 
#•	Java
python = {"Alice", "Bob", "Charlie"}
java = {"Charlie", "David", "Eve"} 
print("Students enrolled in Python:", python)
print("Students enrolled in Java:", java)

#21.Find students enrolled in both courses and students enrolled in only one course.
both = python.intersection(java)
python = python - java
java = java - python
print("Students enrolled in both courses:", both)
print("Students enrolled in only Python:", python)
print("Students enrolled in only Java:", java)

#22.Create two sets representing technical skills of two employees. Find:
#•	Common skills 
#•	Skills unique to Employee 1 
#•	Skills unique to Employee 2 
#•	All available skills

employee1= {"Python", "Java", "C++", "JavaScript"}
employee2 = {"Python", "JavaScript", "SQL", "React"}
common = employee1.intersection(employee2)
unique_to_employee1 = employee1 - employee2
unique_to_employee2 = employee2 - employee1
all_available_skills = employee1.union(employee2)
print("Common skills:", common)
print("Skills unique to Employee 1:", unique_to_employee1)
print("Skills unique to Employee 2:", unique_to_employee2)
print("All available skills:", all_available_skills)

#23.Create a set containing available books and another set containing requested books. Determine which requested books are available.
available_books = {"Book A", "Book B", "Book C", "Book D"}
requested_books = {"Book B", "Book E", "Book C", "Book F"}
a1 = requested_books.intersection(available_books)
print("Available requested books:", a1)

#24.Store visitor IDs from two different days in separate sets. Determine:
#•	Unique visitors across both days 
#•	Returning visitors 
#•	Visitors who came only on the first day 
#•	Visitors who came only on the second day
#•	Create sets representing products belonging to different categories. Find products that belong to both categories.

s1 = {101, 102, 103, 104, 105}
s2 = {104, 105, 106, 107, 108}
unique_visitors = s1.union(s2)
returning_visitors = s1.intersection(s2)
only_first_day = s1 - s2
only_second_day = s2 - s1
print("Unique visitors across both days:", unique_visitors)
print("Returning visitors:", returning_visitors)
print("Visitors who came only on the first day:", only_first_day)
print("Visitors who came only on the second day:", only_second_day)

#25.Represent the friends of two users using sets. Find:
#•	Mutual friends 
#•	Friends unique to User 1 
#•	Friends unique to User 2 
#•	Total unique friends

user1_friends = {"Alice", "Bob", "Charlie"}
user2_friends = {"Charlie", "David", "Eve"}
mutual_friends = user1_friends.intersection(user2_friends)
unique_to_user1 = user1_friends - user2_friends
unique_to_user2 = user2_friends - user1_friends
total_unique_friends = user1_friends.union(user2_friends)
print("Mutual friends:", mutual_friends)
print("Friends unique to User 1:", unique_to_user1)
print("Friends unique to User 2:", unique_to_user2)
print("Toatal unique friends=",total_unique_friends)




