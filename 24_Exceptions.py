def printData(data: str):
    if isinstance(data, str):
        print(data)
    else:
        divisor = 0
        # raise Exception()
        # div = data/divisor
        raise TypeError("This is a type error. Not a String")

    print("End of printData")
    

def Consumer():
    str1 = "Test String"
    try:
        printData(str1)
    except Exception:
        print("Exception in first statement")
    # if ret is not None:
    #     print("Some Error")
    print("-"*40)
    try:
        printData(10)
        print("This will be skipped")
    except (TypeError, ValueError) as ex:
        print("Exception in the second statement", "\n", ex)
    except ZeroDivisionError as ex:
        print("ZeroDivisionError-specific handler", ex)
    except Exception:
        print("Intermediate Exception Handler")
    # if ret is not None:
    #     print("Some Error")

    print("Program returns to normal execution")

try:
    Consumer()
    print("Any print")
except Exception:
    print("After the call to Consumer")

print("Exiting the program now.")