"""
import random

def generate_code(code_len =  4):
    a = ''
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(code_len):
        a =  a + all_chars[random.randint(0, len(all_chars))- 1]
    return a 

print (generate_code(100))

def getfilename_suffix(filename, has_dott=False ):
    pos = filename.rfind('.') #last pos of where it was found
    if 0 < pos < len(filename) - 1:
        pos = pos if has_dott else pos +1
        return filename[pos:]
    else:s
        return ''




def find_the_1and2(list):
    list.sort()
    if len(list) > 2:
        max, max2 = list[len(list)-1], list[len(list) - 2]
        print(max,max2)
        return max, max2


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
def output_countdaysin365():
    days = 0
    flag = 1
    list = []
   
    print('Please input date', end = '\n')
    list.append(int(input()))
    print('Please input month', end = '\n')
    list.append(int(input()))
    print('Please input year', end = '\n')
    list.append(int(input()))
    if len(list) == 3:
        print('The %d day, %d month, %d year will be converted into days', list[0], list[1], list[2])
        flag = 0
    else:
        print('Please input again, wrong format input')
        list.clear()
        flag = 1

    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ][is_leap_year(list[2])]
    for index in range(list[1]-1):
        days += days_of_month[[index][is_leap_year(list[2])]]
    print(days)
    return days

output_countdaysin365()
"""

def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num #init
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()
if __name__ == '__main__':
    main()

    