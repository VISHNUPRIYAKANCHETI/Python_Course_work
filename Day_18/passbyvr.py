# Pass by value :- A copy of the value is given to the function.
# Pass by reference:- The function gets access to the same object, so changes made to a mutable object can be seen outside.
'''def display(n):
    n+=10
    print("Inner Function:",n)
n=10
display(n)
print("Outer Function:",n)


def display(n):
    n+=10.3
    print("Inner Function:",n)
n=10.3
display(n)
print("Outer Function:",n)

def display(n):
    n+=10
    print("Inner Function:",n)
n=10+3j
display(n)
print("Outer Function:",n)

def display(n):
    n+="Programming"
    print("Inner Function:",n)
n="Python"
display(n)
print("Outer Function:",n)

def display(n):
    n+=(5,6)
    print("Inner Function:",n)
n=(1,2,3,4)
display(n)
print("Outer Function:",n)

def display(n):
    n=True
    print("Inner Function:",n)
n=False
display(n)
print("Outer Function:",n)

def display(n):
    n.append(5)
    print("Inner Function:",n)
n=[1,2,3,4]
display(n)
print("Outer Function:",n)

def display(n):
    n.add(4)
    print("Inner Function:",n)
n={1,2,3}
display(n)
print("Outer Function:",n)'''

def display(n):
    n[5]=6
    print("Inner Function:",n)
n={1:2,3:4}
display(n)
print("Outer Function:",n)


