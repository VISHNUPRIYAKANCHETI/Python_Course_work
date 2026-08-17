"""
username,password=input("Enter username and password: ").split()
if username=="admin" and password=="admin123":
    print("Login Successful")
else:
    print("Invalid Credentials")

product=['laptop','mouse','bag']
search=input("Enter product: ")
if search in product:
    print(f'{search} found')
else:
    print(f'{search} not found')"""

bill=int(input("Enter bill: "))
if bill>99:
    print("Final bill:",bill)
else:
    print("Final bill+ del_char:",bill+30)