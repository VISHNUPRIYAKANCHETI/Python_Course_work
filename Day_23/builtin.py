"""
import sys
print(sys.argv)           # print(sys.argv[-1])
print(sys.version)
print(sys.path)
print("Start")
sys.exit()
print("End")

import platform

print(platform.system())
print(platform.release())
print(platform.processor())

import math

print(math.pi)
print(math.e)
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))
print(math.factorial(5))
print(math.gcd(8,12))
print(math.sqrt(36))
print(math.pow(2,2))

import math

print(round(12.0000001))
print(round(12.3333))
print(round(12.666666))
print(round(12.99999))

print(math.ceil(12.00000001))
print(math.ceil(12.3333))
print(math.ceil(12.666666))
print(math.ceil(12.99999999))

print(math.floor(12.00000001))
print(math.floor(12.3333))
print(math.floor(12.666666))
print(math.floor(12.99999999))

import random

random.seed(9)                              # constant output   (without seed it gives different outputs)

print(random.random())
print(random.randint(100000,9999999))
print(random.uniform(1,6))                 #float values

l=['r','p','s']
print(random.choice(l))

lang=['python','java','css','sql','Flask']
print(random.choices(lang,k=2))

random.shuffle(lang)
print(lang)

from collections import Counter
s="python programming"
res=Counter(s)
print(res)

from collections import Counter,defaultdict

products=['sugar','salt','mils']
res=defaultdict(list)

for i in products:
    res[i].append(['des','rev','com'])
print(res)

from collections import Counter,defaultdict
s="Python Programming"

d=defaultdict(int)
for i in s:
    d[i]+=1
print(d)

from collections import deque

l=deque([])
l.append(10)
l.append(20)
l.append(30)
l.popleft()
l.popleft()
l.append(40)
l.popleft()
l.append(50)
print(l)

o/p:- deque([40, 50])


from collections import deque

l=deque([])
l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.pop()
l.pop()
l.appendleft(40)
l.pop()
l.appendleft(50)
print(l)

o/p:- deque([50, 40])"""



