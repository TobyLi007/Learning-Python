from functools import wraps
from time import time

def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__ } uses: {time()- start} seconds')
        return result
    return wrapper

def record(output):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            output(func.__name__, time() - start)
            return result
        return wrapper
    return decorator

class Record():
    def __init__(self, output):
        self.output = output
    
    def __call__(self, func):
        @wraps
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            self.output(func.__name__, time() - start)
            return result
        return wrapper

