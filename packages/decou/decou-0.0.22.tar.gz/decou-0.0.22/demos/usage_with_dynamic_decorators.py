'''
    This script demonstrates how to use 
    Decou to decorate class or routine 
    decorators dynamically. 
'''
from src.decou import _decorator, init_wrapper, dfrm
import inspect
import pprint

pp = pprint.PrettyPrinter(depth=4)

@_decorator(target="any")
class dynamic_decorator:
    def init(wrapper, *args, **kwargs): 
        print("@ dynamic_decorator.init():", wrapper, args, kwargs) 
        return wrapper, args, kwargs 
    
    def inner(wrapper, target, *args, **kwargs):
        print("@ dynamic_decorator.inner()") 
        print("\t@ - wrapper:", wrapper)
        print("\t@ - target:", target)
        print("\t@ - args: ", args)
        print("\t@ - kwargs: ", kwargs)

        if inspect.isroutine(target): 
            return wrapper.if_routine(target, *args, **kwargs)
        if inspect.isclass(target): 
            return wrapper.if_class(target, *args, **kwargs)
    
    def if_routine(wrapper, target, *args, **kwargs):
        print("@ dynamic_decorator.if_routine()")
        print("\t@ - wrapper:", wrapper)
        print("\t@ - target:", target)
        print("\t@ - args: ", args)
        print("\t@ - kwargs: ", kwargs)       
        return target(*args, **kwargs)
        
    def if_class(wrapper, target, *args, **kwargs):
        print("@ dynamic_decorator.if_class()")
        target.foo = f"{target} : 'bar'"
        return target

print("------- CLASS, METHOD, AND FUNCTION DEFINITIONS -------")

# FUNCTIONS # 
@dynamic_decorator 
def function_wrappee(): 
    print("Hello, World! - from function_wrappee()")

# CLASSES # 
@dynamic_decorator("Hello")
class ClassWrappee: 

    @dynamic_decorator 
    def method_wrappee(self): 
        print("Hello, World! - from .method_wrapee()")


print("\n")

print("------- GENERAL CALLS AND ACCESS -------")

print("@ ===> Calling function_wrappee()")
function_wrappee()
print("\n")

print("@ ===> Printing ClassWrapee.foo")
print(ClassWrappee.foo)
print("\n")

print("@ ===> Calling class_wrapee.method_wrappee()")
class_wrappee = ClassWrappee() 
class_wrappee.method_wrappee()
print("\n")

