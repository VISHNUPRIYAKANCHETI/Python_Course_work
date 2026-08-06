Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Type conversions
a=10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
bool(a)
True
list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
f=1.2
int(f)
1
complex(f)
(1.2+0j)
str(f)
'1.2'
bool(f)
True
list(f)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
set(f)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
c=1+2j
int(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
bool(c)
True
str(c)
'(1+2j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
s='codegnan'
i='1234'
int(s)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
int(i)
1234
float(s)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'codegnan'
float(i)
1234.0
bool(s)
True
bool(i)
True
list(s)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
list(i)
['1', '2', '3', '4']
tuple(s)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
tuple(i)
('1', '2', '3', '4')
set(s)
{'o', 'c', 'e', 'g', 'd', 'a', 'n'}
set(i)
{'4', '1', '2', '3'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dict(i)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    dict(i)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
l=[1,2,3,4]
int(l)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
str(l)
'[1, 2, 3, 4]'
bool(l)
True
tuple(l)
(1, 2, 3, 4)
set(l)
{1, 2, 3, 4}
dict(l)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
t=(1,2,3,'v')
int(t)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
str(t)
"(1, 2, 3, 'v')"
bool(t)
True
list(t)
[1, 2, 3, 'v']
set(t)
{1, 2, 3, 'v'}
dict(t)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
s={1,2,'v',4.5'}
   
SyntaxError: unterminated string literal (detected at line 1)
s={1,2,'v',4.5}
   
int(s)
   
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
   
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
complex(s)
   
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
list(s)
...    
[1, 2, 'v', 4.5]
>>> tuple(s)
...    
(1, 2, 'v', 4.5)
>>> dict(s)
...    
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> d={1:1,2:2,3:3}
...    
>>> int(d)
...    
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
>>> float(d)
...    
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
>>> complex(d)
...    
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'dict'
>>> str(d)
...    
'{1: 1, 2: 2, 3: 3}'
>>> bool(d)
...    
True
>>> list(d)
...    
[1, 2, 3]
>>> tuple(d)
...    
(1, 2, 3)
>>> set(d)
...    
{1, 2, 3}
