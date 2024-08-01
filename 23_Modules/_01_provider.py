# __all__ = ['greet', 'greetName', 'greetInteract']

def greet():
    print("Hi")

def greetName(name:str):
    greeting = "Hi"
    finalGreet = prepGreet(greeting, name)
    print(finalGreet)

def greetInteract():
    name = input("Enter your name: ")
    greeting = "Hi"
    finalGreet = prepGreet(greeting, name)
    print(finalGreet)

def prepGreet(greeting, name):
    return greeting + " " + name

def Test():
    greet()
    greetName("Ramakant")
    greetInteract()

print(__name__)

if __name__ == '__main__':
    Test()

'''
if __name__ == '__main__':
    greet()
    greetName("Ramakant")
    greetInteract()
'''


