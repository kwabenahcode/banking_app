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
            # return self.balance
account = Bank(100.50)

while True:
    choose_transaction_type = input("What type of transaction do you want to perform? ")
    transaction_types = ["withdrawal", "deposit"]
    if choose_transaction_type in transaction_types:
        if choose_transaction_type == "withdrawal":
            withdraw_amount = input("How much do you want to withdraw? ")
            try:
                withdraw_amount = float(withdraw_amount)
            except ValueError:
                print("Enter a valid number")
            except Exception as e:
                print("uknown")
                print(type(e))
            account.withdrawal(withdraw_amount)
        else:
            deposit_amount = input("How much do you want to deposit? ")
            try:
                deposit_amount = float(deposit_amount)
            except ValueError:
                print("Enter a valid number")
            except Exception as e:
                print("uknown")
                print(type(e))
            account.Deposit(deposit_amount)
        print(f"Your Balance is:  {account.balance}")
                






    
    
    