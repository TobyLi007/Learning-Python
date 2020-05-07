import re

def main():
    print('Hint:用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0 ')
    username = input('Please enter your username: ')
    qq = input('Your QQ number: ')
    m1 = re.match(r'^[0-9a-zA-Z]{6,20}$', username)
    if not m1:
        print('Please enter a valid username! ')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('Please enter a valid QQ number! ')
    if m1 and m2:
        print('Valid info Thanks!')


if __name__ == '__main__':
    main()