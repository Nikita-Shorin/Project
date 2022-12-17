from math import *
from random import uniform


def left_rectangle_method(func, a, b, n=1_000_000):
    """
    calculates the value of a certain integral by the method of left rectangles
    :param func: integrated function
    :param a: lower bound of integration
    :param b: upper bound of integration
    :param n: number of segments
    :return: the value of the integral
    """
    segment = float((b - a)/n)
    x = a
    integral = 0.0
    for _ in range(n):
        integral += func(x) * segment
        x += segment
    return integral


def right_rectangle_method(func, a, b, n=1_000_000):
    """
    calculates the value of a certain integral by the method of right rectangles
    :param func: integrated function
    :param a: lower bound of integration
    :param b: upper bound of integration
    :param n: number of segments
    :return: the value of the integral
    """
    segment = float((b - a) / n)
    x = segment + a
    integral = 0.0
    for _ in range(n):
        integral += func(x) * segment
        x += segment
    return integral


def average_rectangle_method(func, a, b, n=1_000_000):
    """
    calculates the value of a certain integral by the method of average rectangles
    :param func: integrated function
    :param a: lower bound of integration
    :param b: upper bound of integration
    :param n: number of segments
    :return: the value of the integral
    """
    segment = float((b - a) / n)
    x = 0.5 * segment + a
    integral = 0.0
    for _ in range(n):
        integral += func(x) * segment
        x += segment
    return integral


def monte_carlo(func, a, b, n=1_000_000):
    """
    calculates the value of a certain integral by the Monte-Carlo method
    :param func: integrated function
    :param a: lower bound of integration
    :param b: upper bound of integration
    :param n: number of segments
    :return: the value of the integral
    """
    integral = 0.0
    for _ in range(n):
        x = uniform(a, b)
        y = func(x)
        integral += y
    return (b - a)/float(n) * integral


def trapezoid_method(func, a, b, n=1_000_000):
    """
    calculates the value of a certain integral by the trapezoid method
    :param func: integrated function
    :param a: lower bound of integration
    :param b: upper bound of integration
    :param n: number of segments
    :return: the value of the integral
    """
    segment = float((b - a)/n)
    integral = (func(a) + func(b))/2
    for i in range(1, n):
        integral += func(i * segment + a)
    return integral * segment


def simpsons_formula(func, a, b, n=1_000_000):
    """
    calculates the value of a certain integral by the Simpson method
    :param func: integrated function
    :param a: lower bound of integration
    :param b: upper bound of integration
    :param n: number of segments
    :return: the value of the integral
    """
    n += n % 2
    segment = float((b - a)/n)
    summa = 0.0
    for i in range(1, n // 2):
        summa += 4 * func(a + (2 * i + 1) * segment) + 2 * func(a + (2 * i) * segment)
    return (summa + func(a) + 4 * func(a + segment) + func(b)) * segment / 3
