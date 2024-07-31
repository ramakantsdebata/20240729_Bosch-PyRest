def LogHelper(fn):
    def wrapper(*vArgs, **kwArgs):
        print(fn.__name__, "called")
        return fn(*vArgs, **kwArgs)
    wrapper.__doc__ = fn.__doc__
    return wrapper

#############################################
@LogHelper
def Greet():
    print("Hi")

@LogHelper
def TestFunc():
    print("Test")

@LogHelper
def GreetName(name):
    '''
    Usage: GreetName(<str>)
    Argument has to be a str obj
    '''
    if not isinstance(name, str):
        return GreetName.__doc__

    greeting = "Hi, " + name
    # print(greeting)
    return greeting
    

# Greet = Method(Greet)
# wrapper(Greet)
# Greet = wrapper

##################################

Greet()

TestFunc()

print("Preped greeting -->", GreetName("John"))
print(GreetName(1)) 