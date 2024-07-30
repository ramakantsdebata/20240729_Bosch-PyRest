# bytes - Immutable
# bytearrays - Mutable

bstr1 = b"TestString"
print(bstr1.hex(), type(bstr1))
s1 = bstr1.decode()
print(s1, type(s1))

s2 = str(bstr1, "utf-8")
print(s2, type(s2))

val = 10
x = val.to_bytes(10,"big")
print(x.hex(), type(x))

new_val = int.from_bytes(x,"big")
print(new_val, type(new_val))

import codecs

s1 = "TestString"
x = s1.encode("utf-8")
x = codecs.encode(s1, "utf-8")
print(x, type(x))

