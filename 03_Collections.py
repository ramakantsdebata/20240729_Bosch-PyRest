x = 10

# Identity
print(id(x))

# Type
print(type(x))

# State
print(x) # --> print(str(x)) --> print(x.__str__()) --> print(x.__repr__())


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