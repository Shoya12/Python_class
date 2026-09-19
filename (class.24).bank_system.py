class BankSystem:
    def __init__(self,name,initial_amount):
        self.name=name 
        self.__initial_amount=initial_amount

    def deposit(self,amount):
        self.__initial_amount=self.__initial_amount+amount 
        print(f'Your {amount} was deposited succesfully')

    def withdraw(self,amount):
        if self.__initial_amount >= amount:
            self.__initial_amount=self.__initial_amount-amount
            print(f'Your {amount} was withdrawn succesfully')
        else:
            print('Insufficient funds')

    def show_details(self):
        print(f'The Total amount in your account is: {self.__initial_amount}')

account1=BankSystem('Ram Bahadur',1000)

print('Welcome to the Nabil Bank')

while True:
 print('1.Deposit \n 2.Withdraw \n 3.Show Details \n 4.Exit')
 choice=int(input('Enter your choice:'))
 match choice:
    case 1 :
        amount=float(input('Enter the amount to deposit:'))
        account1.deposit(amount)
    case 2:
        amount=float(input('Enter the amount to withdraw:'))
        account1.withdraw(amount)
    case 3:
        account1.show_details()
    case 4:
        print('Thank you for using Nabil Bank')

 stay=str(input('Do you want to continue? (y/n):'))
 if stay.upper()=='Y':
     continue
 else:
      break

