a = float(input('Please enter three length of sides: (enter to record next digit)'))
b = float(input(''))
c = float(input(''))
p = (a + b + c) / 2
if a+b>c and c+b>a and a + c > b:
    print('The perimeter of this triangle is %.2f/n \
        and the size is %.2f' %(a+b+c , (p * (p - a) * (p - b) * (p - c)) ** 0.5))

else:
    print('This three sides can not form a triangle')
