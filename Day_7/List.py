Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list
l=[]
l=list()
type(l)
<class 'list'>
l=[1,2.3,'str',True,[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},1+2j]
l
[1, 2.3, 'str', True, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}, (1+2j)]
l=[1,1,1,1]
l
[1, 1, 1, 1]
# List Operations:-
#concatenation
a=[1,2,3]
b=[4,5,6]
a+b
[1, 2, 3, 4, 5, 6]
a[3]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a[3]
IndexError: list index out of range
a=[1,2,3,5,6,4,7,88,99,123,1444]
a
[1, 2, 3, 5, 6, 4, 7, 88, 99, 123, 1444]
a[5]
4
a[-1]
1444
# Repeatition
a*3
[1, 2, 3, 5, 6, 4, 7, 88, 99, 123, 1444, 1, 2, 3, 5, 6, 4, 7, 88, 99, 123, 1444, 1, 2, 3, 5, 6, 4, 7, 88, 99, 123, 1444]
# indexing
a[-5]
7
# Slicing
a[:]
[1, 2, 3, 5, 6, 4, 7, 88, 99, 123, 1444]
a[::-1]
[1444, 123, 99, 88, 7, 4, 6, 5, 3, 2, 1]
a[1::2]
[2, 5, 4, 88, 123]
a[::2]
[1, 3, 6, 7, 99, 1444]
# Membership opertors
3 in a
True
23 in a
False
23 not in a
True
123 in a
True
123 not in a
False
# list methods:-
a
[1, 2, 3, 5, 6, 4, 7, 88, 99, 123, 1444]
max(a)
1444
min(a)
1
sorted(a)
[1, 2, 3, 4, 5, 6, 7, 88, 99, 123, 1444]
len(a)
11
a
[1, 2, 3, 5, 6, 4, 7, 88, 99, 123, 1444]
id(a)
2279038889024
a[0]
1
a[0]=34
a
[34, 2, 3, 5, 6, 4, 7, 88, 99, 123, 1444]
id(a)
2279038889024
a.append(20)
a
[34, 2, 3, 5, 6, 4, 7, 88, 99, 123, 1444, 20]
a.append(10)
a
[34, 2, 3, 5, 6, 4, 7, 88, 99, 123, 1444, 20, 10]
a.insert(2,12)
a
[34, 2, 12, 3, 5, 6, 4, 7, 88, 99, 123, 1444, 20, 10]
a.insert(-1,100)
a
[34, 2, 12, 3, 5, 6, 4, 7, 88, 99, 123, 1444, 20, 100, 10]
a.insert(-2,200)
a
[34, 2, 12, 3, 5, 6, 4, 7, 88, 99, 123, 1444, 20, 200, 100, 10]
a.insert(0,2343)
a
[2343, 34, 2, 12, 3, 5, 6, 4, 7, 88, 99, 123, 1444, 20, 200, 100, 10]
a.pop(0)
2343
a
[34, 2, 12, 3, 5, 6, 4, 7, 88, 99, 123, 1444, 20, 200, 100, 10]
a.pop(-1)
10
a
[34, 2, 12, 3, 5, 6, 4, 7, 88, 99, 123, 1444, 20, 200, 100]
a.extend([1,2,554])
a
[34, 2, 12, 3, 5, 6, 4, 7, 88, 99, 123, 1444, 20, 200, 100, 1, 2, 554]
a.remove(34)
a
[2, 12, 3, 5, 6, 4, 7, 88, 99, 123, 1444, 20, 200, 100, 1, 2, 554]
del a
a
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a
NameError: name 'a' is not defined
del a[1]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    del a[1]
NameError: name 'a' is not defined
a=[2, 12, 3, 5, 6, 4, 7, 88, 99, 123, 1444, 20, 200, 100, 1, 2, 554]
a
[2, 12, 3, 5, 6, 4, 7, 88, 99, 123, 1444, 20, 200, 100, 1, 2, 554]
a.clear()
a
[]
a=[2, 12, 3, 5, 6, 4, 7, 88, 99, 123, 1444, 20, 200, 100, 1, 2, 554]
del a[0:3]
a
[5, 6, 4, 7, 88, 99, 123, 1444, 20, 200, 100, 1, 2, 554]
a
[5, 6, 4, 7, 88, 99, 123, 1444, 20, 200, 100, 1, 2, 554]
a.index(13)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a.index(13)
ValueError: 13 is not in list
>>> a.index(4)
2
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> a.count(4)
1
>>> a=[1,2,3]

>>> b=a
>>> b
[1, 2, 3]
>>> b.append(7)
>>> b
[1, 2, 3, 7]
>>> a
[1, 2, 3, 7]
>>> c=a.copy()
>>> c.append(12)
>>> a
[1, 2, 3, 7]
>>> b
[1, 2, 3, 7]
>>> c
[1, 2, 3, 7, 12]
>>> any([1,'',False,[],(),{},set()])
True
>>> any([0,'',False,[],(),{},set()])
False
>>> all([1,'',False,[],(),{},set()])
False
>>> a.sorted()
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a.sorted()
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
>>> a.sort()
>>> a
[1, 2, 3, 7]
>>> a.reverse()
>>> a
[7, 3, 2, 1]
>>> sum(a)
13
