#Numpy Basics
#1]
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#2]
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Dimensions:", arr.ndim)
print("Size:", arr.size)
print("Data type:", arr.dtype)

#3]
import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr)
print("Rows and columns:", arr.shape)

#4]
import numpy as np
a = np.array([10, 20, 30])
b = np.array([2, 4, 5])
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Exponentiation:", a ** b)
print("Modulus:", a % b)

#5]
import numpy as np
arr = np.array([10, 25, 5, 40, 15])
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))

#6]
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])
print(arr[2])
print(arr[-1])

#7]
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])
print(arr[:3])
print(arr[2:])

#8]
import numpy as np
arr = np.arange(1, 10)
new_arr = arr.reshape(3, 3)
print(new_arr)

#9]
import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr)
print("Flattened array:", arr.flatten())

#10]
import numpy as np
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
print(a + b)


# 11
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Array:", arr)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
print("Number of Dimensions:", arr.ndim)


# 12
import numpy as np
a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)


# 13
import numpy as np
arr = np.array([10, 25, 5, 40, 15, 30, 20, 35, 45, 50])
print("Array:", arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))


# 4
import numpy as np
arr = np.arange(1, 21)
even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]
print("Array:", arr)
print("Even Numbers:", even)
print("Odd Numbers:", odd)


# 15
import numpy as np
arr = np.arange(1, 13)
print("Original Array:", arr)
print("2 x 6 Matrix:")
print(arr.reshape(2, 6))
print("3 x 4 Matrix:")
print(arr.reshape(3, 4))
print("4 x 3 Matrix:")
print(arr.reshape(4, 3))


# 16
import numpy as np
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
b = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])
print("Matrix A:")
print(a)
print("Matrix B:")
print(b)
print("Matrix Addition:")
print(a + b)


# 17
import numpy as np
a = np.array([
    [1, 2],
    [3, 4]
])
b = np.array([
    [5, 6],
    [7, 8]
])
print("Matrix A:")
print(a)
print("Matrix B:")
print(b)
print("Matrix Multiplication:")
print(np.dot(a, b))


# 18
import numpy as np
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print("Original Matrix:")
print(arr)
print("Transpose:")
print(arr.T)


# 19
import numpy as np
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
print("First Row:")
print(arr[0])
print("Last Column:")
print(arr[:, -1])
print("Diagonal Elements:")
print(np.diag(arr))
print("Second and Third Rows:")
print(arr[1:3])


# 20
import numpy as np
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
print("Matrix:")
print(arr)
print("Sum of Each Row:")
print(np.sum(arr, axis=1))
print("Sum of Each Column:")
print(np.sum(arr, axis=0))


# 21
import numpy as np
arr = np.arange(1, 21)
print("Array:", arr)
print("First 5 Elements:")
print(arr[:5])
print("Last 5 Elements:")
print(arr[-5:])
print("Alternate Elements:")
print(arr[::2])
print("Reverse Order:")
print(arr[::-1])

#22 
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Original Array:", arr)
arr[arr > 50] = 0
print("Array after replacement:", arr)

#23
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
print("Original Array:", arr)
print("Ascending Order:", np.sort(arr))
print("Descending Order:", np.sort(arr)[::-1])

#24 
arr = np.array([1, 2, 2, 3, 3, 4, 4, 5, 5])
print("Original Array:", arr)
print("Unique Elements:", np.unique(arr))

#25
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])   
arr2 = np.array([[5, 6], [7, 8]])
horizontal_concat = np.hstack((arr1, arr2))
vertical_concat = np.vstack((arr1, arr2))
print("Horizontal Concatenation:")
print(horizontal_concat)
print("Vertical Concatenation:")
print(vertical_concat)

#26
import numpy as np
marks = np.array([85, 92, 78, 96, 88, 91, 84, 89, 93, 87])
print("Marks:", marks)
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))

#27
import numpy as np
marks = np.array([85, 92, 78, 96, 88, 91, 84, 89, 93, 87, 90, 82, 95, 86, 94, 81, 83, 97, 79, 80])
average_marks =np.mean(marks)
print("Class Average:", average_marks)
print("Marks of Students Above Average:")
print(marks[marks > average_marks])

#28
import numpy as np
arr=np.arange(1, 25).reshape(2, 3, 4)
print("3D Array=", arr)
print("Number of Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)

#29 
import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
print("3D Array:")
print(arr)
print("First Element:", arr[0, 0, 0])
print("Last Element:", arr[-1, -1, -1])
print("Element at index [0, 1, 2]:", arr[0, 1, 2])
print("Element at index [1, 2, 3]:", arr[1, 2, 3])

#30 
import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
print("3D Array:")
print(arr)
print("Sum of all elements:", np.sum(arr))
print("Sum of each layer:", np.sum(arr, axis=(1, 2)))
print("Sum along rows:", np.sum(arr, axis=1))
print("Sum along columns:", np.sum(arr, axis=2))

#31 
import numpy as np
arr = np.random.randint(1, 101, size=(3, 4, 5))
print("Original 3D Array:")
print(arr)
arr[arr > 50] = 0
print("Modified 3D Array (values > 50 replaced with 0):")
print(arr)

#32.
import numpy as np
arr = np.random.randint(1, 101, size=(3, 4, 5))
print("Original 3D Array:")
print(arr)
mean = np.mean(arr)
median = np.median(arr)
std_dev = np.std(arr)
variance = np.var(arr)
minimum = np.min(arr)
maximum = np.max(arr)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Variance:", variance)
print("Minimum:", minimum)
print("Maximum:", maximum)

#33.
import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
flattened_arr = arr.flatten()   
print("Original 3D Array:")
print(arr)
print("Flattened 1D Array:")
print(flattened_arr)

#34.
import numpy as np
arr = np.arange(1, 28).reshape(3, 3, 3)
flattened_arr = arr.flatten()
sum_of_elements = np.sum(flattened_arr)
average_of_elements = np.mean(flattened_arr)
maximum_element = np.max(flattened_arr)
minimum_element = np.min(flattened_arr)
print("Original 3D Array:")
print(arr)
print("Flattened 1D Array:")
print(flattened_arr)
print("Sum of Elements:", sum_of_elements)
print("Average of Elements:", average_of_elements)
print("Maximum Element:", maximum_element)
print("Minimum Element:", minimum_element)


#35.	Create a random 3D NumPy array of shape (3, 4, 5). Flatten it and display only the elements that are:•	Greater than 50 •	Even numbers •	Less than the average value
import numpy as np
arr = np.random.randint(1, 101, size=(3, 4, 5))
flattened_arr = arr.flatten()
average_value = np.mean(flattened_arr)
print("Original 3D Array:")
print(arr)
print("Flattened 1D Array:")
print(flattened_arr)
print("Elements greater than 50:")
print(flattened_arr[flattened_arr > 50])
print("Even numbers:")
print(flattened_arr[flattened_arr % 2 == 0])
print("Elements less than the average value:")
print(flattened_arr[flattened_arr < average_value])




















