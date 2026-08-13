# Import array module
import array as arr
a = arr.array('i', [1, 2, 3])
print("The newly created array is:", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")


# Double array
b = arr.array('d', [2.5, 3.2, 3.3])
print("\nThe newly created array is:", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")

#Inserting Array
import array as arr
a = arr.array('i', [1, 2, 3])      
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
a.insert(1, 4)             
print("Array after insertion : ", end=" ")
for i in (a):
    print(i, end=" ")

#Create an array 
from array import array
a = array('i', [10, 20, 30, 40, 50])
print("Array:", a)


#sum of elements in an array.
from array import array
a = array('i', [10, 20, 30, 40, 50])
s = 0
for n in a:
    s = s + n
print("Sum:", s)
from array import array
a = array('i', [10, 20, 30, 40, 50])
print("Position of 30:", a.index(30))

#position of a given element in an array.
from array import array
a = array('i', [10, 20, 30, 40, 50])
n = int(input("Enter element: "))
if n in a:
    print("Position:", a.index(n))
else:
    print("Not found")


#Search for an element
from array import array
a = array('i', [10, 20, 30, 40, 50])
n = int(input("Enter element: "))
if n in a:
    print("Found")
else:
    print("Not found")


#common elements between two arrays.
from array import array
a = array('i', [10, 20, 30, 40])
b = array('i', [30, 40, 50, 60])
c = array('i', [])
for n in a:
    if n in b:
        c.append(n)
print("Common elements:", c)


#Calculate the average of elements in an array.

from array import array
a = array('i', [10, 20, 30, 40, 50])
s = 0
for n in a:
    s = s + n
avg = s / len(a)
print("Average:", avg)


#Copy the elements of one array into another array.
from array import array
a = array('i', [10, 20, 30, 40, 50])
b = array('i', [])
for n in a:
    b.append(n)
print("Original array:", a)
print("Copied array:", b)


#Array built-in functions and methods.

from array import array
a = array('i', [10, 20, 30, 20, 40])
print("Length:", len(a))
a.append(50)
print("After append:", a)
a.insert(2, 25)
print("After insert:", a)
a.remove(20)
print("After remove:", a)
a.pop()
print("After pop:", a)
print("Position of 30:", a.index(30))
print("Count of 20:", a.count(20))
a.reverse()
print("After reverse:", a)
a.extend([60, 70])
print("After extend:", a)
b = a.tolist()
print("List:", b)

# Slicing an array
from array import array
a = array('i', [10, 20, 30, 40, 50])
print("Array:", a)
print("First three elements:", a[0:3])
print("Last two elements:", a[3:5])
print("Alternate elements:", a[::2])