'''
for i in range(5):
    print(str(i) + ": Hi")


for _ in range(5):
    print("Hi")
'''
'''x = 5
if x == 5:
    print("yes")
elif x < 5:
    print("Lesser")
else:
    print("Greater")
'''

'''
l1 = [1, 2, 3, 4, 5]
x = 3
for idx in range(len(l1)):
    if x == l1[idx]:
        print("Found it")
        break
else:
    print("Not found")
'''
'''
for val in l1:
    if x == val:
        print("Found it")
        break
else:                           # All iterations completed; Interpreted as a Failure condition
    print("Not found")
'''
'''
l1 = [1, 2, 3, 4, "Five"]

l2 = []
for val in l1:
    l2.append(val**2)
else:                       # All iterations completed; Interpreted as a Success condition
    print("L2 populated completely")
    print(l2)
print("Done")
'''
'''
## Cpp code
for (int i = 0 ; i < 10; i++)
{
    // Operations
}

if(i >= 10)
{
    //All iterations complete
}
'''

'''
## While loop
cntr = 5
while(cntr > 0):
    print("Hi")
    cntr -= 1 # cntr = cntr -1
    if cntr == 2:
        break
else:
    print("Completed iterations")

cond = True

while(True):
    if cond is True:
        break
    print("Hi")

'''

## Match case

num = int(input("Enter a number: "))

print(num, type(num))

match num:
    case 1:
        print("1 entered")
    case 2:
        print("2 entered")
    case 3:
        print("3 entered")
    case 4:
        print("4 entered")
    case 5:
        print("5 entered")
    case _:
        print("something else entered")
    