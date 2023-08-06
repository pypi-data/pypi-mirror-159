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

@_decorator(target="any")
class wrapper_c: 
    def init(wrapper, *args, **kwargs): 
        return wrapper, args, kwargs 
    
    def inner(wrapper, target, *args, **kwargs): 
        return target(*args, **kwargs)

print("@ Decorators:")
print(dfrm.decorators())
print("@ Decoratees:")
print(dfrm.decoratees())

