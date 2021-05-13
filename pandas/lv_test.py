def my_decorator(self):
    def inner():
        return "Hello World"
    return inner

@my_decorator
def my_func():
    print("*"*10)

my_func()








# ******
# HEllo World
# ******