def main():
    persons = [True] *30
    counter = 0
    key = 9
    while counter < 15:
        for index in range(1, 30 -1 ):
            if (index + 1)% key ==1:
                persons[index] = False
                counter += 1
        key += 1
        for person in persons:
            print('Y' if person else 'N', end=' ')
    for person in persons:
        print('Y' if person else 'N', end = ' ')

def main2():
    persons = [True]*30
    counter, num, index = 0,0,0
    while counter<15:
        if persons[index]:
            num +=1
            if num ==9:
                persons[index] = False
                counter +=1
                num = 0
        index += 1
        index %= 30
    for person in persons:
        print('Y' if person else 'N', end = ' ')





def main1(): 
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('Y' if person else 'N', end=' ')


if __name__ == '__main__':
    main2()
    print()
    main1()
