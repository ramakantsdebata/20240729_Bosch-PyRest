# Lambda / Annonymous-Functions

tools = []

# def square(num):
#     return num ** 2

# square = lambda num : num ** 2

def cube(num):
    return num ** 3

def quad(num):
    return num ** 4

tools.append(lambda num : num ** 2)
tools.append(cube)
tools.append(quad)

## Iteration 2 #########################################

tools = []

tools.append(lambda num : num ** 2)
tools.append(lambda num : num ** 3)
tools.append(lambda num : num ** 4)

## Iteration 3 #########################################

def MethodGenerator(power):
    return lambda num: num ** power

print("--->", end=' ')
square = lambda num : MethodGenerator(2)(num)

## CONSUMER 1 #########################################

# for i in range(3):
#     print(tools[i](10))

## CONSUMER 2 #########################################
# for i in range(2, 5):
#     print((lambda num : num ** i)(10))

## CONSUMER 3 #########################################

tools = []
tools.append(MethodGenerator(2))
tools.append(MethodGenerator(3))
tools.append(MethodGenerator(4))

for i in range(3):
    print(tools[i](10))


print(MethodGenerator(2)(10))



## Call-backs

class Integer:
    def __init__(self, data) -> None:
        self.data = data

    def setData(self, value):
        self.data = value

    def getData(self):
        return self.data
    
    def __str__(self):
        return self.__repr__() + " --> " + str(self.getData())
    
# i1 = Integer(5)

from random import randint

lst = []
for _ in range(10):
    lst.append(Integer(randint(0, 10)))

for val in lst:
    print(val) # val --> str(val) --> val.__str__() --> val.__repr__()


nextEven = lambda x : x+2 if x%2 == 0 else x+1

print(nextEven(2))
print(nextEven(17))