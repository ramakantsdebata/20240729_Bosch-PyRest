# Quotes
# '' or "" have the same semantics

str1 = "This is Abhijeet's notebook."
str2 = 'He said, "Thanks".'

print(str1)
print(str2)

str3 = '''
Multiline string
More lines
Can be used for doc strings as well
'''

print(str3)

def add(a, b):
    '''Adds two data points and returns the sum.
    Can work with numerical types or with types supporting the "+" operator.
    Usage: add(data1, data2)    returns  sum'''
    if isinstance(a, int) == False:
        print(add.__doc__)
    return a + b

print(add.__doc__)
add(1.0, 2.0)

print("One""Two")



training = "Python"
day = 8

s1 = "We are in a %s training for %d days"
finalstr = s1%(training, day)
print(finalstr)

s2 = "We are in a {} training for {} days".format(training, day)
print(s2)

s3 = f"We are in a {training} training for {day} days"    #.format(training, day)
print(s3)

path = r"c:\Users\temp\newfile.txt"  # 'r' or 'R' denotes Raw string; All escaped characters are ignored
print(path)


print(s3[3])
print(s3[3:6])
print("[",s3[3:12:2], "]")
print("[",s3[::2], "]")
print("[",s3[1::2], "]")
print(s3[-1])
print(s3[::-1])

