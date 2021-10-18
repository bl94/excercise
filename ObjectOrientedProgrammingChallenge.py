class Account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    
    def __str__(self) :
        return f"Account owner: {self.owner} \nAccount balance : ${self.balance}"

    def deposit(self,amount_deposit):
        self.balance+=amount_deposit
        print(f"Deposit ${amount_deposit} Accepted")
    def withdraw(self,amount_of_withdrawal):
        if amount_of_withdrawal>self.balance:
            print("Funds Unavalaible")
        else:
            self.balance-=amount_of_withdrawal
            print(f"Withdrawal ${amount_of_withdrawal} Accepted")

def main():
    acct1=Account("Jose",100)
    print(acct1)
    print(acct1.owner)
    print(acct1.balance)
    acct1.deposit(50)
    print(acct1.balance)
    acct1.deposit(50)
    acct1.withdraw(200)
    print(acct1.balance)
    acct1.withdraw(50)
    
main()