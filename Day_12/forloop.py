# str list tuple set dict range
'''s='python programming'
for i in s:
    print(i)


l=[1,2,3,4,5.6]
for num in l:
    print(num)

prices=(234,4567,7890,12345)
for price in prices:
    print(price)

names={'vishnu','lakshmi','sadhana'}
for name in names:
    print(name)

d={1:1,2:4,3:9,4:16}
for i in d:
    print(i,":",d[i])'''

# range :- Used to generate numeric values
# Syntax:- range(start,end+1,step)

'''for i in range(1,11):
    print(i)

for i in range(2,21,2):
    print(i)

for i in range(5,101,5):
    print(i)

for i in range(5,0,-1):
    print(i)

for i in range(19,0,-2):
    print(i)

s='python programming language'
for i in range(len(s)):
    print(i,":",s[i])'''

# range is used for --->str,list,tuple 

# Enumerate -->it's going to give the sequence number and the result should be in tuple

'''s="python programming"
for i in enumerate(s):
    print(i)

s="python programming"
for i in enumerate(s):
    print(i[0],i[1])

l=[123,345,678,910]
for i in enumerate(l):
    print(i[0],i[1])

d={1:1,2:4,3:9,4:16}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])'''

# Break is used to termiante the execution until the condition is satisfied.
# Continue is used to skip a particular condition iteration and continue till the final execution.

'''for i in range(1,11):
    if i==5:
        break
    print(i)

for i in range(1,11):
    if i==5:
        continue
    print(i)'''

# for else :-

'''l=[1,2,3,4,5,6]
n=5
for i in l:
    if l==5:
        print(n,"Found")
        break
else:
    print(n,"Not found")

l=[1,2,3,4,5,6]
n=5
for i in l:
    if l==n:
        print(n,"Found")
else:
    print(n,"Not found")

pin=1234
for i in range(5):
    epin=int(input("Enter the pin: "))
    if epin==pin:
        print("Unlock phone")
        break
    else:
        print("Invalid pin")
else:
    print("Try after 30 seconds")'''

#Prime number
'''num=int(input("Enter a number: "))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")'''

# Another logic for prime number

num=int(input("Enter a number: "))
for i in range(2,num//2+1):
    if num%i==0:
        print(num,"Not a prime number")
        break
else:
    print("prime number")