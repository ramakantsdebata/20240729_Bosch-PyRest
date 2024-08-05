from random import randint

class Car:
    _count = 0
    def __init__(self, make, model, color) -> None:
        self._make = make
        self._model = model
        self.__color = color
        self._chasisNo = self.genSerial()
        Car._count += 1

    def __str__(self) -> str:
        # self.__class__.__name__
        return f"Car[{self._count}] --> {self._make}, {self._model}, {self.__color}, {self._chasisNo}"
    
        ## self.count vs. Car.count

    @property
    def Color(self):         # R-value
        return self.__color

    @Color.setter
    def Color(self, value):  # L-value
        self.__color = value

    @classmethod
    def PrintCount(cls):
        print(Car._count, end=', ')

    @staticmethod
    def genSerial() -> int:
        return randint(1, 100)




class GearedCar(Car):
    _count = 0
    def __init__(self, make, model, color, gears) -> None:
        super().__init__(make, model, color)
        self._gears = gears
        GearedCar._count += 1
        self.__color = "beige"
    
    def __str__(self) -> str:
        return super().__str__() + f", {self._gears}, {self.__color}"
    
    @classmethod
    def PrintCount(cls):
        super().PrintCount()
        print(GearedCar._count)

class SpecificGearedCar(GearedCar):
    _count = 0
    def __init__(self, make, model, color, gears, engine) -> None:
        super().__init__(make, model, color, gears)
        self._engine = engine
        SpecificGearedCar._count += 1

    def __str__(self) -> str:
        return super().__str__() + f", {self._engine}"
    

    # @classmethod
    # def PrintCount(cls):
    #     super().PrintCount()
    #     print(SpecificGearedCar.count, end=', ')

#####################################################

def Test1():
    Car.PrintCount()
    c1 = Car("Honda", "Accord", "Black")
    c2 = Car("Hyundai", "Accent", "Red")
    c3 = Car("Toyota", "Camry", "Yellow")

    print(c1)
    print(c2)
    print(c3)

    c1.PrintCount()
    Car.PrintCount()


def Test2():
    c1 = Car("Honda", "Accord", "Black")
    c2 = Car("Hyundai", "Accent", "Red")
    c3 = Car("Toyota", "Camry", "Yellow")
    gc1 = GearedCar("Honda", "Accord", "Black", 5)
    gc2 = GearedCar("Hyundai", "Accent", "Red", 7)
    sgc1 = SpecificGearedCar("Hyundai", "Accent", "Red", 7, "V12")

    print(sgc1)
    sgc1.PrintCount()

def Test3():
    c1 = Car("Honda", "Accord", "Black")
    print(c1)

    sgc1 = SpecificGearedCar("Hyundai", "Accent", "Red", 7, "V12")
    print(sgc1) # sgc1.__str__()
    # print(c1.__color)

def Test4():
    print(dir(Car))
    c1 = Car("Honda", "Accord", "Black")
    print(dir(c1))
    print(c1._Car__color)

    sgc1 = SpecificGearedCar("Hyundai", "Accent", "Red", 7, "V12")
    print(dir(sgc1))
    print("\n\n")
    print(sgc1)


    print(sgc1.Color)
    sgc1.Color = "Blue"
    print(sgc1.Color)
    print(sgc1)
    



Test4()