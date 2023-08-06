from src.decou import DFRM
import inspect

def decorators():
    '''
        Returns a dictionary of the decorators 
        in DFRM.
    '''
    return DFRM["decorators"] 

def decoratees():
    ''' 
        Returns a dictionary of the decoratees 
        in DFRM.
    ''' 
    return DFRM["decoratees"] 

def has_decorators(_target_):
    '''
        Checks if a target class or method 
        has at least one decorator.
    '''
    if hasattr(_target_, "___decou___"): 
        return True
    else: 
        return False

def decorator_chain(_target_): 
    '''
    '''
    if has_decorators(_target_): 
        return _target_.___decou___.deco_chain
    else:   
        raise Exception(f"Target [{target}] has no decorators")

def get_methods(_class_): 
    members = dir(_class_)
    methods = []
    for member in members: 
        member_value = getattr(_class_, member)
        if inspect.isroutine(member_value):
            methods.append(member_value)
    return methods 

def get_subclasses(_class_):
    members = dir(_class_)
    subclasses = []
    for member in subclasses: 
        member_value = getattr(_class_, member)
        if inspect.isclass(member_value):
            methods.append(member_value)
    return subclasses 

def decorated_methods(_class_): 
    methods = get_methods(_class_) 
    _methods = [] 
    for method in methods: 
        if has_decorators(method): 
            _methods.append(method)
    return _methods

def decorated_classes(_class_): 
    classes = get_classes(_class_) 
    _classes = [] 
    for method in classes: 
        if has_decorators(method): 
            _classes.append(method)
    return _classes

def has_decorator(_class_, _decorator_):
    return _decorator_.decorator.__class__ in decorator_chain(_class_).as_map()

def decorator_args(_class_, _decorator_): 
    return decorator_chain(_class_).as_map()[_decorator_.decorator.__class__]

