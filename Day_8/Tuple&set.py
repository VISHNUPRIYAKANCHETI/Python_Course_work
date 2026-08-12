Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Tuple
t=()
t=tuple()
t=(1,2,3,4)
t
(1, 2, 3, 4)
t=(1)
t
1
t=(1,)
t
(1,)
t=(1,1,1,1)
t
(1, 1, 1, 1)
t=(1,2.3,"Str",[1,2,3],(1,2,3),{1,2,3},True)
t
(1, 2.3, 'Str', [1, 2, 3], (1, 2, 3), {1, 2, 3}, True)
# immutable
# Ordered
# allows duplicates
# fixed size
# Heterogenous
t=(1, 2.3, 'Str', [1, 2, 3], (1, 2, 3), {1, 2, 3},{1:1,2:2,3:3},True)
t
(1, 2.3, 'Str', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}, True)
type(t)
<class 'tuple'>
# tuple operations
(1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
(1,2,3)*4
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
t
(1, 2.3, 'Str', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}, True)
t[1]
2.3
t[-1]
True
t[5]
{1, 2, 3}
t[:]
(1, 2.3, 'Str', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}, True)
t[::-1]
(True, {1: 1, 2: 2, 3: 3}, {1, 2, 3}, (1, 2, 3), [1, 2, 3], 'Str', 2.3, 1)
t[-1:-3:-1]
(True, {1: 1, 2: 2, 3: 3})
t[3:7]
([1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3})
True in t
True
False in t
False
True not in t
False
2.3 in t
True
1 in t
True
2 not in t
True
2 in t
False
t=(1,2,3,45,54,56,678,9999)
t
(1, 2, 3, 45, 54, 56, 678, 9999)
sorted(t)
[1, 2, 3, 45, 54, 56, 678, 9999]
len(t)
8
max(t)
9999
min(t)
1
count(t)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    count(t)
NameError: name 'count' is not defined. Did you mean: 'round'?
t.count(2)
1
t.index(678)
6
all(1,2,3)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    all(1,2,3)
TypeError: all() takes exactly one argument (3 given)
all((1,2,3))
True
all((1,2,3),1,00,0)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    all((1,2,3),1,00,0)
TypeError: all() takes exactly one argument (4 given)
all((1,2,(1,2,32),00,0)

  all((1,2,00,0))
    
SyntaxError: '(' was never closed
all((1,2,3,00,0))
    
False
any((1,2,3,00,0))
    
True
t=(1,2,3)
    
t
    
(1, 2, 3)
a,b,c=t
    
a
    
1
b
    
2
c
    
3
# The above represents packing and unpacking
    
t=(1,2,3,[1,2,3],5)
    
t
    
(1, 2, 3, [1, 2, 3], 5)
t[4]
    
5
t[3]
    
[1, 2, 3]
t[3].append(4)
    
t
    
(1, 2, 3, [1, 2, 3, 4], 5)
t=(12,13,14)
    
sum(t)
    
39
# mutable unordered unique heterogenous
    
# it does not allows mutable elements in a set -->Those are list,set,dict
    
s={}
    
s
    
{}
type(s)
    
<class 'dict'>
s=set()
    
type(s)
    
<class 'set'>
s={1,2,3,4,54,65,76,231,12234,123456,6}
    
s
    
{123456, 1, 2, 3, 4, 65, 6, 231, 12234, 76, 54}
s={1,1,1,1}
    
s
    
{1}
s=set()
    
s.add(1)
    
s.add(23.4)
    
s.add('str')
    
s.add(True)
    
s.add((1,2,3))
    
s.add([1,2,3])
    
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
s.add({1,2,3})
    
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    s.add({1,2,3})
TypeError: unhashable type: 'set'
s.add({1:2,2:3,3:1})
    
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    s.add({1:2,2:3,3:1})
TypeError: unhashable type: 'dict'
s
    
{1, 'str', (1, 2, 3), 23.4}
s.add(False)
    
s
    
{False, 1, (1, 2, 3), 23.4, 'str'}
s.add(True)
    
s
    
{False, 1, (1, 2, 3), 23.4, 'str'}
# set operations
    
# union intersection difference symmetric-difference subset superset disjoint
    
a={1,2,3,4,5}
    
b={3,5,7,8,9}
    
# union
    
a | b
    
{1, 2, 3, 4, 5, 7, 8, 9}
# membership
    
1 in a
    
True
3 in b
    
True
1 in b
    
False
# intersection
    
a & b
    
{3, 5}
# difference
    
a-b
    
{1, 2, 4}
b-a
    
{8, 9, 7}
# symmetric difference
    
a ^ b
    
{1, 2, 4, 7, 8, 9}
b ^ a
    
{1, 2, 4, 7, 8, 9}
# subset
    
{1,2}<=a
    
True
{3,10}<=a
    
False
{3,10}<= b
    
False
{3,8}<=b
    
True
# superset
    
a>=
    
SyntaxError: invalid syntax
a>={1,2}
    
True
b>={1,2}
    
False

m={1,2,3}
    
n={4,5,6}
    
m.isdisjoint(n)
    
True
n.isdisjoint(m)
    
True
a.isdisjoint(b)
    
False
a
    
{1, 2, 3, 4, 5}
a={1,2,3,45,54,56}
    
a
    
{1, 2, 3, 54, 56, 45}
sorted(a)
    
[1, 2, 3, 45, 54, 56]
max(a)
    
56
min(a)
    
1
len(a)
    
6
a.index(a)
    
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    a.index(a)
AttributeError: 'set' object has no attribute 'index'
a.count(1)
    
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    a.count(1)
AttributeError: 'set' object has no attribute 'count'
any({1,2,3,0})
    
True
any({0,False})
    
False
all({'str',0,00})
    
False
all({'str',1,True})
    
True
sum(a)
    
161
a
    
{1, 2, 3, 54, 56, 45}
a={1,2,3}
    
b=a
    
a
    
{1, 2, 3}
b
    
{1, 2, 3}
c=a.copy(5)
    
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    c=a.copy(5)
TypeError: set.copy() takes no arguments (1 given)
c=a.copy()
    
c
    
{1, 2, 3}
c.add(4)
    
c
    
{1, 2, 3, 4}
a
    
{1, 2, 3}
s=set()
    
a={1,2,3,4}
    
a
    
{1, 2, 3, 4}
a.add(5)
    
a
    
{1, 2, 3, 4, 5}
a.add(100)
    
a
    
{1, 2, 3, 4, 5, 100}
a.add(101)
    
a
    
{1, 2, 3, 4, 5, 100, 101}
a.add({10,20,30,40})
    
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    a.add({10,20,30,40})
TypeError: unhashable type: 'set'
a.update({10,20,30,40})
    
a
    
{1, 2, 3, 4, 5, 100, 101, 40, 10, 20, 30}
a.pop(2)
    
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    a.pop(2)
TypeError: set.pop() takes no arguments (1 given)
>>> a.pop()
...     
1
>>> a.pop()
...     
2
>>> a.pop()
...     
3
>>> a.remove(2)
...     
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    a.remove(2)
KeyError: 2
>>> a.remove(10)
...     
>>> a
...     
{4, 5, 100, 101, 40, 20, 30}
>>> a.remove(10)
...     
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    a.remove(10)
KeyError: 10
>>> a.discard(10)
...     
>>> a
...     
{4, 5, 100, 101, 40, 20, 30}
>>> # discard doen not provides error if we enter already delete element
...     
>>> a.clear()
...     
>>> a
...     
set()
>>> a=frozenset({1,2,3,4})
...     
>>> a
...     
frozenset({1, 2, 3, 4})
