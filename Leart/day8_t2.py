from math import sqrt

class Point(object):
    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y
        
    def move_by(self, x, y):
        self._x += x
        self._y += y

    def distance_to(self, other):
        return sqrt((self._x - other._x) ** 2 + (self._y - other._y) ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self._x), str(self._y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()