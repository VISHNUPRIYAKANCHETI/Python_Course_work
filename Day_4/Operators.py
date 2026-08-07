Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Python Operators
'''
1)Arithmetic
2)Comparision
3)Assignment
4)Relational
5)Membership
6)Identity
7)Bitwise
'''
'\n1)Arithmetic\n2)Comparision\n3)Assignment\n4)Relational\n5)Membership\n6)Identity\n7)Bitwise\n'
# Assignment Operator
a=10
b=2
a+b
12
a-b
8
a*b
20
a/b
5.0
a//b
5
a%b
0
a**b
100
a**3
1000
2**3
8
# Comparision Operator
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True
# Assignment Operator
a=10
a+=10
a
20
a-=10
a
10
a*=10
a
100
a/=10
a
10.0
a//=10
a
1.0
a%=10
a
1.0
a=10
a%=10
a
0
a=2
a**=2
a
4
# Relational Operators
email=True
password=False
email and password
False
login=False
display_products=True
login or display_products
True
3%2==0 and 7%2==0
False
6%2==0 or 3%2==0
True
3%2==0
False
not 3%2==0
True
3%2!=0
True
# Membership Operators
# str, list, tuple, set, dictionary
s='python programming'
'python' in s
True
'a' in s
True
'z' in s
False
'java' in s
False
l=[1,2,3,4]
'a' in l
False
1 in l
True
1 not in l
False
t=(1,2,'a',4)
'a' not in t
False
1 in t
True
5 in t
False
set={1,2,3,4,'v'}
'a' in s
True
'a' in set
False
'v' in set
True
'v' not in set
False
data={'Name':'vishnu','batch':65,'course':'pfs'}
'name' in data
False
'Name' in data
True
65 in data
False
'pfs' not in data
True
>>> 'age' in data
False
>>> # Identity Operation
>>> l=[1,2,3,4]
>>> m=[1,2,3,4]
>>> id
<built-in function id>
>>> id(l)
2068520733248
>>> id(m)
2068520339712
>>> l==m
True
>>> l is m
False
>>> n=m
>>> n
[1, 2, 3, 4]
>>> n==m
True
>>> id(n)
2068520339712
>>> id(m)
2068520339712
>>> n is m
True
>>> m is n
True
>>> n is l
False
>>> n is not l
True
>>> # Bitwise Operator
>>> 11 & 12
8
>>> 11 | 12
15
>>> 11 ^ 12
7
>>> 2<<3
16
>>> 16>>2
4
>>> ~23
-24
