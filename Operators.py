Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
b=3
print(a+b)
13
print(a-b)
7
print(a*b)
30
print(a/b)
3.3333333333333335
print(a//b)
3
print(a%b)
1
a=10
b=5
print(a>b)
True
print(a<b)
False
print(a==b)
False
print(a!=b)
True
x=10
x+=5
print(x)
15
x-=5
print(x)
10
x*=5
print(x)
50
x/=5
print(x)
10.0
x%=5
print(x)
0.0
x//=5
print(x)
0.0
x**=5
print(x)
0.0
x&=5
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    x&=5
TypeError: unsupported operand type(s) for &=: 'float' and 'int'
a=10
b=5
print(a > b and b > 2)
print(a < b or b > 2)
print(not(a < b))
SyntaxError: multiple statements found while compiling a single statement
a = 10
b = 5

print(a > b and b > 2)
SyntaxError: multiple statements found while compiling a single statement
a=10
b=5
print(a>b and b>2 )
True
print(a < b or b > 2)
True
>>> print(not(a < b))
True
>>> list1 = [10, 20, 30]
>>> print(20 in list1)
True
>>> print(40 not in list1)
True
>>> a = [1, 2]
... b = a
... c = [1, 2]
SyntaxError: multiple statements found while compiling a single statement
>>> a = [1, 2]
>>> b = a
>>> c = [1, 2]
>>> print(a is b)
True
>>> print(a is c)
False
>>> a=10
>>> b=5
>>> print(a==b)
False
>>> print(a!=b)
True
>>> print(a > b)
True
>>> print(a < b)
False
>>> print(a >= b)
True
>>> print(a <= b)
False
>>> a=5
>>> b=3
>>> print(a & b)
1
>>> print(a | b)
7
>>> print(a ^ b)
6
>>> print(~a)
-6
>>> print(a << 1)
10
>>> print(a >> 1)
2
