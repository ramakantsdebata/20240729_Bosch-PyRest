# Get the code working without any change to the Test() method

class Student:
    def __init__(self, roll, name, aggregate) -> None:
        self._roll = roll
        self._name = name
        self._aggregate = aggregate

    def __str__(self) -> str:
        return f"{self._roll}, {self._name}, {self._aggregate}"
    
class ClassRoom:
    # Create a collection of Students
    # 1. Enable the class to accept a collection in the initialiser
    # 2. Support adding/removing students to the classroom.
    # 3. Support printing the list of all students in the class
    # 4. Support accessing an individual student from the classroom, using indices (subscript operator)  --> clsRoom[5]
    pass


def Test():
    students = [Student(1, "Vishal", 4.0), Student(2, "Rakesh", 4.5), Student(3, "Ekta", 4.5), Student(4, "Abhay", 4.0)]
    
    clsRoom1 = ClassRoom()
    clsRoom2 = ClassRoom(students)

    clsRoom2.add(Student(5, "Manish", 3.5))

    print(clsRoom1)
    print(clsRoom2)
    print(clsRoom2[3])
    clsRoom2[2].aggregate = 4.75

    print(clsRoom2)



if __name__ == '__main__':
    Test()