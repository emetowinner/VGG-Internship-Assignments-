#A command-line Banking Application with the following functionalities:

#Defining the base class and runtime database with linear data structure of max O(n)  
class WinningBank():
    def __init__(self):
        self.email = []
        self.password = []
        self.users = {}
        self.user_acc = {}
        self.counter = 0
        self.banking = True #Ensures the banking process keeps going 
        while self.banking:
            switch = int(input('Welcome Press 1 to USE the system: '))
            if switch == 1:
                Users.user(self)
            else:
                print('Thanks for banking with us!')
                self.banking = False

#Creates and login users
class Users(WinningBank):
    def user(self):
        print('Welcome to Winning Bank PLC, your money is secured with us ')
        switch = int(input('Enter 1 to login 2 to create one: '))
        if switch == 1:
            email = input('Enter your email: ')
            password = input('Enter your password: ')
            ValidateUser.validate_user(self,email,password)
        elif switch == 2:
            user_email = input('Enter your email: ')
            self.email.append(user_email)
            user_password = input('Enter your password: ')
            self.password.append(user_password)
            self.users[self.email[self.counter]] = self.password[self.counter]
            self.user_acc[self.password[self.counter]] = 0
            ValidateUser.validate_user(self,self.email[self.counter],self.password[self.counter])
            self.counter += 1
        else:
            print('Wrong value: ')
            WinningBank.user(self)

#Validates users of the system
class ValidateUser(WinningBank):
    def validate_user(self,email,password):
        print('...........................')
        if email in self.users.keys():
            while self.users[email] != password:
                password = input('Enter your password: ')
            print('Hello!!!')
            switch = int(input('Enter 1 for deposit, 2 withdraw, 3 transfer and 4 for balance: '))
            if switch == 1:
                Deposit.deposit(self)
            elif switch == 2:
                email = input('Enter email: ')
                Withdraw.withdraw(self,email)
            elif switch == 3:
                email = input('Enter your email: ')
                Transfer.transfer(self,email)
            elif switch == 4:
                Balance.get_balance(self)
            else:
                print('Please choose acorrect value')
                ValidateUser.validate_user(self)
        else:
            print("User don't exist")
            Users.user(self)

#Make withdrawals for the users
class Withdraw(WinningBank):
    def withdraw(self,email):
        if email in self.users.keys():
            password = self.users[email]
            if password in self.user_acc.keys():
                amount = float(input('Enter amount to withdraw: '))
                if (self.user_acc[password] <= 0 or amount > self.user_acc[password]):
                    print('Insuficient fund: #',self.user_acc[password])
                    switch = int(input('Enter 1 to deposit 2 cancel'))
                    if switch == 1:
                        Deposit.deposit(self,amount)
                else:                   
                    self.user_acc[password] -= amount    
                    print('Your new balance is: ',self.user_acc[password])    
        return Users.user(self)

#Makes deposits for the users
class Deposit(WinningBank):
    def deposit(self):
        email = input('Enter your email: ')
        if email in self.users.keys():
            password = self.users[email]
            if password in self.user_acc.keys():
                amount = float(input('Enter amount to deposit: '))
                self.user_acc[password] += amount
            print('New Balance is: #',self.user_acc[password])
        else:
            print("Account doesn't exist")
            Users.user(self)

#Makes transfer of funds for the user
class Transfer(WinningBank):
    def transfer(self,email):
        benefciary = input("Enter beneficiary's email: ")
        if benefciary in self.users.keys():
            amount = float(input('Enter amount: '))
            password = self.users[benefciary]
            self.user_acc[password] += amount
            user = self.users[email]
            self.user_acc[user] -= amount
            print(email,' transfered ',amount,' to ',benefciary)
            print(' ')
            print(benefciary,' new balance is: ',self.user_acc[password],'\nYours is: ',self.user_acc[user])
        else:
            print("Account doesn't exist! ")
            Users.user(self)

#Retrives users account balance
class Balance(WinningBank):
    def get_balance(self):
        password = input('Enter your password: ')
        if password in self.user_acc.keys():
            print(self.user_acc[password])

#Runs the code only from the script. Note: script won't run if imported.
if __name__ == '__main__':
    bank = WinningBank()
else:
    print("Can't import script because is not a module, kindly execute the code from the script.")