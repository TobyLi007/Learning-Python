from math import sqrt 
import os


def is_prime(number):
    try:
        assert number>0
    except AssertionError:  
        print("number is invalid.")
    else:
        for num in range(2, int(sqrt(number))+ 1):
            if number% num == 0:
                return False
        return True if number!= 1 else False
def deletion_file(str):
    if os.path.exists(str):
        os.remove(str)
    else:
        print("The file does not exist")

def main():
    filename = ('a.txt', 'b.txt', 'c.txt')
    fs = []
    try:
        for filenames in filename:
            fs.append(open(filenames, 'w', encoding = 'utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs[0].write(str(number) + '\n')
                elif number < 1000:
                    fs[1].write(str(number) + '\n')
                else:
                    fs[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('Error in writing files!')
    finally:
        for f in fs:
            f.close()
    print('Done!')
    flag = input(print('Do you want to delete the files? Y/N?'))
    print(flag)
    if flag == 'Y':
        for i in range(0,3):
            deletion_file(filename[i])
    else:
        print('Files not delete')


if __name__ == '__main__':
    main()