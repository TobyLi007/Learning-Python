from time import sleep
def countdown(n):
    while n>0:
        yield n
        n -= 1

# Fibonacci数生成器
def fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


# 偶数生成器
def even(gen):
    for val in gen:
        if val % 2 == 0:
            yield val


def main():
    gen = even(fib())
    for _ in range(10):
        print(next(gen))


##def main():
##    for num in countdown(5):
##        print(f'Countdown: {num}' )
##        sleep(1)
##    print('Countdown Over!')

if __name__ == '__main__':
    main()