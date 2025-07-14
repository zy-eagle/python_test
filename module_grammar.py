import os

print(os.getcwd())

print("###################################")

from os import getcwd

print(getcwd())

print("###################################")

print(__name__)  # __name__ is '__main__' when the script is run directly

if __name__ == '__main__':
    print("This script is being run directly")

print("###################################")

from sympy import Derivative, Symbol

x = Symbol('x')
y = x * x + 3 * x + 1
derivative_y = Derivative(y, x)
print(derivative_y.doit())  # This will compute the derivative of y with respect to x
print(derivative_y.doit().subs({x: 2}))  # This will substitute x with 2 in the derivative

from sympy.plotting import plot
plot(y, (x, -10, 10))  # This will plot the function y = x^2 + 3x + 1 over the range -10 to 10

print("###################################")

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
point_inst = Point(1, 2)
print(point_inst.x)
print(point_inst.y)

# 实现运算符的重载
class PointKlass(namedtuple('Point', ['x', 'y'])):
    def __add__(self, other):
        self.other_x, self.other_y = other.x, other.y
        return self.x + self.other_x, self.y + self.other_y

p1 = PointKlass(1, 2)
p2 = PointKlass(3, 4)
print(p1 + p2)



























