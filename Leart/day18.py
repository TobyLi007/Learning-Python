# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
for x in range(20):
    for y in range(33):
        z = 100- x- y
        if 5*x + 3*y + z//3 == 100 and z%3 == 0:
            print(x,y,z)
# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼

fish = 6
while True:
    total_fish = fish
    flag_enough = False
    for _ in range(5):
        if (total_fish -1)//5 == 0:
            flag_enough = True
            total_fish = 4*(total_fish - 1) //5
        else:
            flag_enough = False
            total_fish += 5
            break
    if flag_enough == True:
        print(total_fish)
        break


