from collections import namedtuple

Point = namedtuple('Point', 'x y')
p1 = Point(10, 20)
p2 = Point(30, 40)

print(p1[0], p1[1])
print(p1.x, p1.y)

Student = namedtuple('Student_type', ['id', 'name', 'std'])
s1 = Student(1, "Manish", 5)
print(s1.id, s1.name, s1.std)

print(hash(s1))