"""
找出所有水仙花数

Version: 0.1
Author: 骆昊


for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)


from random import randint

money = 1000
while money>0:
    print('Now you have %d', money)
    first_pick = randint(1, 6) + randint(1, 6)
    debt = int(input('Please bet the mount of money '))
    while debt > money:
        debt = int(input('Please bet the less mount of money '))
    if firstfirst_pick == 7 or first_pick == 11:
        print('Win')
        money = money + debt
    elif first_pick == 2 or  first_pick == 3 or first_pick == 12:
        print('lose')
        money = money - debt
        second_pick = randint(1, 6) + randint(1, 6)
    elif second_pick == 7:
        print('Lose')
        money = money - debt
    elif first_pick == second_pick:
        print('Win')
        money = money + first_pick

for i in range(1,10000):
    sum = 0
    for j in range(1,i):
        if i%j == 0:
            sum = j + sum
    if i == sum:
        print(i)      
"""

print(2)
for i in range(3,100):
    flag = 0
    for j in range(2, i- 1):
        if i%j == 0: 
            flag = 1
            break
    if flag == 0:
        print(i)



