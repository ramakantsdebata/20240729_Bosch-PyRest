# LEGB - Local, External, Global, Builtin
'''
def Outer():
    # s1 = "Outer"
    global s1
    s1 = "Global-2"
    print("Outer -->", s1)

s1 = "Global"
Outer()

print("Global -->", s1)
'''
'''
def Outer():
    num = 2
    def Inner():
        # global num
        # nonlocal num
        num = 3
        print("Inner:", num, id(num))
    Inner()

    print("Outer:", num, id(num))

    return Inner
    
num = 1
Outer()

print("Global:", num, id(num))

'''


def Outer():
    print("\nLocals --> ", locals())
    print("\nGlobals -->", globals())

    globals()['num'] = 100
    num = 2

    print("\nLocals --> ", locals())
    print("\nGlobals -->", globals())

    print("Outer:", num, id(num))
    
num = 1
Outer()

print("Global:", num, id(num))




