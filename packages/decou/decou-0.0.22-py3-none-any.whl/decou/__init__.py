import inspect 
import functools

ENABLE_LOGGING = False

DECOU_SCOPE = "___decou___"

DFRM = {
    "decorators": {
        "any": {}, 
        "class": {}, 
        "routine": {}
    },
    "decoratees": {
        "any": {}, 
        "class": {},
        "routine": {}
    } 
}

def log_print(*args, **kwargs):
    ''' 
        Helper function for conditional log printing.
        Behind the scenes, conditionally calls print(...) based 
        on the global constant ENABLE LOGGING.    
    '''
    if ENABLE_LOGGING:
        print(*args, **kwargs)


def validate_target(target, wrapper, decoratee):
    '''
        Validates a decoratee if it is valid for a decorator
        given an explicitly stated type.

        @ target -- the target, can be "class", "routine", or "any" 
        @ wrapper -- wrapper object 
        @ decoratee -- the decoratee function or routine
    '''
    if inspect.isroutine(target): 
        return target(wrapper, decoratee) 
    elif type(target) == str: 
        if target == "routine": 
            if inspect.isroutine(decoratee): 
                return True
            else:
                raise Exception(f"Target for [{wrapper}] must be a routine. " +
                                f"Decoratee [{decoratee}] is a " + 
                                f"[{decoratee.__class__.__name__}]")
        elif target == "class":
            if inspect.isclass(decoratee):
                return True 
            else: 
                raise Exception(f"Target for [{wrapper}] must be a routine. " +
                                f"Decoratee [{decoratee}] is a " + 
                                f"[{decoratee.__class__.__name__}]")
        elif target == "any": 
            return True
        else:
            raise Exception(f"Invalid target [{target}] for [{wrapper}]")

def handle_class(wrapper, decoratee):
    '''
        Handles decorators designed for classes. 

        wrapper -- wrapper object 
        decoratee -- decoratee routine or class
    ''' 
    return wrapper.inner(decoratee)


def init_wrapper(wrapper, args, kwargs):
    '''
        Initializes the wrapper

        wrapper -- wrapper object 
        decoratee -- decoratee routine or class
    '''
    target = None 

    log_print("@ --- In init_wrapper() ---")
    log_print("Args:", args, "Kwargs", kwargs) 

    # fetch target routine from arguments
    if len(args) == 1 and inspect.isroutine(args[0]):
        target = args[0]

    # handle class decoratees
    if len(args) == 1 and inspect.isclass(args[0]):
        decoratee = args[0]

        # validate target
        validate_target(wrapper.kwargs.get("target"), wrapper, decoratee)
       
        # register decoratee 
        register_decoratee(wrapper, decoratee, args, kwargs)

        return handle_class(wrapper, decoratee)

    log_print("Target:", target)

    if target: 
        log_print("init_wrapper().decorator : Case A")

        def decorator(decoratee):
            log_print("Decoratee:", decoratee) 
            
            # validate target
            validate_target(wrapper.kwargs.get("target"), wrapper, decoratee)
        
            # handle class decoratees
            if inspect.isclass(decoratee): 
                return handle_class(wrapper, decoratee)

            # define inner function
            @functools.wraps(decoratee)
            def inner(*inner_args, **inner_kwargs):
                return wrapper.inner(decoratee, *inner_args, **kwargs) 

            # register decoratee 
            register_decoratee(wrapper, inner, args, kwargs)

            return inner

        return decorator(target)
    else:
        log_print("init_wrapper().decorator : Case B")

        def decorator(decoratee):
            log_print("Decoratee:", decoratee)
    
            # validate target
            validate_target(wrapper.kwargs.get("target"), wrapper, decoratee)
           
            # handle class decoratees
            if inspect.isclass(decoratee): 
                return handle_class(wrapper, decoratee)

            # define inner function
            @functools.wraps(decoratee)
            def inner(*inner_args, **inner_kwargs):
                return wrapper.inner(decoratee, *inner_args, **inner_kwargs)

            # register decoratee 
            register_decoratee(wrapper, inner, args, kwargs)

            return inner
        return decorator


def _decorator(*out_args, **out_kwargs):


    '''
        Injector for Decou decorators.   
    '''
    target = None 

    if len(out_args) == 1 and inspect.isclass(out_args[0]):
        target = out_args[0]
    
    log_print("@ --- In _decorator() ---")
    log_print("Args:", out_args, "Kwargs:", out_kwargs)
    log_print("Target:", target)

    # If `target` keyword is not present, notify that
    # it is required.
    if "target" not in out_kwargs:
        raise Exception("The target keyword parameter is required.")

    def decorator(wrapper):

        # handle case where decoratee is in outer arguments
        if len(out_args) == 1 and inspect.isclass(out_args[0]):
            log_print("_decorator: Case A")
            _wrapper = out_args[0]()
            _args = out_args
            _wrapper.args = out_args 
            _wrapper.kwargs = out_kwargs
            register_decorator(_wrapper)
        
            if hasattr(_wrapper, "init"):
                call = _wrapper.init(*_args, **out_kwargs)
                return init_wrapper(call[0], call[1], call[2])
            else: 
                return init_wrapper(_wrapper, _args, _out_kwargs)
                

        # handle case where decoratee is in the parameter wrapper
        else: 
            log_print("_decorator: Case B")
            _wrapper = wrapper()
            _wrapper.args = out_args 
            _wrapper.kwargs = out_kwargs
            register_decorator(_wrapper)

            @functools.wraps(_wrapper)
            def inner(*inner_args, **inner_kwargs): 
                if hasattr(_wrapper, "init"):
                    call = _wrapper.init(*inner_args, **inner_kwargs)
                    return init_wrapper(call[0], call[1], call[2])
                else: 
                    return init_wrapper(_wrapper, inner_args, inner_kwargs)
        
            inner.decorator = _wrapper

            return inner
            
    return decorator 

class DecorateeScope: 
    def __init__(self, *args, **kwargs):
        pass

class DecoChain:
    def __init__(self): 
        self._chain = []

    def add(self, call):
        self._chain.append(call)

    def as_list(self):
        return self._chain 

    def as_map(self):
        mapping = {}
        for chain in self._chain:
            wrapper = chain[0]
            wrappee = chain[1]
            args = chain[2]
            kwargs = chain[3]
            arg_tuple = (args, kwargs, wrappee, wrapper)
            if wrapper.__class__ not in mapping: 
                mapping[wrapper.__class__] = []
            mapping[wrapper.__class__].append(arg_tuple)
        return mapping

def register_decorator(wrapper):
    '''
        Registers a wrapper to DFRM.
    '''
    
    target_type = wrapper.kwargs["target"]
    decorators = DFRM["decorators"]
    if wrapper not in decorators[target_type]:
        decorators[target_type][wrapper] = {}
    else: 
        decorators[target_type][wrapper] += {}
    
def register_decoratee(wrapper, decoratee, args, kwargs): 
    '''
        Registers a decoratee to DFRM
    '''
    target_type = wrapper.kwargs["target"]
    
    decoratees = DFRM["decoratees"]
    decorators = DFRM["decorators"]

    if not hasattr(decoratee, DECOU_SCOPE):
        setattr(decoratee, DECOU_SCOPE, DecorateeScope())

    decou_scope = decoratee.___decou___
   
    if hasattr(decou_scope, "reference"):
        del decoratees[target_type][decou_scope.reference]

    if not hasattr(decou_scope, "deco_chain"):
        decou_scope.deco_chain = DecoChain()

    decou_call = (wrapper, decoratee, args, kwargs)

    decou_scope.reference = decoratee
    decou_scope.deco_chain.add(decou_call)

    decoratees[target_type][decou_scope.reference] = True
    decorators[target_type][wrapper][decoratee] = True