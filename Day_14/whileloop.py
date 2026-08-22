# while loop
'''
i=1
while i<=10:
    print(i)
    i+=1

i=10
while i>0:
    print(i)
    i-=1

i=5
while i<=50:
    print(i)
    i+=5'''

# Strings
'''
s='while loop'
i=0
while i<len(s):
    print(s[i])
    i+=1

s='while loop'
i=len(s)-1
while i>=0:
    print(s[i])
    i-=1

l=list(map(int,input("enter list of items: ").split(',')))
i=0
while i<len(l):
    print(l[i])
    i+=1

n=int(input("enter a number: "))
while n!=0:
    a=n%10
    n=n//10
    print(a)

n=int(input("enter a number: "))
sum=0
while n!=0:
    a=n%10
    n=n//10
    sum+=a
print(sum)

n=int(input("enter a number: "))
product=1
while n!=0:
    a=n%10
    n=n//10
    product*=a
print(product)

n=int(input("enter a number: "))
res=0
while n!=0:
    a=n%10
    n=n//10
    res=res*10+a
print(res)

n=int(input("enter a number: "))
sum=0
while n!=0:
    a=n%10
    n=n//10
    if a%2==0:
        sum+=a
print(sum)


l=list(map(int,input("Enter elemets: ").split(',')))
while 0 in l:
    l.remove(0)
print(l)'''

l=list(map(int,input("Enter elemets: ").split(',')))
start=0
end=len(l)-1
while start <= end:
    if start==end:
        print(l[start])
    else:
        a=l[start]+l[end]
        print(a)
    start+=1
    end-=1








