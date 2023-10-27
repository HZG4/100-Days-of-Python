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