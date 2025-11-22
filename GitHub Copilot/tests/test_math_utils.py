import math
import pytest
from math_utils import (
    add,
    subtract,
    multiply,
    divide,
    power,
    sqrt,
    factorial,
    gcd,
    lcm,
    is_prime,
    mean,
    median,
    mode,
    variance,
    stddev,
    clamp,
    approx_equal,
    NonIntegerError,
    NegativeFactorialError,
)


def test_basic_arithmetic():
    assert add(2, 3) == 5
    assert subtract(5, 2) == 3
    assert multiply(3, 4) == 12
    assert power(2, 3) == 8
    assert power(9, 0.5) == 3.0


def test_divide_behaviour():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    # non-raising mode returns signed infinity
    assert math.isinf(divide(1, 0, raise_on_zero=False))
    assert math.isinf(divide(-1, 0, raise_on_zero=False)) and divide(-1, 0, raise_on_zero=False) < 0


def test_sqrt():
    assert sqrt(4) == 2.0
    with pytest.raises(ValueError):
        sqrt(-1)
    c = sqrt(-1, allow_complex=True)
    assert isinstance(c, complex)


def test_factorial_and_errors():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(NonIntegerError):
        factorial(3.5)
    with pytest.raises(NegativeFactorialError):
        factorial(-2)


def test_gcd_lcm():
    assert gcd(12, 18) == 6
    assert gcd(7) == 7
    assert lcm(4, 6) == 12
    assert lcm(0, 5) == 0
    assert lcm(7) == 7


def test_is_prime():
    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(13)
    assert not is_prime(15)
    with pytest.raises(TypeError):
        is_prime(2.5)


def test_statistics_basic():
    data = [1, 2, 2, 3, 4]
    assert mean(data) == pytest.approx(2.4)
    assert median([1, 3, 2]) == 2
    # mode returns single value when unique
    assert mode(data) == 2
    # multimode case returns list (sorted)
    assert mode([1, 1, 2, 2]) == [1, 2]
    assert variance([1, 2, 3, 4]) == pytest.approx(1.6666666666666667)  # sample variance
    assert variance([1, 2, 3, 4], population=True) == pytest.approx(1.25)
    assert stddev([1, 2, 3, 4]) == pytest.approx(math.sqrt(1.6666666666666667))


def test_clamp_and_approx():
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0
    assert clamp(20, 0, 10) == 10
    with pytest.raises(ValueError):
        clamp(1, 5, 4)
    assert approx_equal(1.0000000001, 1.0)
    assert not approx_equal(1.1, 1.0, rel_tol=1e-4)


def test_input_validation_errors():
    with pytest.raises(TypeError):
        add("a", 2)
    with pytest.raises(TypeError):
        mean("not iterable")
    with pytest.raises(ValueError):
        # mean of empty sequence should raise
        mean([])