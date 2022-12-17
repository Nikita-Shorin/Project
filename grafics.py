from general import *
import numpy as np
import matplotlib.pyplot as plt


primitives = [
                (lambda x: x, lambda x: x**2/2),
                (lambda x: x**2, lambda x: x**3/3),
                (lambda x: x**3, lambda x: x**4/4),
                (lambda x: 3, lambda x: 3*x),
                (lambda x: 3**x, lambda x: (3**x)/log(3, e)),
                (lambda x: e**x, lambda x: e**x),
                (lambda x: sin(x), lambda x: -cos(x)),
                (lambda x: cos(x), lambda x: sin(x))
            ]
functions = [
                left_rectangle_method,
                right_rectangle_method,
                average_rectangle_method,
                monte_carlo,
                trapezoid_method,
                simpsons_formula
            ]
titles = [
                "Метод левых прямоугольников",
                "Метод правых прямоугольников",
                "Метод средних прямоугольников",
                "Метод Монте-Карло",
                "Метод трапеций",
                "Формула Симпсона"
         ]
border = (-5, 7)
num_of_points = np.logspace(2, 6, 11, dtype=int)


def calculation(n, function):
    """
    calculates the value of the relative error
    :param n: number of segments
    :param function: integration method
    :return: relative error
    """
    summa = 0
    for primitive in primitives:
        analytical_sum = primitive[1](border[1]) - primitive[1](border[0])
        experimental_sum = function(primitive[0], border[0], border[1], n)
        summa += abs((experimental_sum - analytical_sum) / analytical_sum)
    return summa / len(primitives)


def draw():
    """
    draws graphs of relative errors from the number of segments
    :return: None
    """
    plt.figure(figsize=(15, 10))
    tmp = np.vectorize(calculation)
    for i in range(6):
        delta = tmp(num_of_points, functions[i])
        # https://mmas.github.io/least-squares-fitting-numpy-scipy
        a = np.vstack([np.log(num_of_points), np.ones(len(np.log(num_of_points)))]).T
        coefficients = np.linalg.lstsq(a, np.log(delta), rcond=None)[0]
        #
        plt.subplot(2, 3, i + 1)
        plt.tight_layout()
        plt.scatter([num_of_points[0]], [delta[0]], 0, label=f'k={coefficients[0]}')
        plt.scatter([num_of_points[0]], [delta[0]], 0, label=f'b={coefficients[1]}')
        plt.loglog(num_of_points, delta, 'or')
        plt.loglog([num_of_points[0], num_of_points[-1]],
                   np.exp([coefficients[0] * np.log(num_of_points[0]) + coefficients[1],
                           coefficients[0] * np.log(num_of_points[-1]) + coefficients[1]]),
                   '-b', label='Апрокс. прямая')
        plt.ylabel("Относительная погрешность")
        plt.xlabel("Кол-во разбиений")
        plt.title(titles[i])
        plt.grid()
        plt.legend()
    plt.show()


if __name__ == "__main__":
    draw()
