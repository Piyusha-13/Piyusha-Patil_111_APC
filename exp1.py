Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l1=[10,20]
l1.append(30)
print(l1)
[10, 20, 30]
l1[2]
30
t1=(10,20,30)
t1[2]
30
s1={10,20,30,40}
s1[3]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s1[3]
TypeError: 'set' object is not subscriptable
print(s1)
{40, 10, 20, 30}
dict={"1":"abc","2":"cdg","3":3}
print(dict)
{'1': 'abc', '2': 'cdg', '3': 3}
dict[1]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    dict[1]
KeyError: 1
>>> dict["1"]
'abc'
>>> dict["4"]=123
>>> dict
{'1': 'abc', '2': 'cdg', '3': 3, '4': 123}
>>> dict(keys)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    dict(keys)
NameError: name 'keys' is not defined
>>> print(dict(key))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(dict(key))
NameError: name 'key' is not defined
>>> print(dict(keys))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(dict(keys))
NameError: name 'keys' is not defined
>>> dict.keys()
dict_keys(['1', '2', '3', '4'])
>>> dict.values()
dict_values(['abc', 'cdg', 3, 123])
>>> l1=[10,20,30,40]
>>> l1.insert(4,50)
>>> print(l1)
[10, 20, 30, 40, 50]
>>> l1.extend(60,70)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    l1.extend(60,70)
TypeError: list.extend() takes exactly one argument (2 given)
>>> l2=[10,20,30,40]
>>> print(l1)
[10, 20, 30, 40, 50]
>>> print(l2)
[10, 20, 30, 40]
>>> l1.extend(l2)
>>> l1
[10, 20, 30, 40, 50, 10, 20, 30, 40]
>>> l1.pop()
40
>>> l1.remove(20)
>>> l1
[10, 30, 40, 50, 10, 20, 30]

