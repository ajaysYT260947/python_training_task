class InsufficientFundsError(Exception):
    pass


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")
        self.balance -= amount
        print(f"Withdrawn: {amount}")

    def show(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")


account = Account("Arun", 1000)

try:
    account.deposit(500)
    account.withdraw(2000)
except InsufficientFundsError as e:
    print("Error:", e)
finally:
    print("Transaction finished")

account.show()


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, min_balance=500):
        super().__init__(owner, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise InsufficientFundsError("Withdrawal would reduce balance below minimum balance")
        self.balance -= amount
        print(f"Withdrawn: {amount}")

# Test
priya = SavingsAccount("Priya", 1500)

try:
    priya.withdraw(1200)
except InsufficientFundsError as e:
    print("Error:", e)

try:
    priya.withdraw(800)
except InsufficientFundsError as e:
    print("Error:", e)

print("isinstance(priya, Account):", isinstance(priya, Account))      