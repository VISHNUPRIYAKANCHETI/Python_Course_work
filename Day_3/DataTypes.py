Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=12
>>> type(a)
<class 'int'>
>>> b=12.3
>>> type(b)
<class 'float'>
>>> c=1+2j
>>> type(c)
<class 'complex'>
>>> #sequential data types :- String list tuple
>>> s='codegnan'
>>> id(s)
2452347618544
>>> s+='python'
>>> s
'codegnanpython'
>>> l=[1,2,3,4]
>>> type(l)
<class 'list'>
>>> t=(1,2,3,'v')
>>> type(t)
<class 'tuple'>
>>> s={1,2,3,4,60,4}
>>> type(s)
<class 'set'>
>>> a={1,'vis',22.5}
>>> type(a)
<class 'set'>
>>> d={'productname':'abc','price':23,'stock':True}
>>> d
{'productname': 'abc', 'price': 23, 'stock': True}
>>> typr(d)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    typr(d)
NameError: name 'typr' is not defined. Did you mean: 'type'?
>>> type(d)
<class 'dict'>
>>> s=frozenset({1,1,1,116,18})
>>> s
frozenset({1, 18, 116})
>>> a=True
>>> b=False
>>> type(a)
<class 'bool'>
s=None
type(s)
<class 'NoneType'>
