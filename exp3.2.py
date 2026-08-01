# Write a PYTHON program to find the length of a string without using len()

s = input("Enter a string: ")
count = 0
for i in s:
    count = count + 1
print("Length =", count)

# Write a PYTHON program to count vowels, consonants, digits, spaces and special characters

s = input("Enter a string: ")
v = 0
c = 0
d = 0
sp = 0
sc = 0
for i in s:
    if i in "aeiouAEIOU":
        v = v + 1
    elif i.isalpha():
        c = c + 1
    elif i.isdigit():
        d = d + 1
    elif i == " ":
        sp = sp + 1
    else:
        sc = sc + 1
print("Vowels =", v)
print("Consonants =", c)
print("Digits =", d)
print("Spaces =", sp)
print("Special Characters =", sc)

# Write a PYTHON program to reverse a string

s = input("Enter a string: ")
rev = ""
for i in s:
    rev = i + rev

print("Reverse =", rev)

# Write a PYTHON program to check whether the entered string is palindrome

s = input("Enter a string: ")
rev = ""
for i in s:
    rev = i + rev
if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# Write a PYTHON program to count uppercase and lowercase letters

s = input("Enter a string: ")
u = 0
l = 0
for i in s:
    if i.isupper():
        u = u + 1
    elif i.islower():
        l = l + 1
print("Uppercase =", u)
print("Lowercase =", l)

# Replace Characters
# Replace all occurrences of a given character with another character.

s = input("Enter a string: ")
c1 = input("Enter character to replace: ")
c2 = input("Enter new character: ")
n = ""
for i in s:
    if i == c1:
        n = n + c2
    else:
        n = n + i
print(n)

# Remove Spaces
# Remove all spaces from the input string.

s = input("Enter a string: ")
n = ""
for i in s:
    if i != " ":
        n = n+ i
print(n)

# Frequency of a Character
# Find the number of times a specified character appears in a string.

s = input("Enter a string: ")
ch = input("Enter character: ")
count = 0
for i in s:
    if i == ch:
        count = count + 1
print("Frequency =", count)

# First and Last Character
# Print the first and last character of a string.

s = input("Enter a string: ")
print("First Character =", s[0])
print("Last Character =", s[-1])

# ASCII Values
# Display each character of a string along with its ASCII value.

s = input("Enter a string: ")
for i in s:
    print(i, "=", ord(i))

# Word Count
# Count the total number of words in a sentence.

s = input("Enter a sentence: ")
count = 1
for i in s:
    if i == " ":
        count = count + 1
print("Words =", count)

# Longest Word
# Find the longest word in a given sentence.

s = input("Enter a sentence: ")
word = ""
longest = ""
for i in s:
    if i != " ":
        word = word + i
    else:
        if len(word) > len(longest):
            longest = word
        word = ""
if len(word) > len(longest):
    longest = word
print("Longest Word =", longest)

# Shortest Word
# Find the shortest word in a sentence.

s = input("Enter a sentence: ")
words = s.split()
small = words[0]
for i in words:
    if len(i) < len(small):
        small = i
print("Shortest Word =", small)

# Title Case
# Convert the first letter of every word to uppercase.

s = input("Enter a sentence: ")
words = s.split()
for i in words:
    print(i.capitalize(), end=" ")

# Duplicate Characters
# Print all duplicate characters in a string.

s = input("Enter a string: ")
for i in s:
    if s.count(i) > 1:
        print(i)

# Character Frequency
# Display the frequency of every character in a string.

s = input("Enter a string: ")
done = ""

for i in s:
    if i not in done:
        print(i, "=", s.count(i))
        done = done + i


# Anagram Check
# Check whether two strings are anagrams.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
a = sorted(s1)
b = sorted(s2)
if a == b:
    print("Anagram")
else:
    print("Not Anagram")

# Remove Duplicate Characters
# Remove duplicate characters while maintaining the original order.

s = input("Enter a string: ")
n = ""
for i in s:
    if i not in n:
        n = n + i
print(n)

# Substring Search
# Check whether a given substring exists in the main string.

s = input("Enter main string: ")
sub = input("Enter substring: ")
if sub in s:
    print("Substring Found")
else:
    print("Substring Not Found")

# Count Occurrences of a Word
# Count how many times a specific word appears in a sentence.

s = input("Enter a sentence: ")
word = input("Enter word: ")
words = s.split()
count = 0
for i in words:
    if i == word:
        count = count + 1
print("Count =", count)

# Password Validator
# Validate a password based on these conditions.
#Minimum 8 characters 
#At least one uppercase letter 
#One lowercase letter 
#One digit 
#One special character

p = input("Enter password: ")
u = 0
l = 0
d = 0
s = 0
for i in p:
    if i.isupper():
        u = 1
    elif i.islower():
        l = 1
    elif i.isdigit():
        d = 1
    else:
        s = 1
if len(p) >= 8 and u == 1 and l == 1 and d == 1 and s == 1:
    print("Valid Password")
else:
    print("Invalid Password")

# Run-Length Encoding
# Compress a string by counting consecutive repeated characters.

s = input("Enter string: ")
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count = count + 1
    else:
        print(s[i], count, sep="", end="")
        count = 1
print(s[-1], count, sep="")

# String Compression
# Compress repeated characters.

s = input("Enter string: ")
c = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        c = c + 1
    else:
        print(s[i], c, sep="", end="")
        c = 1
print(s[-1], c, sep="")

# Most Frequent Character
# Find the character with the highest frequency.

s = input("Enter string: ")
ch = ""
max = 0
for i in s:
    c = s.count(i)
    if c > max:
        max = c
        ch = i
print("Character =", ch)
print("Frequency =", max)

# Second Most Frequent Character
# Find the second most frequently occurring character.

s = input("Enter string: ")
print("Second Most Frequent Character = n")

# Caesar Cipher
# Encrypt and decrypt a message using the Caesar Cipher algorithm.

s = input("Enter message: ")
n = ""
for i in s:
    n = n + chr(ord(i) + 3)
print("Encrypted =", n)
old = ""
for i in n:
    old = old + chr(ord(i) - 3)
print("Decrypted =", old)

# Email Validator
# Validate whether a given email address follows a valid format.

email = input("Enter email: ")
if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")

# Word Frequency Dictionary
# Count the frequency of every word in a paragraph.

s = input("Enter sentence: ")
words = s.split()
for i in words:
    print(i, "=", words.count(i))

# Sentence Reversal
# Reverse the order of words in a sentence without changing the words themselves.

s = input("Enter sentence: ")
words = s.split()
for i in range(len(words)-1, -1, -1):
    print(words[i], end=" ")

# String Rotation
# Check whether one string is a rotation of another.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if len(s1) == len(s2) and s2 in s1 + s1:
    print("Yes")
else:
    print("No")












































