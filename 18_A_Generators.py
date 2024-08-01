'''
int Method()
{
    static int cntr = 0;
    return ++cntr;
}
'''

# def Method():
#     cntr = 0
#     cntr += 1
#     return cntr

def Method():
    cntr = 1
    yield cntr
    cntr += 1
    yield cntr  
    cntr += 1
    yield cntr  
    cntr += 1
    yield cntr  
    cntr += 1
    yield cntr  

'''
gen = Method()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))  # 6th time leads to an Exception --> StopIteration
'''
'''
gen = Method()
while True:
    try:
        print(next(gen))
    except StopIteration:
        print("All Done")
        break
'''

# for val in Method():
#     print(val)

#############################################

def Method2():
    cntr = 1
    # while True:
    for _ in range(10):
        cntr += 1
        yield cntr

gen = Method2()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
