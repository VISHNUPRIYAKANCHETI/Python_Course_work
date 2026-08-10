Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# String Operation
# 1)String Concatination
# 2)Repeatetion
# 3)Indexing
# 4)Slicing
# 5)Membership

#String
a='Codegnan'
a
'Codegnan'
a='Python'
b='Programming'
a+b
'PythonProgramming'
type(a)
<class 'str'>
# 1) String Concatination:-
a='Python'
b='Programming'
a+b
SyntaxError: multiple statements found while compiling a single statement
a='Python'
b='Programming'
a+b
'PythonProgramming'
fname='vishnu'
lname='priya'
fname+lname
'vishnupriya'
# String Repeatition:-
'a'*10
'aaaaaaaaaa'
'-codegnan-'*10
'-codegnan--codegnan--codegnan--codegnan--codegnan--codegnan--codegnan--codegnan--codegnan--codegnan-'
# Indexing :- accessing particular element or character
s='codegnan'
s[0]
'c'
s[-1]
'n'
s[[4]

s[4]
  
SyntaxError: '[' was never closed
s[4]
  
'g'
# String Slicing:- Accessing group of characters or elements
  
names='lakshmi vishnupriya sadhana'
  
names[:]
  
'lakshmi vishnupriya sadhana'
names[:7]
  
'lakshmi'
names[8:19]
  
'vishnupriya'
names[20:27]
  
'sadhana'
names[0:]
  
'lakshmi vishnupriya sadhana'
names[-1:]
  
'a'
names[-1::]
  
'a'
names=[-1::-1]
  
SyntaxError: invalid syntax
names[-1:-1]
  
''
names[::-1]
  
'anahdas ayirpunhsiv imhskal'
# membership:-in not in
  
'a' in names
  
True
'vishnupriya' not in names
  
False
'z' not in names
  
True
names[-1:-8]
  
''
names[-1:-8:-1]
  
'anahdas'
# functions
  
len(names)
  
27
ord('a')
  
97
ord('A')p
  
SyntaxError: invalid syntax
ord('A')
  
65
chr(10)
  
'\n'
chr(100)
  
'd'
max(names)
  
'y'
min(names)
  
' '
sorted(names)
  
[' ', ' ', 'a', 'a', 'a', 'a', 'a', 'd', 'h', 'h', 'h', 'i', 'i', 'i', 'k', 'l', 'm', 'n', 'n', 'p', 'r', 's', 's', 's', 'u', 'v', 'y']

# Case Conversion Methods
  
s="Python Programming language"
  
s.upper()
  
'PYTHON PROGRAMMING LANGUAGE'
s.lower()
  
'python programming language'
s.title()
  
'Python Programming Language'
s.swapcase()
  
'pYTHON pROGRAMMING LANGUAGE'
s.capitalize()
  
'Python programming language'
"Víßhñú".casefold()
  
'vísshñú'
# Alignment Methods:-
  
s.center(50,'-')
  
'-----------Python Programming language------------'
s.center(20,'*')
  
'Python Programming language'
s.center(30,'*')
  
'*Python Programming language**'
s.ljust(50,'-')
  
'Python Programming language-----------------------'
s.rjust
  
<built-in method rjust of str object at 0x00000285C2A11FC0>
s.rjust(50,'-')
  
'-----------------------Python Programming language'
'23'.zfill(4)
  
'0023'
'123456'.zfill(2)
  
'123456'
'8'.zfill(4)
  
'0008'
# Searching Methods
  
s.find('p')
  
-1
s='python programming language'
  
s.find('p')
  
0
s.rfind('p)
...         
SyntaxError: unterminated string literal (detected at line 1)
>>> s.rfind('p')
...         
7
>>> s.index('p')
...         
0
>>> s.rindex('p')
...         
7
>>> s.index('z')
...         
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> s.find('z')
...         
-1
>>> s.count('a')
...         
3
>>> s.count('p')
...         
2
>>> s.replace('p','1')
...         
'1ython 1rogramming language'
>>> s.replace('m','2')
...         
'python progra22ing language'
>>> s.maketrans('aeiou','#$@*&')
...         
{97: 35, 101: 36, 105: 64, 111: 42, 117: 38}
>>> s.translate(s.maketrans('aeiou','#$@*&'))
...         
'pyth*n pr*gr#mm@ng l#ng&#g$'
>>> text="Hello"
...         
>>> text.encode()
...         
b'Hello'
>>> b'Hello'.decode()
...         
'Hello'
