Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=1
type(a)
<class 'int'>
a=1.2
type(a)
<class 'float'>
a="hello"
type(a)
<class 'str'>
a=b'hello'
type(a)
<class 'bytes'>
a=[10,20,30]
type(a)
<class 'list'>
b=(10,20,30)
type(b)
<class 'tuple'>
c={a:"berry",b:"mango",c:30}
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    c={a:"berry",b:"mango",c:30}
NameError: name 'c' is not defined
c={a:"berry",b:"mango",d:30}
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    c={a:"berry",b:"mango",d:30}
NameError: name 'd' is not defined. Did you mean: 'id'?
c={"a":"berry","b":"mango","c":30}
type(c)
<class 'dict'>
c=True
type(c)
<class 'bool'>
c=byte(20)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    c=byte(20)
NameError: name 'byte' is not defined. Did you mean: 'bytes'?
c=bytes(20)
type(c)
<class 'bytes'>
c=memoryview(byes(20))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    c=memoryview(byes(20))
NameError: name 'byes' is not defined. Did you mean: 'bytes'?
d=memoryview(c)
type(d)
<class 'memoryview'>
a=10
b=10
c=a+b
d
<memory at 0x0000020A3F846C80>
a=10
b=10
c=a+b
SyntaxError: multiple statements found while compiling a single statement
a=10
b=10
a+b
20
a=20
b=10
a-b
10
a=10
b=20
a*b
200
a=20
b=2
a/b
10.0
a=10
b=5
a//b
2
a=10
b=5
a%b
0
a=10
b=20
a**b
100000000000000000000
x=10
y=10
x==y
True
x=20
y=30
x<y
True
x=20
y=30
x>y
SyntaxError: multiple statements found while compiling a single statement
x=40
y=10
x>y
True
x=30
y=30
x<=y
True
x=30
y=40
x>=y
False
x=10
y=20
x!=y
True
>>> c=10
>>> d=20
>>> c+=d
>>> c
30
>>> c=50
>>> d=30
>>> c-=d
>>> c
20
>>> c*=d
>>> c
600
>>> c/=d
>>> c
20.0
>>> c%=d
>>> c
20.0
>>> c**=d
>>> c
1.073741824e+39
>>> c//=d
>>> c
3.5791394133333333e+37
>>> a=10
>>> b=20
>>> c=30
>>> if a>b or b>c"
SyntaxError: unterminated string literal (detected at line 1)
>>> a=10
... b=20
... c=30
... if a>b or b>c:
...     
SyntaxError: multiple statements found while compiling a single statement
>>> a=10
... b=20
... if a<b and b>a:
...     
SyntaxError: multiple statements found while compiling a single statement
>>> l1=[10,20,30]
... l1.append(40)
... print(l1)
SyntaxError: multiple statements found while compiling a single statement







