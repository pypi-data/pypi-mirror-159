'''
    This script demonstrates how to use
    Decou to decorate function decorators.
'''
from src.decou import _decorator, init_wrapper

@_decorator(target="routine")
class flexible_routine_decorator: 
    def init(wrapper, *args, **kwargs): 
        print("@ flexible_routine_decorator.init():", wrapper, args, kwargs)
        return wrapper, args, kwargs

    def inner(wrapper, target, *args, **kwargs):
        print("@ flexible_routine_decorator.inner(): ", wrapper, target, args, kwargs)
        return target(*args, **kwargs)
        

print("------- FUNCTION DEFINITIONS -------")

# No Arguments # 
@flexible_routine_decorator 
def wrappee_a(): 
    print("Hello, World! - from wrappee_a()")

# With Arguments # 
@flexible_routine_decorator(1234, foo="bar")
def wrappee_b(): 
    print("Hello, World! - from wrappee_b()")

print("------- FUNCTION CALLS -------")

wrappee_a() 
wrappee_b()