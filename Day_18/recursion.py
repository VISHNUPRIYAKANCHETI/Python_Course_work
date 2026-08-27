#syntax
'''
def fun():
    if base condition:
        return
    fun(updated)
fun(parameters)

def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
display(1)'''

def display(n,m):
    if m==len(n):
        return
    print(n[m])
    display(n,m+1)
display("Python",0)




