# List Comprehension
'''
# print 1-10
l=[i for i in range(1,11)]
print(l)

# print even numbers
l=[i for i in range(2,11,2)]
print(l)

# print factors of a number
n=12
f=[i for i in range(1,n+1) if n%i==0]
print(f)

#print only even numbers and print 0 in odd palces
x=[1,2,3,4,5,6,7,8,9,10]
y=[i if i%2==0 else 0 for i in x]
print(y)

#l=[[1,2,3],[1,2,3],[1,2,3]]
#normal method
li=[]
for i in range(3):
    temp=[]
    for j in range(1,4):
        temp.append(j)
    li.append(temp)
print(li)

# By using List Comprehension

l=[[j for j in range(1,4)]for i in range(3)]
print(l)'''

#set of numbers 1-10
s={i for i in range(1,11)}
print(s)

d={i:i*i for i in range(1,11)}
print(d)
