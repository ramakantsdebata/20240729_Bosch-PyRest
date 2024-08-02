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
        # Possible cleanup
    except (TypeError, ValueError) as ex:
        print("Exception in the second statement", "\n", ex)
        # Possible cleanup
        raise FileNotFoundError("Log file not found")           # <-- New, distinct exception raised
    except ZeroDivisionError as ex:                             # <--Partially handle the problem scenario 
        print("ZeroDivisionError-specific handler", ex)         # and delegate the rest outwards
        raise                                                   # Re-raise the earlier exception
    # except Exception:
    #     print("Intermediate Exception Handler")
    finally:
        # Exceutes this block, irrespective of exception occurance
        # Generally, used for resource cleanup
        # Possible cleanup
        print("Cleanup")

    # Possible cleanup

    # if ret is not None:
    #     print("Some Error")

    print("Program returns to normal execution")

try:
    Consumer()
    print("Any print")
except Exception as ex:
    print("After the call to Consumer")
    

print("Exiting the program now.")