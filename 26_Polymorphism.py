class Animal:
    def speak(self):
        pass

    def Eat(self):
        print("Munching")


# class Dog(Animal):
class Dog:
    def speak(self):
        print("Woof")

    def Show(self):
        return self.__str__()

# class Cat(Animal):
class Cat:
    def speak(self):
        print("Meow")


# class Cow(Animal):
class Cow:
    def speak(self):
        print("Moo")

    def Eat(self):
        print("Ruminate")


#########################################

def Converse(obj: Animal):
    obj.speak()

########################################

d = Dog()
c = Cat()
cw = Cow()

d.speak()

an: Animal = d
Converse(an)

an = c
Converse(an)

an = cw
Converse(an)

def RandomAnimal() -> Animal:
    from random import randint
    ch = randint(1, 3)
    match ch:
        case 1:
            return Dog()
        case 2:
            return Cat()
        case 3:
            return Cow()


an = RandomAnimal()
Converse(an)