from abc import ABC, abstractmethod 

class Bank(ABC):
    @abstractmethod
    def deposit(self,amount):
        pass 

    @abstractmethod 
    def withdraw(self,amount):
        pass

    @abstractmethod
    def show_detail(self):
        pass 


class SavingAccount(Bank):
     def __init__(self,name,initial_amount):
            self.name=name 
            self.__initial_amount=initial_amount
    
     def deposit(self,amount):
            self.__initial_amount=self.__initial_amount+amount 
            print(f'Your {amount} was deposited succesfully')
    
     def withdraw(self,amount):
            if amount >= self.__initial_amount+5000:
               print('Insufficient funds')
                    
            else:
                self.__inital_amount-=amount 
                print(f'{amount} was deducted from your account')
    
     def show_details(self):
            print(f'The Total amount in your account is: {self.__initial_amount}')
    
class CurrentAccount(Bank):
    def __init__(self,name,initial_amount):
            self.name=name 
            self.__initial_amount=initial_amount
    
    def deposit(self,amount):
            self.__initial_amount=self.__initial_amount+amount 
            print(f'Your {amount} was deposited succesfully')
    
    def withdraw(self,amount):
            if amount <= self.__initial_amount:
                self.__initial_amount=self.__initial_amount-amount
                print(f'Your {amount} was withdrawn succesfully')
            else:
                print('Insufficient funds')
    
    def show_details(self):
            print(f'The Total amount in your account is: {self.__initial_amount}')

print('1.Saving Account \n 2.Current Account')
acc_type=int(input('Enter your choice'))
if acc_type==1:
      account=SavingAccount('Ram',10000)
elif acc_type==2:
      account=CurrentAccount('Techdint',10000)
else:
      print('Pls choose from 1 to 2 ')
      print ('Welcome to nabil bank')
      while True:
        print("1. Deposite\n2. Withdraw\n3. Show Details\n4. Exit")
    
        choice=int(input("Enter any Number form 1 to 4:"))

        match choice:
            case 1:
                amount=float(input("Enter the depositing amount"))
                account.deposite(amount)

            case 2:
                amount=float(input("Enter the withdrawing amount"))
                account.withdraw(amount)

            case 3:
                account.show_details()

            case 4:
                print("Thank you for using Nabil bank")
                break   
