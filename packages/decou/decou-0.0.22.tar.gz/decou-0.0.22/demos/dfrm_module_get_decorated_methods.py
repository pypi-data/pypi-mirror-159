from src.decou import _decorator, dfrm

@_decorator(target="any")
class task: 
    def init(wrapper, *args, **kwargs):
        return wrapper, args, kwargs 
    
    def inner(wrapper, target, *args, **kwargs): 
        return target(*args, **kwargs) 

@_decorator(target="any")
class daily: 
    def init(wrapper, *args, **kwargs):
        return wrapper, args, kwargs

    def inner(wrapper, target, *args, **kwargs): 
        return target(*args, **kwargs)

@_decorator(target="any")
class weekly: 
    def init(wrapper, *args, **kwargs): 
        return wrapper, args, kwargs 

    def inner(wrapper, target, *args, **kwargs):
        return target(*args, **kwargs)


# ----- TASK MANAGER ----- # 
class TaskManager: 

    @task 
    def task_a():   
        pass 

    @task 
    def task_b(): 
        pass 

    @task 
    @daily 
    def task_c(): 
        pass 

    @task 
    @daily 
    def task_d(): 
        pass 
    
    @task 
    @weekly 
    def task_e(): 
        pass 

    @task(a=5)
    @task(b=3)
    @weekly 
    def task_f(): 
        pass 

# Get all decorated methods with weekly tag 
with_weekly = [ member for member in dfrm.decorated_methods(TaskManager) \
                if dfrm.has_decorator(member, weekly) ]
print(with_weekly)