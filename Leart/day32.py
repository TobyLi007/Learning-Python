from time import sleep
import threading 
from concurrent.futures import ThreadPoolExecutor
from random import randint

class Account(object):
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
    def deposit(self, money):
        with self.condition:
            new_balance = money + self.balance
            sleep(0.01)
            self.balance = new_balance
            self.condition.notify_all()

    def withdraw(self, money):
        with self.condition:
            while self.balance < money:
                self.condition.wait()
            new_balance = self.balance - money
            sleep(0.01)
            self.balance = new_balance
def AddMoney(account):
    money = randint(5, 10)
    account.deposit(money)
    print(threading.current_thread().name, 
            ':', money, '====>', account.balance)
    sleep(0.5)
def SubMoney(account):
    money = randint(10, 30)
    account.withdraw(money)
    print(threading.current_thread().name, 
            ':', money, '<====', account.balance)
    sleep(1)

def main():
    account = Account()
    with ThreadPoolExecutor(max_workers= 10) as pool:
        for _ in range(5):
            pool.submit(AddMoney, account)
            pool.submit(SubMoney, account)

    pool.shutdown()
        
if __name__ == '__main__':
    main()