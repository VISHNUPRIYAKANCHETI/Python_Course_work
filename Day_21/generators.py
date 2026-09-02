# generator
# yield is used to pause its execution and resumes later
'''
def reels():
    data=["1..100","101..200","201..300","301..400","401..500"]
    for i in data:
        yield i
res=reels()
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))

o/p:-

1..100
101..200
201..300
301..400
401..500

def countdown():
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1
res=countdown()
for i in res:
    print(i)

def fact(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i

res=fact(12)
for i in res:
    print(i)

#Primes

def primes(n):
    for i in range(1,n+1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            yield i

res=primes(100)
for i in res:
    print(i,end=" ")'''
