from __future__ import division

import numpy
from sympy import *
import math
from fractions import Fraction
from sympy import *

x, y = symbols('x y')


def slope(x1, y1, x2, y2):
    m = 0
    b = (x2 - x1)
    d = (y2 - y1)
    if b != 0:
        m = d/b

    Yintercept = -m * x1 + y1

    print('slope:', m)
    print('y-intercept:', Yintercept)
    print('y = {}x + {}'.format(m, Yintercept))
    return m


def DistanceFormula(x1, y1, x2, y2):
    # d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    a = (x2 - x1) ** 2
    b = (y2 - y1) ** 2
    c = a + b
    print('√{}'.format(c))
    distance = math.sqrt(c)
    print(distance)


def MidPointOfALine(x1, y1, x2, y2):
    # (x, y) = (x1 + x2)/2, (y1 + y2)/2
    x = (x1 + x2)/2
    y = (y1 + y2)/2
    print(x, y)
    return x, y


def EndPointOfALine(end_point1, end_point2, mid_point1, mid_point2):
    #Mid point = (Endpoint #1 + Endpoint #2)/2
    # x1 = (x + x2)/2
    #end point#2 = -endpoint#1 + midpoint * 2
    x = -end_point1 + mid_point1 * 2
    y = -end_point2 + mid_point2 * 2
    print(x, y)


def MixedFractionIntoImproper(a, b, c):
    answer = (a * c + b)/c
    return answer


def ImproperFractionIntoMixed(a, b):
     c = a // b
     d = a % b
     print('{},{}/{}'.format(c, d, b))


def DecimalIntoFraction(x):
    fraction = Fraction(x)
    print(fraction)


def CircleEquation(x, y):
    # x ** 2 + y ** 2 = r ** 2
    r = x ** 2 + y ** 2
    print('r squared =', r)
    return r


def AreaOfCircle(r):
    # pi*radius(squared)
    a = r ** 2 * 3.14
    print(a)
    return a


def CircumferenceOfCircle(r):
    c = r * 2 * 3.14
    print(c)
    return c


def Centroid(x1, y1, x2, y2, x3, y3):
    x = (x1 + x2 + x3)/3
    y = (y1 + y2 + y3)/3
    print(x, y)
    return x, y


def PerpendicularBisector(x1, y1, x2, y2):
    x_midpoint = (x1 + x2) / 2
    y_midpoint = (y1 + y2) / 2
    print('midpoints = ({}, {})'.format(x_midpoint, y_midpoint))
    # y - y_midpoint = m(x - x_midpoint)
    x_midpoint = x_midpoint * -1
    y_midpoint = y_midpoint * -1
    m = 0
    b = (x2 - x1)
    d = (y2 - y1)
    if b != 0:
        m = d/b
        fraction = Fraction(m)
        negative_reciprocal = 1/(fraction) * -1
        negative_reciprocal = float(negative_reciprocal)
    Yintercept = negative_reciprocal * x_midpoint - y_midpoint
    print('slope:', negative_reciprocal)
    print('y = {}x + {}'.format(negative_reciprocal, Yintercept))


def circumcenter(x1, y1, x2, y2, x3, y3):
    x, y = symbols('x y')
    x_midpoint_1 = (x1 + x2)/2
    y_midpoint_1 = (y1 + y2)/2

    x_midpoint_2 = (x2 + x3)/2
    y_midpoint_2 = (y2 + y3)/2

    a = [x_midpoint_1, x_midpoint_2, y_midpoint_1, y_midpoint_2]
    number = 0
    for i in a:
        print(a[number])
        number += 1

    x_midpoint_1 = x_midpoint_1 * -1
    x_midpoint_2 = x_midpoint_2 * -1

    y_midpoint_1 = y_midpoint_1 * -1
    y_midpoint_2 = y_midpoint_2 * -1

    slope_1 = 0
    placeHolder_1 = (x2 - x1)
    placeHolder_2 = (y2 - y1)
    if placeHolder_1 != 0:
        slope_1 = placeHolder_2/placeHolder_1
        slope_1 = Fraction(slope_1)
        negative_reciprocal = 1/slope_1 * -1

    Yintercept = negative_reciprocal * x_midpoint_1 - y_midpoint_1

    slope_2 = 0
    placeHolder_3 = (x3 - x2)
    placeHolder_4 = (y3 - y2)
    if placeHolder_3 != 0:
        slope_2 = placeHolder_4/placeHolder_3
        slope_2 = Fraction(slope_2)
        negative_reciprocal_2 = 1/slope_2 * -1

    Yintercept_2 = negative_reciprocal_2 * x_midpoint_2 - y_midpoint_2

    #eq1 = Eq(negative_reciprocal*x+Yintercept-(negative_reciprocal*x+Yintercept_2), 0)
    #eq2 = Eq(negative_reciprocal*x+Yintercept, 0)
    #sol = solve([eq1, eq2], [x, y])
    #print(sol)

    print('y = {}x + {}'.format(negative_reciprocal, Yintercept))
    print('y = {}x + {}'.format(negative_reciprocal_2, Yintercept_2))
    print(f'Take this to https://www.symbolab.com/solver/non-linear-system-of-equations-calculator \n y = '
          f'{negative_reciprocal}x + {Yintercept}, y = '
          f'{negative_reciprocal_2}x + {Yintercept_2} ')

def altitudesTriangle(x1, y1, x2, y2, x3, y3):
    a = x2 - x1
    b = y2 - y1
    # a and b are placeholder
    if a != 0:
        slope_1 = b/a
        slope_1 = 1/slope_1 * -1
        Yintercept_1 = (slope_1 * x3 - y3) * -1
        print('y = {}x + {}'.format(slope_1, Yintercept_1))
    else:
        print('x = {}'.format(y3))
    #find negative reciprocal, slope, y intercept
    #then repeat for all 3 altitudes

    a = x3 - x2
    b = y3 - y2
    if a != 0:
        slope_2 = b/a
        slope_2 = 1/slope_2 * -1
        Yintercept_2 = (slope_2 * x1 - y1) * -1
        print('y = {}x + {}'.format(slope_2, Yintercept_2))
    else:
        print('x = {}'.format(y1))

    a = x1 - x3
    b = y1 - y3
    if a != 0:
        slope_3 = b/a
        slope_3 = 1/slope_3 * -1
        Yintercept_3 = (slope_3 * x2 - y2) * -1
        print('y = {}x + {}'.format(slope_3, Yintercept_3))
    else:
        print('x = {}'.format(y2))


def threeDistanceFormula(x1, y1, x2, y2, x3, y3):
    #find 3 distances instead of one
    a = (x2 - x1) ** 2
    b = (y2 - y1) ** 2
    c = a + b
    print('√{}'.format(c))
    print(math.sqrt(c))
    a = (x3 - x2) ** 2
    b = (y3 - y2) ** 2
    c = a + b
    print('√{}'.format(c))
    print(math.sqrt(c))
    a = (x1 - x3) ** 2
    b = (y1 - y3) ** 2
    c = a + b
    print('√{}'.format(c))
    print(math.sqrt(c))

def negativeReciprocal(a):
    try:
        a = 1 / a * -1
    except ZeroDivisionError:
        pass
    #print('slope = {}'.format(a))
    #put back if triangleType isn't use
    return a


def triangleType(m1, m2, m3, length1, length2, length3):
    if negativeReciprocal(m1) == m2 or negativeReciprocal(m3) == m2 or negativeReciprocal(m1) == m3:
        print('right triangle')
    elif length1 == length2 or length1 == length3 or length2 == length3:
        if m1 and m2 == m3 and length1 and length2 == length3:
            print('equilateral')
        else:
            print('isoscele')
    else:
        print('scalene')


def threeSlopes(x1, y1, x2, y2, x3, y3):
    a = x2 - x1
    b = y2 - y1
    # a and b are placeholder
    if a != 0:
        slope_1 = b/a
        Yintercept_1 = (slope_1 * x3 - y3) * -1
        print('y = {}x + {}'.format(slope_1, Yintercept_1))
    else:
        print('undefined')
    #find negative reciprocal, slope, y intercept
    #then repeat for all 3 altitudes

    a = x3 - x2
    b = y3 - y2
    if a != 0:
        slope_2 = b/a
        Yintercept_2 = (slope_2 * x1 - y1) * -1
        print('y = {}x + {}'.format(slope_2, Yintercept_2))
    else:
        print('undefined')

    a = x1 - x3
    b = y1 - y3
    if a != 0:
        slope_3 = b/a
        Yintercept_3 = (slope_3 * x2 - y2) * -1
        print('y = {}x + {}'.format(slope_3, Yintercept_3))
    else:
        print('undefined')


def Yintercept(x, y, slope):
    b = -1 * slope * x + y
    print('y-intercept = {}'.format(b))
