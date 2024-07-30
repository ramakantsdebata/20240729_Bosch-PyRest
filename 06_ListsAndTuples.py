# List - Mutable collection of non-homogenous elements
def add(a, b):
    return a + b

lst = [1, 2, "Ramakant", add, 5, 2]

print(lst[1])
print(lst[3](1, 2))
lst.append(35)
lst.remove(2)
print(lst)

print(len(lst))  # lst.__len__()

if add in lst:
    print("Present")
else:
    print("Not found")

print(lst.pop(2))
print(lst)

lst2 = [5] * 5
print(lst2)

print("#"*40)


for val in lst:
    print(val)

for idx, val in enumerate(lst):
    print(idx, val)

##############################################################

str1 = "Manish"
str2 = str1
str1 += "!!"
print(str1)
print(str2)


# lst1 = [1, 2, 3, 4, 5]
# lst2 = lst1
# lst1[1] = 200
# print(lst1)
# print(lst2)

def Func(some_list):
    print(id(some_list))
    print(type(some_list))
    some_list[1] = 200
    print(some_list)

lst1 = [1, 2, 3, 4, 5]
print(id(lst1))
print("Printing the data ->",lst1[:])
Func(lst1[:])
print(id(lst1))
print(lst1)


tp = (1, 2, 3, 4, 5) # Immutable
newlist = list(tp) ; print(newlist)
newtuple = tuple(newlist); print(newtuple)

# tp.append(10)
# tp.remove(2)

lst = list(tp)
lst.append(6)
tp = tuple(lst)


print(tp)