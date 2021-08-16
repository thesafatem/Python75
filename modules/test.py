# import calc
from geometry import perimeter
from geometry import circumference as cir

# from calc import *

print(calc.calc_var)

a, b = map(int, input().split())
print(calc.sum(a, b))
print(calc.sub(a, b))
print(calc.mul(a, b))
print(calc.div(a, b))
print(perimeter(a, b))

r = int(input())
print(cir(r))