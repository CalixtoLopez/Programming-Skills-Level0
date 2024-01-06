"""
1. Create an online banking system with the following features:

* Users must be able to log in with a username and password.(TODO)
* If the user enters the wrong credentials three times, the system must lock them out.(TODO)
* The initial balance in the bank account is $2000. (TODO)
* The system must allow users to deposit, withdraw, view, and transfer money.
* The system must display a menu for users to perform transactions.2. 
"""

print("-"*100)
print("Register User:")
print("-"*100)
username = input("Your name: ")
password = input("Password: ")

print("-"*100)
print("Login User:")
count=1
total_deposit = 2000
movements = []
while(True):
    username_login = input("Your name: ")
    password_login = input("Password: ")
    if(username == username_login and password == password_login):
        while(True):
            print("Select operation:")
            print("Initial balance:", total_deposit)
            print("(1) Add deposit")
            print("(2) Withdraw")
            print("(3) Show")
            print("(4) Transfer money")
            print("(5) Show movements:")

            select = int(input("SELECT MENU(1)(2)(3)(4)(5):  "))
            print('*'*100)
            if(select == 1):
                depositAdd = int(input("Add deposit:"))
                total_deposit= total_deposit + depositAdd
                movements.append("Add deposit:"+ str(total_deposit))
                print("Total deposit:",total_deposit)
                print('*'*100)

            if (select == 2):
                withdraw = int(input("Withdraw:"))
                total_deposit = total_deposit - withdraw
                movements.append("withdraw:"+ str(total_deposit))
                print("Total deposit:",total_deposit)
            if(select == 3):
                show = total_deposit
                movements.append("Show"+ str(show))
                print("Total deposit:",total_deposit)
            if(select==4):
                transfer_money = int(input("Transfer money:"))
                total_deposit =  transfer_money + total_deposit
                movements.append("Transfer money:"+ str(total_deposit))
                print("Total deposit:",transfer_money)
            if(select ==5):
                print("Total deposit:",movements)
    else:
        if(count == 3):
            print("Your account is blocked 3-3")
            break
        else:
            print("False name or password",count, "- 3")
            count = count + 1
    print("-"*100)
