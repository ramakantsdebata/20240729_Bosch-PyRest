class File:
    def __init__(self) -> None:
        print("File.init")

class FileStream(File):
    def __init__(self) -> None:
        print("FileStream.init")
        File.__init__(self)

class EncryptedFile(File):
    def __init__(self) -> None:
        print("EncrptedFile.init")
        File.__init__(self)



class EncryptedFileStream(FileStream, EncryptedFile):
    def __init__(self) -> None:
        print("EncryptedFileStream.init")
        FileStream.__init__(self)
        EncryptedFile.__init__(self)



efs = EncryptedFileStream()
