'''#1] Write a PYTHON program that reads a value of n and check the number is zero or non zero value.

a=int(input("Enter number="))
if a==0:
    print("Number is zero")
else:
    print("Number is nonzero")

#Write a PYTHON program to find a largest of two numbers.

a=int(input("Enter number1="))
b=int(input("Enter number2="))
if a>b:
    print(a,"is largest")
else:
    print(b,"is largest")

#Write a PYTHON program that reads the number and check the no is positive or negative.
a=int(input("Enter number1="))
if a==0:
    print("Number is zero")
elif a>0:
    print("Number is positive")
else:
    print("Number is negative")

#Write a PYTHON program to check entered character is vowel or consonant.

a=(input("Enter string="))
if 'a'or'e'or'i'or'o'or'u':
    print("Entered character is vowel")
else:
    print("Consonant")
    
#Write a PYTHON program to evaluate the student performance
      #If % is >=80 then  Very Good performance
      #If % is >=70 then Good performance
      #If % is >=60 then average performance
      #else Poor performance.

a=int(input("Enter marks="))
if a>=80:
    print("Very good performance")
elif a>=70:
    print("Good performance")
elif a>=60:
    print("Average performance")
else:
    print("Poor performance")

#Write a PYTHON program to find largest of three numbers.
a=int(input("Enter number1="))
b=int(input("Enter number2="))
c=int(input("Enter number3="))
if a>b:
    print(a,"is greater")
elif b>c:
    print(b,"is greater")
else:
    print(c,"is greater")

#Write a PYTHON program to find smallest of three numbers
a=int(input("Enter number1="))
b=int(input("Enter number2="))
c=int(input("Enter number3="))
if a<b:
    print(a,"is smallest")
elif b<c:
    print(b,"is smallest")
else:
    print(c,"is smallest")

#Write a PYTHON program to check weather number is even or odd.
a=int(input("Enter number="))
if a%2==0:
    print(a,"is even")
else:
    print(a,"is odd")

#Write a PYTHON program to check a year for leap year.

a=int(input("Enter year="))
if a%4==0:
    print(a,"is leap year")
else:
    print(a,"is not leap year")'''

#A company insures its drivers in the following cases:- If the driver is married.- If the driver is unmarried, male and above 30 yearsof age.
#- If the driver is unmarried, female and above 25 years of age.
#In all the other cases, the driver is not insured.
#Write a PYTHON program to determine whether the driver is insured or not

m = input("Married? (yes/no): ")
g = input("Gender (male/female): ")
a = int(input("Age: "))

if m == "yes":
    print("Driver is insured")
elif g == "male" and a > 30:
    print("Driver is insured")
elif g == "female" and a > 25:
    print("Driver is insured")
else:
    print("Driver is not insured")

    
    

    


















    


