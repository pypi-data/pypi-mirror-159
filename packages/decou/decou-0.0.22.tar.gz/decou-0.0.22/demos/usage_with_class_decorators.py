'''
    This script demonstrates how to use 
    Decou to decorate class decorators. 
'''
from src.decou import _decorator, init_wrapper 

@_decorator(target="class")
class flexible_class_decorator:
    def init(wrapper, *args, **kwargs): 
        print("@ flexible_class_decorator.init():", wrapper, args, kwargs) 
        return wrapper, args, kwargs 
    
    def inner(wrapper, target, *args, **kwargs):
        print("@ flexible_class_decorator.inner()", wrapper, args, kwargs) 
        target.foo = f"{target} : 'bar'"
        return target

print("------- CLASS DEFINITIONS -------")

@flexible_class_decorator
class WrappeeA: 
    def __init__(self):
        pass

@flexible_class_decorator(1234, foo="bar")  
class WrappeeB: 
    def __init__(self):
        pass

print("------- CLASS ACCESS -------")

print(WrappeeA.foo)
print(WrappeeB.foo)