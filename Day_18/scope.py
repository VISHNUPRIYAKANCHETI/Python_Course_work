# Local Variable :- we can declare the variable inside the function
'''def display():
    n=10
    print("Inside function:",n)
display()
print("Outside function:",n)


# Global variable :- we can declare the variable outside the function
def display():
    print("Inside function:",n)
n=10
display()
print("Outside function:",n)

# Global variable makes the local variable global
def display():
    global n
    n=10
    print("Inside function:",n)
display()
print("Outside function:",n)

def display():
    global n
    n+=10
    print("Inside function:",n)
n=10
display()
print("Outside function:",n)

def display():
    course="PFS"
    def update():
        course="JFS"
        print("Inner function:",course)
    update()
    print("Outer function:",course)
display()

def display():
    course="PFS"
    def update():
        nonlocal course
        course="JFS"
        print("Inner function:",course)
    update()
    print("Outer function:",course)
display()

# If we use bulit-in methods as variables it will loose its functionality 
l=[1,2,3,4,5]
print(max(l))

max=10
print(max)

l=[1,2,3,4,5]
print(max(l))

print=10
print(max)'''





