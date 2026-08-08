Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Input Formatting
# int, float, complex, str, list, tuple, set, dic, bool
a=input()
codegnan
a
'codegnan'
a=input()
2
a
'2'
# integer
marks=int(input("Enetr marks: "))
Enetr marks: 95
marks
95
# Float
price=float(input("Enetr price: "))
Enetr price: 45.5
price
45.5
price=float(input("Enetr price: "))
Enetr price: 2
price
2.0
# List tuple set
names='vishnu lakshmi sadhana'
names.split()
['vishnu', 'lakshmi', 'sadhana']
names='vishnu,lakshmi,sadhana'
names.split(',')
['vishnu', 'lakshmi', 'sadhana']
names=input("Enter names: ").split()
Enter names: vishnu lakshmi sadhana
names
['vishnu', 'lakshmi', 'sadhana']
names=tuple(input("Enter names: ").split())
Enter names: vishnu lakshmi sadhana
names
('vishnu', 'lakshmi', 'sadhana')
names=tuple(input("Enter names: ").split(','))
Enter names: vishnu,lakshmi,sadhana
names
('vishnu', 'lakshmi', 'sadhana')
names=set(input("Enter names: ").split())
Enter names: vishnu lakshmi sadhana
names
{'sadhana', 'lakshmi', 'vishnu'}
names=tuple(input("Enter names: ").split(','))
Enter names: vishnu,lakshmi,sadhana
names
('vishnu', 'lakshmi', 'sadhana')
names=set(input("Enter names: ").split(','))
Enter names: vishnu,lakshmi,sadhana
names
{'sadhana', 'lakshmi', 'vishnu'}
marks=input().split()
12 23 34 45 56 67
marks
['12', '23', '34', '45', '56', '67']
map(int,marks)
<map object at 0x000002308B7D5180>
list(map(int,marks))
[12, 23, 34, 45, 56, 67]
marks=list(map(int,input("Enetr marks: ").split()))
Enetr marks: 12 13 1 42 15
marks
[12, 13, 1, 42, 15]
marks=tuple(map(int,input("Enetr marks: ").split()))
Enetr marks: 1 2 3 4 5
marks
(1, 2, 3, 4, 5)
marks=set(map(int,input("Enetr marks: ").split(',')))
Enetr marks: 1,2,3,4,4
marks
{1, 2, 3, 4}
marks=set(map(float,input("Enetr marks: ").split(',')))
Enetr marks: 1,2,3,4,5
marks
{1.0, 2.0, 3.0, 4.0, 5.0}
marks=set(map(float,input("Enetr marks: ").split(',')))
Enetr marks: 1,2
marks
{1.0, 2.0}
marks=set(map(complex,input("Enter marks: ").split(',')))
Enter marks: 1,2,3,45,56
marks
{(1+0j), (2+0j), (3+0j), (45+0j), (56+0j)}
>>> marks=set(map(str,input("Enter marks: ").split(',')))
Enter marks: 1,2,3,4
>>> marks
{'1', '2', '4', '3'}
>>> marks=set(map(list,input("Enter marks: ").split(',')))
Enter marks: 1,2,3
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    marks=set(map(list,input("Enter marks: ").split(',')))
TypeError: unhashable type: 'list'
>>> marks=set(map(bool,input("Enter marks: ").split(',')))
Enter marks: 1,2,3,0
>>> marks
{True}
>>> marks=set(map(bool,input("Enter marks: ").split(',')))
Enter marks: 0
>>> marks
{True}
>>> a,b=[1,2]
>>> a
1
>>> b
2
>>> a,b,c=(1,12.3,"str")
>>> a
1
>>> b
12.3
>>> c
'str'
>>> email,password=input("Enter email and pass: ").split())
SyntaxError: unmatched ')'
>>> email,password=input("Enter email and pass: ").split()
Enter email and pass: vishnu@gmail.com 1234
>>> email
'vishnu@gmail.com'
>>> password
'1234'
>>> name,marks=input("Enter name and marks: ").split()
Enter name and marks: vishnu 95
>>> name
'vishnu'
>>> marks
'95'
>>> int(marks)
95
>>> a,b,c=list(map(int,input("Enter name and marks: ").split()))
Enter name and marks: 1 2 3
a
1
b
2
c
3
a,b,c=map(int,input("Enter name and marks: ").split())
Enter name and marks: 1 2 3
a
1
b
2
c
3
a,b,c=int(input("Enter name and marks: ").split())
Enter name and marks: 1 2 3
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a,b,c=int(input("Enter name and marks: ").split())
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
a,b,c=int(input("Enter values: "))
Enter values: 1 2 3
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a,b,c=int(input("Enter values: "))
ValueError: invalid literal for int() with base 10: '1 2 3'
# Eval function

status=eval(input())
False
status
False
type(status)
<class 'bool'>
status=input()
False
status
'False'
type(status)
<class 'str'>
status=eval(input())
2.00
status
2.0
type(status)
<class 'float'>
status=eval(input())
1+2j
status
(1+2j)
type(status)
<class 'complex'>
