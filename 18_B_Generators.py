# Fibonacci Series

def Fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

it = Fib(10)

# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         print("All done")
#         break


for val in Fib(10):
    print(val)