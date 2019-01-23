import datetime
import pytz


class Account:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(
            Account._current_time(), balance)]
        print("Account created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transaction_list.append((
                Account._current_time(), amount))
            print("Deposited {}.".format(
                amount), end=" ")
            self.show_balance()

    def withdraw(self, amount):
        if 0 <= amount <= self.__balance:
            self.__balance -= amount
            print("Withdrew {}.".format(amount), end=" ")
            self.show_balance()
            self._transaction_list.append((
                Account._current_time(), amount))
        else:
            print("Tried to withdraw {}.".format(amount))
            print(
                "The amount must be no more than your current balance.", end='')
            self.show_balance()

    def show_balance(self):
        print("Balance is {}.".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            elif amount == 0:
                tran_type = "balance"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(
                amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    kevin = Account("Kevin", 0)
    kevin.deposit(16000)
    kevin.withdraw(10491)
    kevin.show_transactions()

    hayek = Account("F. Hayek", 12000)
    hayek.__balance = 66666
    hayek._Account__balance = 55555
    hayek.deposit(1200)
    hayek.withdraw(1000)
    hayek.show_transactions()
    print(hayek.__dict__)
