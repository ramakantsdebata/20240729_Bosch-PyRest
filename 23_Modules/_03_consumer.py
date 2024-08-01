# from _01_provider import *
from _01_provider import greet
from _01_provider import greetName
from _01_provider import Test as Provider_Test


greet()
greetName("Rakesh")


def PerformOp():
    from _01_provider import greet
    greet ()
    # from _01_provider import *   # Can't import all inside a scope. Has to be Global'''

def Test():
    print("My Test")


Provider_Test()
Test()