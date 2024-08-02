def ReadFile(fileName):
    fl = open(file=fileName)
    textRead = fl.read(10)
    print(textRead)
    textRead = fl.readline()
    print(textRead)
    textRead = fl.readlines()
    print(textRead)
    fl.close()

def WriteFile(fileName):
    try:
        fl = open(file=fileName, mode="a")
        cpCount = fl.write("Test Data\nAnotherline")
        fl.flush()
        print(cpCount)
        fl.writelines(["Line 2", "line 3", "Line 4"])
        
    finally:
        fl.close()

def WriteFile_2(fileName):
    with open(file=fileName, mode="a") as fl:
        cpCount = fl.write("Test Data\nAnotherline")
        fl.flush()
        print(cpCount)
        cpCount = fl.writelines(["Line 2", "line 3", "Line 4"])
        print(cpCount)
        fl.close()

def RelocateCursor(fileName):
    fl = open(file=fileName, mode="r+")
    textRead = fl.read(10)
    pos = fl.tell()
    print(pos)
    fl.seek(5, 0)   # Non-zero offset for whence=0, is acceptable, else not
    fl.seek(5, 1)   # Error
    fl.seek(-5,2)   # Error
                    # Above is true only for the text mode; Works fine with the binary mode
    fl.close()        

fName = "satish.txt"
ReadFile(fName)
WriteFile(fName)
# WriteFile(fName)
RelocateCursor(fName)