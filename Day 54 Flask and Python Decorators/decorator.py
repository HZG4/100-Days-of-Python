# <-------------------------------------- Basic Decorator Analogy ---------------------------------------->

import time
def decorator_function(func):
    def wrapper_function():
                    # do something before running the passed_function
        start_time = time.time() 
                    # call the passed function, add conditions or extend its behaviour
        func()
                    # do something after running the passed_function
        end_time = time.time()
        print(f"function: {func.__name__}, Speed: {end_time-start_time}")
                    # return wrapped function without parentheses
    return wrapper_function
 
                    # this will wrap this function in decorator_function.
@decorator_function 
def passed_function():
    print("This function just prints a string")
 
                    # call the decorated function
passed_function()


# <---------------- Using Positional Arguements and Keyword Arguements in wrapper_func() ------------------> 
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = True

def decorator_function(func):
    def wrapper_function(*args, **kwargs):
        if args[0].is_logged_in == True:
            func(args[0])
    return wrapper_function

@decorator_function
def greet_user(user):
    print(f"User {user.name} has logged in!")

new_user = User("Hamza")
greet_user(new_user)