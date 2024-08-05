from _30_ClassOfStudents import Student
import json

def Test1():
    ## JSON Operations ####################
    # 1. Create object and store it to a file
    fileName = "Students.json"

    st1 = Student(1, "Vinayak", 4.5)

    dt1 = {
        'roll': st1._roll,
        'name': st1._name,
        'aggregate': st1._aggregate,    
    }

    with open(fileName, mode="w") as file:
        json.dump(dt1, file)
        

    ## Modify the object in the file
    with open(fileName, "r") as file:
        dt2 = json.load(file)


    st2 = Student(dt2['roll'], dt2['name'], dt2['aggregate'])
    print(st2)
    st2.aggregate = 4.75

    # Now as before, covert the object to a dictionary, and then dump it to a json file

def Test2():
    import pickle
    fileName_p = "Student.pkl"

    st1 = Student(1, "Vinayak", 4.5)

    with open(fileName_p, "wb") as file:
        pickle.dump(st1, file)

    # Read from the file, modify the object and store it back to the file
    with open(fileName_p, "rb") as file:
        st2 = pickle.load(file)

    print(type(st2))
    st2.aggregate = 4.75
    print(st2)

    with open(fileName_p, "wb") as file:
        pickle.dump(st2, file)


Test2()