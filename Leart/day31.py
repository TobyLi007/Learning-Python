import time
import threading
from concurrent.futures import ThreadPoolExecutor

class Account(object):
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
    
    def deposit(self, money):
        with self.lock:
            new_balance  = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance

class AddMoneyTread(threading.Thread):
    def __init__(self, account, money):
        self.account = account
        self.money = money
        super().__init__()

    def run(self):
        self.account.deposit(self.money)

def main():
    futures = []
    account = Account()
    pool = ThreadPoolExecutor(max_workers= 100)# totally 10 threads
    for _ in range(10000):
        future = pool.submit(account.deposit ,1)
        futures.append(future)
    pool.shutdown()
    for future in futures:
        future.result()
    print(account.balance)

if __name__ == '__main__':
    main()