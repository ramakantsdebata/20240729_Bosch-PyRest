#!/usr/bin/env py
# print("Hi")


# print(float(2**53))
# print(float(2**53+1))
# print(float(2**53+2))
# print(float(2**53+3))
# print(float(2**53+4))


print((0.7 - 0.6) == 0.1)
print(0.7 - 0.6)

from decimal import Decimal
x = Decimal(0.55)
print(x, type(x))


print((Decimal(0.7) - Decimal(0.6)) == Decimal(0.1))
print(Decimal(0.7) - Decimal(0.6))
print(Decimal('0.7') - Decimal('0.6'))

import decimal

print(decimal.getcontext())
y = Decimal('22')/Decimal('7')
print(y)
decimal.getcontext().prec = 5
y = Decimal('22')/Decimal('7')   # Decimal('22').operator/(Decimal('7'))
print(y)
decimal.getcontext().rounding = decimal.ROUND_FLOOR
decimal.getcontext().prec = 28
R = 7
# PI = 22/7
PI = Decimal('22')/Decimal('7')
print(2*PI*R)

from fractions import Fraction  

PI = Fraction('22/7')
print(PI)
print(2*PI*R)

two_third = Fraction(2, 3)
one_tenth = Fraction('0.1')
arb = Fraction(2456/27889)
print(one_tenth, arb)