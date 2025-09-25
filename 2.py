from math import *

def get_number(x, y, z):
  return 5 * atan(x) - 0.25 * acos(x) * ((x + 3 * abs(x - y) + x ** 2) / (abs(x - y) * z + x**2))

print(get_number(0.1722, 6.33, 3.25*10**-4))
