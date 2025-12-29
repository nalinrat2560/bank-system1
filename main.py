class Account:
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"ฝากเงิน {amount} บาท สำเร็จ")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"ถอนเงิน {amount} บาท สำเร็จ")
        else:
            print("ยอดเงินไม่พอ")

class SavingsAccount(Account):
    def __init__(self, owner_name, balance=0, interest_rate=0.03):
        super().__init__(owner_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"ไดรับดอกเบี้ย {interest} บาท")