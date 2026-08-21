# Factors of a given number
'''
n=int(input("Enter the number: "))
res=[]
for i in range(1,n+1):
    if n%i==0:
        res.append(i)
print(f'Factors of {n} = {res}')

s=input("Enter a string: ")
d={}
for ch in s:
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1
print(d)'''

s=input("Enter a string: ")
count=1
res=''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        res+=s[i]+str(count)
        count=1
print(res+s[i]+str(count))
