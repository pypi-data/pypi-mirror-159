from src.decou import _decorator, dfrm   

@_decorator(target="routine")
class wrapper_a: 
    def init(wrapper, *args, **kwargs): 
        return wrapper, args, kwargs 

    def inner(wrapper, target, *args, **kwargs):
        return target(*args, **kwargs) 

@_decorator(target="class")
class wrapper_b: 
    def init(wrapper, *args, **kwargs): 
        return wrapper, args, kwargs 
    
    def inner(wrapper, target, *args, **kwargs): 
        return target(*args, **kwargs)

@_decorator(target="routine")
class wrapper_c: 
    def init(wrapper, *args, **kwargs): 
        return wrapper, args, kwargs 
    
    def inner(wrapper, target, *args, **kwargs): 
        return target(*args, **kwargs)

@wrapper_a 
def wrappee_a1():
    print("Hello, World! - from wrappee_a1")

@wrapper_a 
def wrappee_a2(): 
    print("Hello, World! - from wrappee_a2") 

@wrapper_b 
class WrappeeA1: 
    def __init__(self):
        pass 

    @wrapper_c
    def wrapper_c1(self): 
        pass 

    @wrapper_c
    def wrapper_c2(self): 
        pass 

@wrapper_b 
class WrappeeA2: 
    def __init__(self):
        pass 

    @wrapper_c
    def wrapper_c3(self):
        pass 

    @wrapper_c
    def wrapper_c4(self):
        pass 

print("@ Decorators")
print(dfrm.decorators())
print("@ Decoratees")
print(dfrm.decoratees())
