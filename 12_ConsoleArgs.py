import sys

def Greet():
    name = ''
    if len(sys.argv) > 1:
        name = sys.argv[1]

    print("Hi", name, "!!")

Greet()
