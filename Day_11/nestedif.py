fa=eval(input("Follows Account: "))
cf=eval(input("Close Friend: "))
if fa:
    if cf:
        print("Story is Visible")
    else:
        print("Not in Close Friends List")
else:
    print("First Flollow the Account")

reg=eval(input("Registered: "))
fee=eval(input("Fee Paid: "))
if reg:
    if fee:
        print("Tournament Entry Confirmed")
    else:
        print("Entry Fee Pending")
else:
    print("Registration Required")

link=eval(input("Link Active: "))
Permission=eval(input("Permission Granted: "))
if link:
    if Permission:
        print("File Opened Successfully")
    else:
        print("Access Denied")
else:
    print("Invalid File Link")


data={
    "vishnu":{'status':True,'python':95,'mysql':98,'flask':99},
    "Lakshmi":{'status':True,'python':85,'mysql':88,'flask':89},
    "Sivanjali":{'status':True,'python':35,'mysql':38,'flask':39},
    "Baji":{'status':False,'python':None,'mysql':None,'flask':None},
    "Sadhana":{'status':True,'python':55,'mysql':58,'flask':59},
}
name=input("Enter the name: ")
if name in data:
    if data[name]['status']:
        sum=data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg=sum/3
        print(f'{name}!!!')
        print(f"your avg score is {avg}")
        if avg>90:
            print("Outstanding Performace")
        elif avg>80:
            print("Very Good")
        elif avg>50:
            print("Good, Better luck next time")
        else:
            print("You fails the exam, try hard")
    else:
        print("you didn't attempt the exam, bring your parents")

else:
    print(f'{name} not found in data')