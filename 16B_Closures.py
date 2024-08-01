def Exponents(exp: int):
    def Inner(num):
        return num**exp
    return Inner



sqr = Exponents(2)
cube = Exponents(3)
c = cube

num = sqr(2)
print(num)

num = c(2)
print(num)