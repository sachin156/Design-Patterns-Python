# from functions import wraps

def simpdeco(func):
    def wrapper():
        print("before the function")
        func()
        print("After the function")
    return wrapper

def say_whee():
    print("whee")

say_whee=simpdeco(say_whee)
print(say_whee())



def make_blink(function):

    def decorator():
        ret=function()
        return "<blink>"+"Hello World from make blink"+"</blink>"
    return decorator


# Using the @make_blink decorator to use the function
@make_blink
def hello_world():
    return "Hello World"

print(hello_world())




