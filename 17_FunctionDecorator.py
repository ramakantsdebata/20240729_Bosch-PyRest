def LogHelper(fn):
    def wrapper(*vArgs, **kwArgs):      # Packing the args received
        print(fn.__name__, "called")
        ret_val = fn(*vArgs, **kwArgs)     # Unpacking the args received
        return ret_val
    wrapper.__doc__ = fn.__doc__
    return wrapper

#############################################
# @LogHelper
def Greet():
    print("Hi")

Greet = LogHelper(Greet)   # Explicit assignment, instead of decorating the method above

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


@LogHelper
def Add(a, b, *varData, **kwData):
    sum = a + b

    for val in varData:
        print(val)

    for k, val in kwData.items():
        print(k, val)


    for val in varData:
        sum += val

    for val in kwData.values():
        sum  += val

    return sum

# Greet = Method(Greet)
# wrapper(Greet)
# Greet = wrapper

##################################

Greet()

TestFunc()

print("Preped greeting -->", GreetName("John"))
print(GreetName(1)) 

print(Add(1, 2, 3, 4, e = 5, f = 6))