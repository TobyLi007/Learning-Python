def fib(num, temp = {}):
    if num ==1 or num == 2:
        return 1
    try:
        return temp[num]
    except KeyError:
        temp[num] = fib(num -1) +fib(num- 2)
        return temp[num]


print(fib(10))