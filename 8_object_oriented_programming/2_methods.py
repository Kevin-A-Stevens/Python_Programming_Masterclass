"""
Methods

Creating a static method

The _ in _current_time makes it clear this method is not meant
to be used outside the class
"""
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
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdrawal(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                trans_type = "deposited"
            else:
                trans_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, trans_type, date, date.astimezone()))


if __name__ == "__main__":
    kevin = Account("Kevin", 0)
    kevin.show_balance()

    kevin.deposit(1000)
    kevin.withdrawal(500)

    kevin.withdrawal(2000)

    kevin.show_transactions()

    steph = Account("Steph", 800)
    steph.deposit(100)
    steph.withdrawal(200)
    steph.show_transactions()
    print(steph.__dict__)




