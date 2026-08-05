Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
================================================= RESTART: C:/Users/vishnu kancheti/OneDrive/Desktop/Python_course_work/Day_2/Day_2.py =================================================
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
35
>>> a=b=c=2
>>> a
2
>>> b
2
>>> c
2
>>> a,b,c=1,2,3
>>> a
1
>>> b
2
>>> c
3
>>> a,b=b,a
>>> 
>>> a
2
>>> b
1
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> b
1
