'''
n=int(input())
for i in range(n):
    for j in range(n):
        print('*',end=" ")
    print()
    

n=int(input())
for i in range(n):
    for j in range(n):
        if j%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()

n=int(input())
for i in range(n):
    for j in range(n):
        print(j%2,end=" ")
    print()

n=int(input())
for i in range(n):
    for j in range(n):
        print(i%2,end=" ")
    print()

n=int(input())
for i in range(n):
    for j in range(n):
            print((i+j)%2,end=" ")
    print()

n=int(input())
for i in range(n):
    for j in range(n):
        print(i+j,end=" ")
    print()

n=int(input())
c=1
for i in range(n):
    for j in range(n):
        print(c,end=" ")
        c+=1
    print()

n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

n=int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()

n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()'''

'''
n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print('',end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(n-i-1):
        print("*",end=" ")
    print()'''


'''n=int(input())
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n-i):
        print("*",end=" ")
    print()


n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for k in range(n-i-1):
        print(" ",end=" ")
    print()
for i in range(n):
    for j in range(n-i-1):
        print("*",end=" ")
    for k in range(i+1):
        print(" ",end=" ")
    print()

    
n=int(input())
m=n//2
for i in range(n):
    if i<=m:
        for j in range(i+1):
            print("*",end=" ")
    else:
        for k in range(n-i):
            print("*",end=" ")
    print() 

n=int(input())
m=n//2
for i in range(n):
    if i<=m:
        print("* "*(i+1),end=" ")
    else:
        print("* "*(n-i),end=" ")
    print()'''

n=int(input())
m=n//2
for i in range(n):
    if i<=m:
        print(" "*(m-i),"*"*(i+1),end=" ",sep="")
    else:
        print(" "*(i-m),"*"*(n-i),end=" ",sep="")
    print()