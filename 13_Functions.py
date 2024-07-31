'''
extern "C"
int add(int, int)
float add(float, float)
int add(int, float)
int add(float, int)
int sub(int, int) --> _sub@2_in_in
'''
'''
def add(a: int, b: int):
    return a + b

def add(a: float, b: float):
    return a + b

def add(a: int, b: int, c: int):
    return a + b + c

def add(a: int, b: int, c: int = 0):
    return a + b + c

print(add(1, 2))
print(add(1.1, 2.2))
print(add(1, 2, 3))
'''

from multipledispatch import dispatch

@dispatch(int, int)
def add(a, b):
    print("Add for ints")
    return a + b

@dispatch(float, float)
def add(a, b):
    print("Add for floats")
    return a + b


print(add(1, 2))
print(add(1.1, 2.2))