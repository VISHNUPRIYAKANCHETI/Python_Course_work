Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#stripping and trimming method
s='     hello     world       '
s.strip()
'hello     world'
s.lstrip()
'hello     world       '
s.rstrip()
'     hello     world'
s.replace(' ','')
'helloworld'

s='java-python-c-c++-mysql-flask'
s.split('-')
['java', 'python', 'c', 'c++', 'mysql', 'flask']
s.split('')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s.split('')
ValueError: empty separator
s.split('-',2)
['java', 'python', 'c-c++-mysql-flask']
s.rsplit('-',2)
['java-python-c-c++', 'mysql', 'flask']
s.lsplit('-',3)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s.lsplit('-',3)
AttributeError: 'str' object has no attribute 'lsplit'. Did you mean: 'rsplit'?
l='''python'''
l='''python
mysql
java
flask
'''
l
'python\nmysql\njava\nflask\n'
l.splitlines()
['python', 'mysql', 'java', 'flask']
c=['python', 'mysql', 'java', 'flask']
c
['python', 'mysql', 'java', 'flask']
''.join(c)
'pythonmysqljavaflask'
' '.join.(c)
SyntaxError: invalid syntax
' '.join(c)
'python mysql java flask'
'-'.join(c)
'python-mysql-java-flask'
'-'.join(('1','2',','3'))
          
SyntaxError: unterminated string literal (detected at line 1)
'-'.join(('1','2',',','3'))
          
'1-2-,-3'
'-'.join({'1','2',',','3'})
          
',-3-2-1'
a='strings.py'
          
a.partition('.')
          
('strings', '.', 'py')
a='string.py.java.png.txt'
          
a
          
'string.py.java.png.txt'
a.partition('.')
          
('string', '.', 'py.java.png.txt')
a.rpartition('.')
          
('string.py.java.png', '.', 'txt')
a.rpartition('-')
          
('', '', 'string.py.java.png.txt')
('', '', 'string.py.java.png.txt')
          
('', '', 'string.py.java.png.txt')

# String testing methods
          
a='strings.png'
          
a.startswith('str')
          
True
a.startswith('')
          
True
a.startswith(' ')
          
False
a.endswith('png')
          
True
a.endswith('')
          
True
a.endswith(' ')
          
False
'python123'.islower()
          
True
'123python'.islower()
          
True
'PYthon'.islower()
          
False
'PYTHON123'isupper()
          
SyntaxError: invalid syntax
'PYTHON123'.isupper()
          
True
'PYThoN123'isupper()
          
SyntaxError: invalid syntax
'PYThoN123'.isupper()
          
False
'12@python'.isalpha()
          
False
'PYTHon'.isalpha()
          
True
'123python@'.isalnum()
          
False
>>> '123python'.isalnum()
...           
True
>>> 'Python Programming'.istitle()
...           
True
>>> 'python Program'.istitle()
...           
False
>>> '     '.isspace()
...           
True
>>> ''.isspace()
...           
False
>>> 'my_var'.isidentifier()
...           
True
>>> 'MY_Var'.isidentifier()
...           
True
>>> 'my@var'.identifier()
...           
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    'my@var'.identifier()
AttributeError: 'str' object has no attribute 'identifier'. Did you mean: 'isidentifier'?
>>> 'my@var'.isidentifier()
...           
False
>>> '123455'.isdecimal()
...           
True
>>> '123455'.isdigit()
...           
True
>>> 'ERTYTRE124'.isdigit()
...           
False
>>> 'RTYTRE1245'.isdecimal()
...           
False
>>> '12343'.isnumeric()
...           
True
