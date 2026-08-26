# Syntax
'''
def functionname(arguments):
    #statements
functionname(parameters)


def gst(price):
    print("Original price:",price)
    print("Final price:",price+(price*0.18))
gst(100)
gst(500)
gst(1000)
gst(200)
gst(10000)

o/p:-
---
Original price: 100
Final price: 118.0
Original price: 500
Final price: 590.0
Original price: 1000
Final price: 1180.0
Original price: 200
Final price: 236.0
Original price: 10000
Final price: 11800.0


# Print Tables from 1 to 20
 --------------------------

def table(n):
    print(f'{n}-Table')
    print("--------------")
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')
for i in range(1,20):
    table(i)


# Leap Year

def isleap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "Leap Year"
    else:
        return "Not a Leap Year"
print(isleap(2022))
print(isleap(2024))
print(isleap(2026))

o/p:-
---
Not a Leap Year
Leap Year
Not a Leap Year


def isprime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return "Not a Prime"
    return "Prime"
print(isprime(2))
print(isprime(3))
print(isprime(4))
print(isprime(11))

o/p:-
---
Prime
Prime
Not a Prime
Prime


#Positional Arguments :- A positional argument is an argument passed to a function where the value is assigned to a parameter based on its position or order.
#--------------------

def display(name,email,pswd):
    print("name:",name)
    print("email:",email)
    print("password:",pswd)
display("vishnu","vishnu@gmail.com",'vishnu@22')
display("vishnu@gmail.com","vishnu@22",'vishnu')
display('vishnu@22','vishnu',"vishnu@gmail.com")

o/p:-
---
name: vishnu
email: vishnu@gmail.com
password: vishnu@22
name: vishnu@gmail.com
email: vishnu@22
password: vishnu
name: vishnu@22
email: vishnu
password: vishnu@gmail.com


#Keyword Arguments :- A keyword argument is an argument passed to a function by explicitly specifying the parameter name along with its value.
#-----------------

def display(name,email,pswd):
    print("name:",name)
    print("email:",email)
    print("password:",pswd)
display(name="vishnu",email="vishnu@gmail.com",pswd='vishnu@22')
display(email="vishnu@gmail.com",pswd="vishnu@22",name='vishnu')
display(pswd='vishnu@22',name='vishnu',email="vishnu@gmail.com")

o/p:-
---
name: vishnu
email: vishnu@gmail.com
password: vishnu@22
name: vishnu
email: vishnu@gmail.com
password: vishnu@22
name: vishnu
email: vishnu@gmail.com
password: vishnu@22


#Default Arguments :-A parameter with a predefined value that is used when no argument is passed.
#-----------------

def display(name,email,pswd=None):
    print("name:",name)
    print("email:",email)
    print("password:",pswd)
display("vishnu","vishnu@gmail.com")
display("vishnu","vishnu@gmail.com",'vishnu@22')

o/p:-
---
name: vishnu
email: vishnu@gmail.com
password: None
name: vishnu
email: vishnu@gmail.com
password: vishnu@22


#Variable Arguments :-Variable arguments mean a function can accept any number of arguments without knowing in advance how many values will be passed.
#------------------
--->*args — Variable Positional Argument -->Results in "Tuple"
--->**args --> Results in dictionary
--->It allows us to pass multiple positional arguments to a function.

def display(*names):
    print(names)
display("Vishnu")
display("Vishnu","Lakshmi")
display("Vishnu","Lakshmi","Sadhana")
display("Vishnu","Lakshmi","Sadhana","siva")

o/p:-
---
'Vishnu',)
('Vishnu', 'Lakshmi')
('Vishnu', 'Lakshmi', 'Sadhana')
('Vishnu', 'Lakshmi', 'Sadhana', 'siva')


def display(**names):
    print(names)
display(n1="Vishnu")
display(n1="Vishnu",n2="Lakshmi")
display(n1="Vishnu",n2="Lakshmi",n3="Sadhana")
display(n1="Vishnu",n2="Lakshmi",n3="Sadhana",n4="siva")

o/p:-
---
{'n1': 'Vishnu'}
{'n1': 'Vishnu', 'n2': 'Lakshmi'}
{'n1': 'Vishnu', 'n2': 'Lakshmi', 'n3': 'Sadhana'}
{'n1': 'Vishnu', 'n2': 'Lakshmi', 'n3': 'Sadhana', 'n4': 'siva'}
'''