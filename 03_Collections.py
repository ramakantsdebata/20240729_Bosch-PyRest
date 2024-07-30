x = 100000

# Identity
print(id(x))

# Type
print(type(x))

# State
print(x) # --> print(str(x)) --> print(x.__str__()) --> print(x.__repr__())


'''
class MyType:
    def __str__(self):
        return "Stringify"

    # def __repr__(self):
    #     return "Representing"

obj = MyType()
print(obj)
print(str(obj))
print(obj.__str__())
print(obj.__repr__())
print(hex(id(obj)))
'''

'''
y = x
print(id(y))
y += 1
print(id(x), id(y))

a = 100
print(id(a))
a += 1
print(id(a))
'''

y = 100001
y -= 1
print(x, id(x), "\n", y, id(y))


print("\n\n", "=#"*40, "\n" )
l1 = [1, 2]
print(type(l1), id(l1))
l1.append(3)
print(type(l1), id(l1))
l1[0] = 10