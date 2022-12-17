from general import *
import pytest
import grafics


@pytest.mark.parametrize("name_func",
                         [
                            left_rectangle_method,
                            right_rectangle_method,
                            average_rectangle_method,
                            trapezoid_method,
                            simpsons_formula
                         ]
                         )
@pytest.mark.parametrize("func, primitive",
                         [
                             (lambda x: x, lambda x: x**2/2),
                             (lambda x: x**2, lambda x: x**3/3),
                             (lambda x: x**3, lambda x: x**4/4),
                             (lambda x: 3, lambda x: 3*x),
                             (lambda x: 3**x, lambda x: (3**x)/log(3, e)),
                             (lambda x: e**x, lambda x: e**x),
                             (lambda x: sin(x), lambda x: -cos(x)),
                             (lambda x: cos(x), lambda x: sin(x))
                         ]
                         )
@pytest.mark.parametrize("a, b, n",
                         [
                             (-1, 1, 1_000_000),
                             (-1, 3, 1_000_000),
                             (2, 5, 1_000_000),
                             (-3, 2, 1_000_000),
                             (-3, 5, 1_000_000)
                         ]
                         )
def test_integral(name_func, primitive, func, a, b, n):
    res = name_func(func, a, b, n)
    res_analytic = primitive(b) - primitive(a)
    assert res_analytic == pytest.approx(res, abs=1e-3)


@pytest.mark.parametrize("name_func",
                         [
                            left_rectangle_method,
                            right_rectangle_method,
                            average_rectangle_method,
                            monte_carlo,
                            trapezoid_method
                         ]
                         )
@pytest.mark.parametrize("func, primitive",
                         [
                             (lambda x: x**2, lambda x: x**3/3),
                             (lambda x: x**3, lambda x: x**4/4),
                             (lambda x: sin(x), lambda x: -cos(x)),
                             (lambda x: cos(x), lambda x: sin(x)),
                             (lambda x: 1/x, lambda x: log(abs(x), e))
                         ]
                         )
@pytest.mark.parametrize("a, b, n",
                         [
                             (-1000, 20000, 10),
                             (-2000, 30000, 10),
                             (-12000, 53000, 10),
                             (-30000, 200000, 10),
                             (-300000, 530000, 10)
                         ]
                         )
def test_wrong(name_func, primitive, func, a, b, n):
    res = name_func(func, a, b, n)
    res_analytic = primitive(b) - primitive(a)
    assert res_analytic != pytest.approx(res, abs=1e-6)


@pytest.mark.parametrize("name_func",
                         [
                            left_rectangle_method,
                            right_rectangle_method,
                            average_rectangle_method,
                            trapezoid_method,
                            simpsons_formula
                         ]
                         )
@pytest.mark.parametrize("nums",
                         [
                            1_000,
                            10_000,
                            100_000,
                            1_000_000
                         ]
                         )
def test_calculation(name_func, nums):
    assert 0 == pytest.approx(grafics.calculation(nums, name_func), abs=1e-2)
