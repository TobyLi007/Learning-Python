#Generator method
def fib(max):
    a,b = 0,1
    for _ in range(max):
        a,b = b, a+b
        yield a

for f in fib(6):
    print(f) 
#Iteration method

class Fib(object):
    def __init__(self, max):
        self.index = 0
        self.max = max
        self.a, self.b = 0, 1

    def __iter__(self):
        return self
    def __next__(self):
        if self.index < self.max:
            self.a , self.b = self.b,  self.a + self.b
            self.index +=1
            return self.a
        else:
            raise StopIteration()
for fibs in Fib(8):
    print(fibs)