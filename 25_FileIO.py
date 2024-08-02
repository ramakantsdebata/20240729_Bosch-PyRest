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
        fl = open(file=fileName, mode="rw+")
        cpCount = fl.write("Test Data\nAnotherline")
        fl.flush()
        print(cpCount)
        cpCount = fl.writelines(["Line 2", "line 3", "Line 4"])
        print(cpCount)
    finally:
        fl.close()

def WriteFile_2(fileName):
    with open(file=fileName, mode="rw+") as fl:
        cpCount = fl.write("Test Data\nAnotherline")
        fl.flush()
        print(cpCount)
        cpCount = fl.writelines(["Line 2", "line 3", "Line 4"])
        print(cpCount)

def RelocateCursor(fileName):
    fl = open(file=fileName, mode="rw+")
    textRead = fl.read(10)
    pos = fl.tell()
    fl.seek(20, whence=1)
        

fName = "README.md"
ReadFile(fName)
WriteFile(fName)
# WriteFile(fName)
RelocateCursor(fName)