"""create account class with 2 attributes - balance & acc no. 
create methods for debit,credit,& printing the balace."""

class Account:
    
    def __init__(self , balance , acc):
        self.balance = balance
        self.acc = acc

    def debit(self , amount):
        self.balance -= amount
        print("$",amount,"was debited")
        print("balance = ",self.balance)

    def credit(self , amount):
        self.balance += amount
        print("$",amount,"was credited")
        print("balance = ",self.balance)
        
    def balance(self):
        return self.balance

acc1 = Account(777,1234) 
acc1.debit(34)
acc1.credit(67)


