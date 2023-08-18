#Banking app

class Bank:
    def __init__(self, initial_amount = 0.00):
        self.balance = initial_amount
        
    def transaction(self, transaction_string):
        with open("transactions.txt", "a") as file:
            file.write(f"{transaction_string} \n")
        
    def withdrawal(self, withdraw_amount):
        try:
            withdraw_amount = float(withdraw_amount)
        except ValueError:
            withdraw_amount = 0
        if withdraw_amount:
            self.balance = self.balance - withdraw_amount
            self.transaction(f"withdrew {withdraw_amount}")
        # return self.balance
    
    def Deposit(self, amount):
        try:
            amount = float(amount)
        except:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.transaction(f"Deposited {amount}")
        return self.balance

account = Bank(100.50)
account.withdrawal(30.23)
print(account.balance)


depo = account.Deposit(90.34)
print(depo)





    
    
    