# print 10-1 numbers using recursion
'''
def display(n):
    if n==11:
        return
    display(n+1)
    print(n)
display(1)

# Reverse a string 

def display(s,n):
    if n==len(s):
        return
    display(s,n+1)
    print(s[n],end=" ")
    
display("codegnan",0)

def display(s,ind,w):
    if len(s)-w+1==ind:
        return
    print(s[ind:ind+w])
    display(s,ind+1,w)
s=input()
w=int(input())
display(s,0,w)

# Sum of elements in a list

def display(l,n):
    sum=0
    if n==len(l):
        return 0
    return l[n] + display(l,n+1)
l=list(map(int,input("enter a list of elements: ").split()))
print(display(l,0))

# Sum of the digits in a number

def display(d):
    if d==0:
        return 0
    return d%10 + display(d//10)
d=int(input())
print(display(d))

def fact(n):
    if n==0:
        return 1 
    return n * fact(n-1)
n=int(input())
print(fact(n))

# printing fibonacci series range upto 20
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)
for i in range(20):
    print(fib(i)) '''

  