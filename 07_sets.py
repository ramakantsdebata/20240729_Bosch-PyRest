# set [Mutable] - collection of keys [immutables]
# Key - A hashable entity
# Hashable - Something that doesn't shange
# Why - If the obj changes, the hash changes
# Hash - Unidirectional transformation of data

'''l1 = [1, 2]
l2 = [2, 3]

st1 = set()
st1.add(l1)
st1.add(l2)
'''

val = 10
print(hash(val))

st1 = "Test"
print(hash(st1))

tp = (1, 2, 3, 4)
print(hash(tp))

lst = [1, 2, 3, 4]
# print(hash(lst))

st1 = {1, 2, 3, 4}
st2 = {4, 5, 6}
print(st1, st2, sep='\n')

if 1 in st1:
    print("yes")

print(st1 | st2)
print(st1.union(st2))

print(st1 & st2)
print(st1 - st2)
print(st1 ^ st2)

print(st1.isdisjoint(st2))
print(st1 & st2 == set())

'''
issubset
issuperset()
'''

st3 = {1, 2}
print(st3.issubset(st1))
print(st1.issuperset(st3))

st1.remove(4); print(st1)
st1.discard(7); print(st1)

print(st1.pop())


## Frozenset - Immutable collection of keys
fs = frozenset(st1)
print(fs, type(fs))

print(hash(fs))
st4 = {1, 2, 3, fs}
print(st4)

fs2 = frozenset(st4)
print(fs2)