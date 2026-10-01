#1.
print("Program started")
import pandas as pd
print("Pandas imported")
data = {
    "Student ID": [101, 102, 103, 104, 105],
    "Student Name": ["Amit", "Priya", "Rahul", "Sneha", "Vikas"],
    "Python Marks": [85, 72, 90, 65, 78],
    "DBMS Marks": [80, 75, 88, 70, 82],
    "Mathematics Marks": [90, 68, 85, 75, 80]
}
df = pd.DataFrame(data)
print(df)

#2.
import pandas as pd
data = {
    "Student ID": [101, 102, 103, 104, 105],
    "Student Name": ["Amit", "Priya", "Rahul", "Sneha", "Vikas"],
    "Python Marks": [85, 72, 90, 65, 78],
    "DBMS Marks": [80, 75, 88, 70, 82],
    "Mathematics Marks": [90, 68, 85, 75, 80]
}
df = pd.DataFrame(data)
print("Student Data:")
print(df)
df["Total Marks"] = df["Python Marks"] + df["DBMS Marks"] + df["Mathematics Marks"]
df["Average Marks"] = df["Total Marks"] / 3
print("\nDataFrame with Total and Average Marks:")
print(df)
students_above_75 = df[df["Average Marks"] > 75]
print("\nStudents with Average Marks above 75%:")
print(students_above_75[["Student ID", "Student Name", "Average Marks"]])

#3
import pandas as pd
data = {
    "Employee ID": [101, 102, 103, 104, 105],
    "Employee Name": ["Amit", "Priya", "Rahul", "Sneha", "Vikas"],
    "Department": ["IT", "HR", "Finance", "IT", "Marketing"],
    "Salary": [55000, 48000, 65000, 52000, 75000],
    "Experience": [3, 5, 7, 4, 10]
}
df = pd.DataFrame(data)
print("Employee Data:")
print(df)
print("\nEmployees with Salary Greater Than ₹50,000:")
print(df[df["Salary"] > 50000])
average_salary = df["Salary"].mean()
print("\nAverage Salary:", average_salary)
highest_salary = df["Salary"].max()
print("Highest Salary:", highest_salary)
highest_experience = df["Experience"].max()
print("\nEmployee with Highest Experience:")
print(df[df["Experience"] == highest_experience])

#4
import pandas as pd
data = {
    "Product ID": [101, 102, 103, 104, 105],
    "Product Name": ["Laptop", "Mobile", "Keyboard", "Mouse", "Monitor"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Electronics"],
    "Price": [50000, 30000, 1500, 800, 12000],
    "Quantity": [5, 8, 20, 30, 10]
}
df = pd.DataFrame(data)
df["Total Amount"] = df["Price"] * df["Quantity"]
print(df)
print("\nProduct with Highest Total Sales:")
print(df[df["Total Amount"] == df["Total Amount"].max()])

#5
import pandas as pd
data = {
    "Patient ID": [101, 102, 103, 104, 105],
    "Patient Name": ["Amit", "Priya", "Rahul", "Sneha", "Vikas"],
    "Age": [65, 45, 72, 58, 67],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Asthma", "Cancer"],
    "Medical Charges": [55000, 25000, 80000, 35000, 65000]
}
df = pd.DataFrame(data)
print(df)
print("\nPatients above 60 years:")
print(df[df["Age"] > 60])
print("\nAverage Medical Charge:")
print(df["Medical Charges"].mean())
print("\nMaximum Medical Charge:")
print(df["Medical Charges"].max())
print("\nPatients with Medical Charges greater than 50000:")
print(df[df["Medical Charges"] > 50000])

#6
import pandas as pd

data = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Customer": ["Amit", "Priya", "Rahul", "Sneha", "Vikas"],
    "Product": ["Laptop", "Mobile", "Keyboard", "Monitor", "Tablet"],
    "Quantity": [2, 3, 5, 2, 4],
    "Price": [50000, 30000, 2000, 15000, 12000],
    "Discount": [5000, 3000, 1000, 2000, 1500]
}
df = pd.DataFrame(data)
df["Final Amount"] = df["Quantity"] * df["Price"] - df["Discount"]
print("All Orders:")
print(df)
print("\nOrders above 5000:")
print(df[df["Final Amount"] > 5000])
print("\nHighest-value Order:")
print(df[df["Final Amount"] == df["Final Amount"].max()])
print("\nAverage Order Value:")
print(df["Final Amount"].mean())

#7
import pandas as pd
data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Vikas"],
    "Department": ["IT", "CS", "IT", "ENTC", "CS"],
    "Total_Classes": [50, 50, 60, 40, 50],
    "Classes_Attended": [45, 35, 50, 28, 40]
}
df = pd.DataFrame(data)
df["Attendance Percentage"] = (df["Classes_Attended"] / df["Total_Classes"]) * 100
print(df)
print("\nStudents with attendance below 75%:")
print(df[df["Attendance Percentage"] < 75])

#8
import pandas as pd
data = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Monitor", "Tablet"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics"],
    "Price": [50000, 30000, 2000, 15000, 12000],
    "Quantity": [2, 3, 10, 2, 4]
}
df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Quantity"]
print("DataFrame:")
print(df)
print("\nProducts with sales greater than 10000:")
print(df[df["Total_Sales"] > 10000])
print("\nProduct with maximum sales:")
print(df[df["Total_Sales"] == df["Total_Sales"].max()])
print("\nAverage Sales:")
print(df["Total_Sales"].mean())

#9
import pandas as pd
data = {
    "Amit": 85,
    "Priya": 72,
    "Rahul": 90,
    "Sneha": 65,
    "Vikas": 78
}
s = pd.Series(data)
print("Student Marks:")
print(s)
print("\nMarks of Rahul:")
print(s["Rahul"])
print("\nMaximum Marks:")
print(s.max())
print("\nMinimum Marks:")
print(s.min())
print("\nAverage Marks:")
print(s.mean())
print("\nStudents who scored more than 75:")
print(s[s > 75])

#10
import pandas as pd

data = {
    "Amit": 55000,
    "Priya": 48000,
    "Rahul": 65000,
    "Sneha": 45000,
    "Vikas": 75000
}
s = pd.Series(data)
print("Employee Salaries:")
print(s)
print("\nHighest Salary:")
print(s.max())
print("\nLowest Salary:")
print(s.min())
print("\nAverage Salary:")
print(s.mean())
print("\nEmployees earning more than 50000:")
print(s[s > 50000])

#11
import pandas as pd
data = {
    "Laptop": 50000,
    "Mobile": 30000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Monitor": 12000
}
s = pd.Series(data)
print("Products and Prices:")
print(s)
s = s * 1.10
print("\nPrices after 10% increase:")
print(s)
print("\nMost Expensive Product:")
print(s.idxmax(), s.max())

print("\nProducts costing more than 1000:")
print(s[s > 1000])

#12
import pandas as pd
data = {
    101: 65,
    102: 45,
    103: 72,
    104: 58,
    105: 67
}
s = pd.Series(data)
print("Patient Ages:")
print(s)
print("\nAverage Age:")
print(s.mean())
print("\nOldest Patient:")
print(s.idxmax(), s.max())
print("\nYoungest Patient:")
print(s.idxmin(), s.min())
print("\nPatients above 60 years:")
print(s[s > 60])

#13
import pandas as pd
data = {
    "Amit": 85,
    "Priya": 72,
    "Rahul": 95,
    "Sneha": 68,
    "Vikas": 92
}
s = pd.Series(data)
print("Average Attendance:")
print(s.mean())
print("\nStudents with attendance below 75%:")
print(s[s < 75])
print("\nStudents with attendance above 90%:")
print(s[s > 90])
print("\nHighest Attendance:")
print(s.max())

#14
import pandas as pd
df = pd.read_csv(r"C:\Users\patil\OneDrive\Desktop\APC\student.csv")
print("First 5 Records:")
print(df.head())
print("\nLast 5 Records:")
print(df.tail())
df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3
print("\nTotal and Average Marks:")
print(df)
print("\nStudents with Average Greater Than 75:")
print(df[df["Average"] > 75])
print("\nStudent with Highest Average:")
print(df[df["Average"] == df["Average"].max()])
print("\nAverage Marks of Each Subject:")
print(df[["Python", "DBMS", "Maths"]].mean())


#15
import pandas as pd
df = pd.read_csv("employees.csv")
print("--- Employees from CSE Department ---")
print(df[df["Department"] == "CSE"])
print("\n--- Average Salary ---")
print(df["Salary"].mean())
print("\n--- Highest and Lowest Salary ---")
print("Highest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())
print("\n--- Employees with Salary Greater than 50,000 ---")
print(df[df["Salary"] > 50000])
print("\n--- Department-wise Average Salary ---")
print(df.groupby("Department")["Salary"].mean())

#16
import pandas as pd
df = pd.read_csv("patients.csv")
print("--- Patients Above 60 Years ---")
print(df[df["Age"] > 60])
print("\n--- Average Medical Expense ---")
print(df["Medical_Expense"].mean())
print("\n--- Patient with Highest Medical Expense ---")
print(df[df["Medical_Expense"] == df["Medical_Expense"].max()])
print("\n--- Patient Count for Each Disease ---")
print(df["Disease"].value_counts())
print("\n--- Patients with Medical Expense Exceeding 50,000 ---")
print(df[df["Medical_Expense"] > 50000])

#17
import pandas as pd
df = pd.read_csv("weather.csv")
print("--- Maximum Temperature ---")
print(df["Temperature"].max())
print("\n--- Minimum Temperature ---")
print(df["Temperature"].min())
print("\n--- Average Temperature ---")
print(df["Temperature"].mean())
print("\n--- Records with Temperature Above 35°C ---")
print(df[df["Temperature"] > 35])
print("\n--- City-wise Average Temperature ---")
print(df.groupby("City")["Temperature"].mean())