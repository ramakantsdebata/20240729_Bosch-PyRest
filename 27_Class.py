class Car:
    count = 0
    def __init__(self, make, model, color) -> None:
        self.make = make
        self.model = model
        self.color = color
        Car.count += 1

    def __str__(self) -> str:
        return f"Car[{self.count}] --> {self.make}, {self.model}, {self.color}"
        ## self.count vs. Car.count

    
    @classmethod
    def PrintCount(cls):
        print(cls.count)
    
#####################################################

Car.PrintCount()
c1 = Car("Honda", "Accord", "Black")
c2 = Car("Hyundai", "Accent", "Red")
c3 = Car("Toyota", "Camry", "Yellow")

print(c1)
print(c2)
print(c3)

c1.PrintCount()
Car.PrintCount()