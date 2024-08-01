# Fibonacci Series

def Fib(n):         # Generator Function; Returns a generator{iterator} when called
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b
'''
it = Fib(10)

while True:
    try:
        # print(next(it))
        print(it.__next__())
    except StopIteration:
        print("All done")
        break
'''
'''
for val in Fib(10):
    print(val)
'''    


it1 = Fib(10)
it2 = Fib(12)
it3 = Fib(15)

print(id(it1), id(it2), id(it3), sep='\n')

for i in range(9):
    if i%10 != 0:
        print("IT1 -->", next(it1))
    if i%2 != 0:
        print("IT2 -->", next(it2))
    if i%3 != 0:
        print("IT3 -->", next(it3))
    print()


# Iterable: Supports __iter__()                     --> iter(obj)
# Iterator: Supports __iter__() AND  __next__()     --> iter(obj), next(obj)

# iter() --> returns an iterator
#            If called on an ITER-ABLE, returns an iterator type, distinct from its own type
#

def isIterable(obj):
    try:
        it = iter(obj)
        print(type(it))
        return True
    except Exception:
        return False


lst = (1, 2, 3)
x = 10
print(isIterable(lst))


# iter() --> returns an iterator
#            If called on an ITERATOR, returns the object itself

it = iter(lst)
it_again = iter(it) # it.__iter__()
print(type(it), type(it_again), sep='\n')
print()
print(id(it), id(it_again), sep='\n')
