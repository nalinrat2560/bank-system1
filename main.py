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