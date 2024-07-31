'''
def add(a: int, b: int) -> int:
    return a + b

print(add(1, "two"))
'''

## Define Higher vs. Define Earlier
'''
def Bar():
    print("Bar")
    Baz()

def Foo():
    print("Foo")
    Bar()

def Baz():
    print("Baz")

def Main():
    print("Main")
    Foo()

Main()
'''

## Argument passing
# 1. Positional args
'''
def add(a, b = 0, c = 0):       # Non-default args can't be after default args
    print(f"{a}, {b}, {c}")
    return a + b + c

print(add(1, 2, 3))


print(add(a=1, c = 2, b = 3)) # Named args = Keyworded
                              # Pos. args can't be after kw-args

print(add(1, c = 2))

'''
# Unpacking and packing
'''
lst = [1, 2, 3]
a, b, c = lst
print(a, b, c)

def add(a, b = 0, c = 0):
    print(f"{a}, {b}, {c}")
    return a + b + c

print(add(lst[0], lst[1], lst[2]))

a, b, c = 1, 2, 3
a, b, c = lst
print(add(a, b, c))

print(add(*lst))        # Unpacking a collection in the call

lst = (1, 2, 3, 4, 5, 6, 7)
a, b, c, *others = lst
# Unpacking 'lst'
# assigning to a, b & c
# Packing the rest into 'others' 
print(type(lst), lst)
print(type(others), others)


def Method(*lst1):                  # Packing the data passed during call
    print(len(lst1), type(lst1))

Method(1, 2, 3, 4, 5, 6, 7)
'''
'''
def Multiret():
    a = 1
    b = 2
    c = 3
    return a, b, c

lst = list(Multiret())
print(type(Multiret()))
'''
''' INCORRECT USAGE
data: list
*data = 1, 2, 3
print(type(data), data)
'''
'''
def Method(*lst):
    print(type(lst), lst)

Method([1, 2, 3])
l1 = [1, 2, 3, 4]
Method(l1)
'''

## Variable Args
'''
def Add1(a, b, *data):
    print(a, b, data)
    sum  = a + b
    for val in data:
        sum += val
    return sum

def Add2(*data):
    if isinstance(data[0], int):
        sum = 0
    else:
        sum = ''

    for val in data:
        sum += val
    return sum

def Add3(*data):
    sum = data[0]

    for idx in range(1, len(data)):
        sum += data[idx]
    return sum

# print(Add())
# print(Add(1))
print(Add3(1, 2))
print(Add3(1, 2, 3, 4, 5))

print(Add3("Hi", "There", "Howdy"))
'''

def Sentence(**kwWords):          # Keyworded args / kwargs
    res = ''
    for k, v in kwWords.items():
        print(k, v)

    for word in kwWords.values():
        res = res + word + ' '

    return res

print(Sentence(First = "Hi", Second = "there"))
# print(Sentence('Hi', 'there', 'how', 'is', 'the', 'weather', 'today', 'over', 'there'))


## Special Args
# / --  Args to the left of '/' should only be positional
# * -- Args to the right of the '*' should only be keyworded
'''
def method(a, b=0 , /, c=0, d=0, *, e=0, f=0):
    pass

method(1)
method(1, 2)
# method(1, b = 2)  # Error

method(1, 2, 3)
method(1, 2, 3, d = 4)

# method(1, 2, 3, 4, 5) # Error
method(1, 2, 3, 4, e=5)

def open_cust(name, /, mode = 'r', newline = '\n', *, encoding = 'utf-8', closefd:bool = True):
    pass

open_cust("file.txt")
# open_cust(name="file.txt")
open_cust("file.txt", encoding='utf-16', newline='')


def wrapper(*vArgs, **kwArgs):  ## Packing the received data into a collection
    print("Calling the method")
    localFn = open_cust(*vArgs, **kwArgs)  ## Unpack the collections
    pass

wrapper("file.txt", encoding='utf-16', newline='')
'''

def GenericArgList(*vArgs, **kwArgs):
    print("Arguments are :-")
    for args in vArgs:
        print(args)

    for k, v in kwArgs.items():
        print(k, v)

    print("Done\n\n")

GenericArgList()
GenericArgList(1)
GenericArgList(1, 2, 3)
GenericArgList(a= 1, b = 2, c = 3)
GenericArgList(1, 2, 3, a= 1, b = 2, c = 3)