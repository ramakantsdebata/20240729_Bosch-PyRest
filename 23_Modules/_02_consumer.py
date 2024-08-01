'''
import _01_provider
print("Imported modules ------------------")

_01_provider.greet()
_01_provider.greetName("Manish")
_01_provider.Test()
'''

from _01_provider import *
# from _01_provider import prepGreet
print("Imported modules ------------------")

greet()
# greetName("Manish")
# print(prepGreet("1", "2"))
# Test()
'''
def Test():
    print("Test")
'''


# Test()