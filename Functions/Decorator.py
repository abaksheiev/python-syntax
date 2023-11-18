def decorator(fun):
    def wrapper(msg):
        print('*'*10)
        fun(msg)
        print('*'*10)
    return wrapper

@decorator
def dispalay(msg):
     print(msg)

dispalay('Welcome')
