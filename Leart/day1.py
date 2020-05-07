print ('hello world')


"""
第一个Python程序 - hello, world!
向伟大的Dennis M. Ritchie先生致敬

Version: 0.1
Author: 骆昊
"""

print('hello, world!')
# print("你好,世界！")
print('你好', '世界')
print('hello', 'world', 'Toby', 'is', 'The King', sep=', ', end='!')
print('goodbye, world', end='!\n')

import turtle

turtle.pensize(4)
turtle.pencolor('yellow')

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.mainloop()

