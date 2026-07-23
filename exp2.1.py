'''#create a program to calcute area of triangle
base=int(input("Enter base"))
height=int(input("Enter base"))
a=0.5*base*height
print(a)

#Write a program volume of sphere.
r=int(input("Enter radius"))
v=4/3*3.14*r*r*r
print(v)

#Write a program to find total surface area of cylinder
h=int(input("Enter height="))
r=int(input("Enter radius="))
v=2*3.14*r*(h+r)
print(v)

#area of square
s=int(input("Enter side="))
v=s*s
print(v)

#write a program to convert pounds into kg
pounds = float(input("Enter weight in pounds: "))
kg = pounds * 0.453592
print("Weight in kilograms =", kg)

#kilometre into miles
km= float(input("Enter km: "))
miles=km*0.62137
print(miles)

#write program to calculate factorial of number

n=int(input("Enter number="))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

#check whether number is prime or not

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

#pallindrome or not
num = int(input("Enter a number: "))
rev=0
original_num=rev
while num>0:
    rem=num%10
    rev=rev*10+rev
    num=num//10
if original_num==rev:
    print("Number is pallindrome")
else:
    print("Number is not Pallindrome")

#to convert decimal to binary ,octal,hexadecimal
num = int(input("Enter a decimal number: "))

print("Binary =", bin(num))
print("Octal =", oct(num))
print("Hexadecimal =", hex(num))'''

#calculate factors of numbers.
num = int(input("Enter a number: "))
print("Factors are:")
for i in range(1, num + 1):
    if num % i == 0:

        print(i)

#to find askey values
ch = input("Enter a character: ")
print("ASCII value =", ord(ch))
