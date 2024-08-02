def ReadFile(fileName):
    fl = open(file=fileName)
    textRead = fl.read(10)
    print(textRead)
    textRead = fl.readline()
    print(textRead)
    textRead = fl.readlines()
    print(textRead)
    print("-"*40)
    fl.close()

def WriteFile(fileName):
    try:
        fl = open(file=fileName, mode="w+")
        cpCount = fl.write("Test Data\n Anotherline")
        fl.flush()
        print(cpCount)
        cpCount = fl.writelines(["Line 2", "line 3", "Line 4"])
        print("1",cpCount)
    finally:
        fl.close()

def WriteFile_2(fileName):
    with open(file=fileName, mode="w+") as fl:
        cpCount = fl.write("Test Data\n Anotherline")
        fl.flush()
        print("2",cpCount)
        cpCount = fl.writelines(["Line 2", "line 3", "Line 4"])
        print(cpCount)

def RelocateCursor(fileName):
    fl = open(file=fileName, mode="r+")
    fl.seek(0,2)
    pos = fl.tell()
    print(pos)
    fl.seek(0, 0)
    textRead = fl.read(10)
    print(textRead)
    pos = fl.tell()
    fl.seek(5, 0)   # Non-zero offset for whence=0, is acceptable, else not
    fl.seek(5, 1)   # Error
    fl.seek(-5,2)   # Error
                    # Above is true only for the text mode; Works fine with the binary mode
    fl.close()
        

fName = "sample.txt"
# ReadFile(fName)
# WriteFile(fName)
# WriteFile(fName)
RelocateCursor(fName)