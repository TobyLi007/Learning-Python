
from random import randrange, randint, sample


def display(balls):
   for index, ball in enumerate(balls):
       if index == len(balls) - 1:
           print('|', end = ' ')
       print('%d' %ball, end = ' ')
   print()

def random_select():
    balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1,16))
    return selected_balls

def main():
    n = int(input('Input: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()