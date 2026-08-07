Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> b=2.3
>>> c='codegnan'
>>> print(a,b,c)
10 2.3 codegnan
>>> print("a=",a,"b=",b,"c=",c)
a= 10 b= 2.3 c= codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='')
a=10b=2.3c=codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='\n')
a=
10
b=
2.3
c=
codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='\t')
a=	10	b=	2.3	c=	codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='\t',end="\n\n")
a=	10	b=	2.3	c=	codegnan

>>> print("a=",a,"b=",b,"c=",c,sep='\t',end='@')
a=	10	b=	2.3	c=	codegnan@
>>> print(f'a={a} b={b} c={c}')
a=10 b=2.3 c=codegnan
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=2.300000 c=codegnan
>>> print('a={} b={} c={}'.format(a,b,c))
a=10 b=2.3 c=codegnan
>>> print('a={} b={} c={}'.format(c,a,b))
a=codegnan b=10 c=2.3
>>> print('a={0} b={1} c={2}'.format(a,b,c))
a=10 b=2.3 c=codegnan
>>> print('a={2} b={0} c={1}'.format(a,b,c))
a=codegnan b=10 c=2.3
