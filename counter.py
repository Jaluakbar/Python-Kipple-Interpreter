from functools import wraps

def function_used_counter(f):
    @wraps(f)
    def inner(*args, **kwargs):
        inner.counter+=1
        return f(*args,**kwargs)
    inner.counter = 0
    return inner