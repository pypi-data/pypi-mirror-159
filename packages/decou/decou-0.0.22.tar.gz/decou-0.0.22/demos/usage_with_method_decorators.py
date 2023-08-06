'''
    This script demonstrates how to use 
    Decou to decorate method decorators.
'''
from src.decou import _decorator, init_wrapper 

@_decorator(target="routine") 
class flexible_routine_decorator: 
    def init(wrapper, *args, **kwargs): 
        print("@ flexible_routine_decorator.init():", wrapper, args, kwargs) 
        return wrapper, args, kwargs

    def inner(wrapper, target, *args, **kwargs): 
        print("@ flexible_routine_decorator.inner():")
        print("\t@ - wrapper:", wrapper)
        print("\t@ - target:", target)
        print("\t@ - args: ", args)
        print("\t@ - kwargs: ", kwargs)
        return target(*args, **kwargs)
    

print("------- CLASS AND METHOD DEFINITIONS -------")

class Wrappee: 

    # No Arguments #
    @flexible_routine_decorator 
    def method_wrappee_a(self):
        print("Hello, World! - from .method_wrappee_a()")

    # With Arguments # 
    @flexible_routine_decorator(1234, foo="bar") 
    def method_wrappee_b(self): 
        print("Hello, World! - from .method_wrappee_b()")

print("------- METHOD ACCESS -------")
wrappee = Wrappee() 
wrappee.method_wrappee_a() 
wrappee.method_wrappee_b()