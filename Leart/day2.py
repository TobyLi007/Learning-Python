"""
a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'complex'>
print(type(d)) # <class 'str'>
print(type(e)) # <class 'bool'>


a = int(input('a = ')) #typecasting
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))
"""

f= float(input("Please enter f = "))
c = (f-32)/1.8
print('C value is % f' %c)