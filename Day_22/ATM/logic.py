data={
    123456:{'name':'Vishnupriya','pin':1234,'balance':50000,'history':[]},
    234561:{'name':'Lakshmi','pin':1234,'balance':10000,'history':[]},
    345612:{'name':'Baji','pin':1234,'balance':5000,'history':[]}
}

def login():
    global acc_num
    acc_num=int(input("Enter the Account Number: "))
    pin=int(input("Enter the pin: "))
    if acc_num in data and data[acc_num]['pin']==pin:
        print("Login successfull")
        return True
    else:
        print("Invalid login")

def menu():
    print(f"Welcome to the ATM,{data[acc_num]['name']}")
    print("[C]heck balance")
    print("[D]eposit")
    print("[W]ithdraw")
    print("[V]iew Transaction")
    print("[E]xit")

def checkbalance():
    print(f"Hello {data[acc_num]['name']},")
    print("Current Balance:",data[acc_num]['balance'],end='\n\n')

def deposit():
    amount=int(input("Enter deposit amount: "))
    data[acc_num]['balance']+=amount
    data[acc_num]['history'].append(f"{amount} is deposited")
    print(f"{amount} is deposited successfully")
    checkbalance()

def withdraw():
    amount=int(input("Enter withdraw amount: "))
    if data[acc_num]['balance']>=amount:
        data[acc_num]['balance']-=amount
        data[acc_num]['history'].append(f"{amount} is withdraw")
        print(f"{amount} is withdraw successfully")
        checkbalance()

def viewtransaction():
    if data[acc_num]['history']:
        print("======= Transaction History =======")
        for i in data[acc_num]['history']:
            print(i)
        else:
            print("======= End of the History =======")
    else:
        print("No Transaction History")

    