class BaseType:
    def __init__(self, data) -> None:
        self.dataBase = data
        print("BaseType-->", self.__class__.__mro__)

        
    def __str__(self) -> str:
        return f"A-{self.dataA}"


class A(BaseType):
    def __init__(self, data) -> None:
        print("A-->", self.__class__.__mro__)
        super().__init__(data)
        self.dataA = data

    def __str__(self) -> str:
        return f"A-{self.dataA}"

class B(BaseType):
    def __init__(self, data) -> None:
        print("B-->", self.__class__.__mro__)
        super().__init__(data)
        self.dataB = data

    def __str__(self) -> str:
        return f"B-{self.dataB}"

class C(A, B):
    def __init__(self, data) -> None:
        print("C-->", self.__class__.__mro__)
        super().__init__(data)

    def __str__(self) -> str:
        return super().__str__()
    


print("\nMROs -->")
print(f"{BaseType.__mro__ = }")
print(f"{A.__mro__ =}")
print(f"{B.__mro__ =}")
print(f"{C.__mro__ =}")
print("\n\n")


c = C(10)

# print(c.__class__.__bases__)
# print(c.__class__.__mro__)

