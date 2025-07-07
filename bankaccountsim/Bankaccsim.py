class account:
    def __init__(self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no
    
    def debit(self,debited):
        print(f"Amount debited from your account: ₹{debited}")
        self.balance-=debited
        print(f"Your remaining balance: ₹{self.balance}\n")

    def credit(self,credited):
        print(f"Amount credited to your account: ₹{credited}")
        self.balance+=credited
        print(f"Your remaining balance: ₹{self.balance}\n")

    def print_bal(self):
        print(f"Balance : ₹{self.balance}\n")

acc = account(100000,3256890)
acc.print_bal()
acc.debit(2000)
acc.credit(20000)
