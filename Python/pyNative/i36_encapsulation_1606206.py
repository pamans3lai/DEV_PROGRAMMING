class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit {amount}. Saldo akhir: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance += amount
            print(f"Penarikan {amount}. Saldo akhir: {self.__balance}")
        else:
            print("Saldo tidaK  cukup")

    def get_balance(self):
        return self.__balance

#penggunaan

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(2000)
print(f"Saldo akhir: {acc.get_balance()}")

