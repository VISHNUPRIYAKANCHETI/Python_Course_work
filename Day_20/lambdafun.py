#Lambda:-It is a anonymous function
# Syntax
"""
var=lambda arg : expression
"""
'''
wish=lambda name:f"Welcome to the course {name}"
print(wish("Vishnu"))

gst=lambda price:price+price*0.18
print(gst(1000))

avg=lambda a,b,c:a+b+c/3
print(avg(10,20,30))

isvowels=lambda a:"Vowel" if a in "aeiouAEIOU" else "Consonant"
print(isvowels("X"))

iseven=lambda n:"Even" if n%2==0 else "Odd"
print(iseven(11))

largest=lambda a,b,c:a if a>b and a>c else b if b>c else c
print(largest(20,37,10))


# Map

l=[1,2,3,4,5,6]
update=list(map(lambda i: i+10,l))
print(update)

t=[100,200,300,400,500,600]
discount=list(map(lambda i:i-i*0.3,t))
print(discount)

# Filter
l=[1,2,3,4,5,6]
update=list(filter(lambda i: i%2!=0,l))
print(update)

t=[100,200,300,400,500,600]
discount=list(filter(lambda i:i>300,t))
print(discount)

l=["vishnu@gmail.com","vishnu@codegnan.com","vishnu@yahoo.com"]
domain=list(map(lambda i:i.split("@")[-1],l))
print(domain)


from functools import reduce
l=[4,2,4,65,75,4000,8]
res=reduce(lambda sum,i:sum+i,l)
print(res)


from functools import reduce
l=[4,2,4,65,75,4000,8]
res=reduce(lambda product,i:product*i,l)
print(res)


seats={'s1':True,
       's2':False,
       's3':False,
       's4':False,
       's5':True}
avail=list(filter(lambda i:seats[i]!=True,seats))
print(avail)

products={'eggs':280,
       'sugar':60,
       'salt':40,
       'butter':80,
       'milk':12}
res=list(filter(lambda i:products[i]>50,products))
print(res)'''

products={'eggs':280,
       'sugar':60,
       'salt':40,
       'butter':80,
       'milk':12}
res=dict(sorted(products.items(),key=lambda i:i[1]))
res=dict(sorted(products.items(),key=lambda i:i[1],reverse=True))
print(res)


