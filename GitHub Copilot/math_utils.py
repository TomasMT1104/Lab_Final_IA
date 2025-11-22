"""
math_utils.py

A small, robust mathematics utility library with input validation,
clear error types, and helpful utility functions for common numeric tasks.

Features:
- Basic arithmetic with validation
- Safe division with optional non-raising behavior
- Power and square root (with optional complex results)
- Factorial with explicit integer checks
- gcd and lcm for multiple integers
- Primality test
- Basic descriptive statistics (mean, median, mode, variance, stddev)
- Utility helpers: clamp, approx_equal

Requires Python 3.8+ for statistics.multimode (falls back to custom implementation when necessary).
"""

from __future__ import annotations

import math
import statistics
from numbers import Number
from typing import Iterable, List, Union, Sequence

# Exceptions


class MathError(Exception):
    """Base class for math_utils exceptions."""


class NonIntegerError(MathError):
    """Raised when an integer value is required but a non-integer is provided."""


class NegativeFactorialError(MathError):
    """Raised when factorial is requested for a negative integer."""


# Type aliases
Numeric = Union[int, float, complex]


# Helper validators


def _ensure_number(x: object, name: str = "value") -> Number:
    if not isinstance(x, Number):
        raise TypeError(f"{name} must be a number (int, float, complex); got {type(x).__name__}")
    return x


def _ensure_iterable_numbers(data: Iterable, name: str = "data") -> List[Number]:
    try:
        seq = list(data)
    except TypeError:
        raise TypeError(f"{name} must be an iterable of numbers")
    if not seq:
        raise ValueError(f"{name} must not be empty")
    for i, v in enumerate(seq):
        if not isinstance(v, Number):
            raise TypeError(f"element {i} of {name} is not a number (got {type(v).__name__})")
    return seq


# Arithmetic


def add(a: Numeric, b: Numeric) -> Numeric:
    """Return a + b after validating inputs are numbers."""
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a + b


def subtract(a: Numeric, b: Numeric) -> Numeric:
    """Return a - b after validating inputs are numbers."""
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a - b


def multiply(a: Numeric, b: Numeric) -> Numeric:
    """Return a * b after validating inputs are numbers."""
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a * b


def divide(a: Numeric, b: Numeric, *, raise_on_zero: bool = True) -> float:
    """
    Divide a by b as floating-point.

    Parameters:
    - raise_on_zero: if True (default), division by zero raises ZeroDivisionError.
                     if False, returns math.copysign(math.inf, a) for zero denominator.

    Raises:
    - ZeroDivisionError when b == 0 and raise_on_zero is True
    - TypeError when inputs are not numeric
    """
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    if b == 0:
        if raise_on_zero:
            raise ZeroDivisionError("division by zero")
        return math.copysign(math.inf, a)
    return a / b


def power(a: Numeric, b: Numeric) -> Numeric:
    """Return a ** b with basic validation. Let Python handle domain errors."""
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a ** b


def sqrt(x: Numeric, *, allow_complex: bool = False) -> Numeric:
    """
    Compute the square root.

    - If x is negative and allow_complex is False, raises ValueError.
    - If allow_complex is True, returns a complex result for negative inputs.
    """
    _ensure_number(x, "x")
    if isinstance(x, complex):
        return complex(x) ** 0.5
    if x < 0:
        if not allow_complex:
            raise ValueError("cannot compute real square root of negative number")
        return complex(x) ** 0.5
    return math.sqrt(x)


# Integer / number-theoretic utilities


def factorial(n: int) -> int:
    """
    Return n! for non-negative integers.

    Raises:
    - NonIntegerError if n is not an int
    - NegativeFactorialError if n < 0
    """
    if not isinstance(n, int):
        raise NonIntegerError("factorial requires an integer input")
    if n < 0:
        raise NegativeFactorialError("factorial is not defined for negative integers")
    # Use math.factorial for speed and correctness
    return math.factorial(n)


def gcd(*args: int) -> int:
    """
    Compute the greatest common divisor of one or more integers.

    Raises:
    - ValueError if no arguments supplied
    - TypeError if any argument is not an int
    """
    if not args:
        raise ValueError("gcd requires at least one integer argument")
    for x in args:
        if not isinstance(x, int):
            raise TypeError("gcd requires integer arguments")
    result = abs(args[0])
    for x in args[1:]:
        result = math.gcd(result, abs(x))
    return result


def lcm(*args: int) -> int:
    """
    Compute the least common multiple of one or more integers.

    Raises:
    - ValueError if no arguments supplied
    - TypeError if any argument is not an int
    """
    if not args:
        raise ValueError("lcm requires at least one integer argument")
    for x in args:
        if not isinstance(x, int):
            raise TypeError("lcm requires integer arguments")
    def _lcm2(a: int, b: int) -> int:
        if a == 0 or b == 0:
            return 0
        return abs(a // math.gcd(a, b) * b)
    result = abs(args[0])
    for x in args[1:]:
        result = _lcm2(result, x)
    return result


def is_prime(n: int) -> bool:
    """
    Determine whether n is a prime number.

    - Works for integers (negative, 0, 1 are not prime).
    - Uses simple deterministic trial division which is efficient for small-medium integers.
    """
    if not isinstance(n, int):
        raise TypeError("is_prime requires an integer input")
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    # trial division up to sqrt(n)
    limit = int(math.isqrt(n))
    i = 3
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True


# Statistics


def mean(data: Iterable[Number]) -> float:
    """Return arithmetic mean of data (non-empty)."""
    seq = _ensure_iterable_numbers(data, "data")
    return statistics.mean(seq)


def median(data: Iterable[Number]) -> float:
    """Return median of data (non-empty)."""
    seq = _ensure_iterable_numbers(data, "data")
    return statistics.median(seq)


def mode(data: Iterable[Number]) -> Union[Number, List[Number]]:
    """
    Return the mode of the data.
    - If there's a single mode, return that element.
    - If multiple modes exist, return a list of modes sorted in ascending order.
    """
    seq = _ensure_iterable_numbers(data, "data")
    # statistics.multimode available in Python 3.8+
    try:
        modes = statistics.multimode(seq)
    except AttributeError:
        # Fallback: compute frequencies manually
        freq = {}
        for x in seq:
            freq[x] = freq.get(x, 0) + 1
        max_count = max(freq.values())
        modes = sorted([k for k, v in freq.items() if v == max_count])
    if not modes:
        raise ValueError("mode: no modes found")
    if len(modes) == 1:
        return modes[0]
    return modes


def variance(data: Iterable[Number], *, population: bool = False) -> float:
    """
    Return variance of data.
    - population=False (default) computes sample variance (raises if less than 2 samples)
    - population=True computes population variance
    """
    seq = _ensure_iterable_numbers(data, "data")
    if population:
        return statistics.pvariance(seq)
    return statistics.variance(seq)


def stddev(data: Iterable[Number], *, population: bool = False) -> float:
    """
    Return standard deviation of data.
    - population=False (default) computes sample stddev
    - population=True computes population stddev
    """
    seq = _ensure_iterable_numbers(data, "data")
    if population:
        return statistics.pstdev(seq)
    return statistics.stdev(seq)


# Utilities


def clamp(x: Number, low: Number, high: Number) -> Number:
    """
    Clamp x to the interval [low, high].

    Raises:
    - ValueError if low > high
    - TypeError if any argument is not numeric
    """
    _ensure_number(x, "x")
    _ensure_number(low, "low")
    _ensure_number(high, "high")
    if low > high:
        raise ValueError("low must be <= high")
    return max(low, min(high, x))


def approx_equal(a: Number, b: Number, *, rel_tol: float = 1e-9, abs_tol: float = 0.0) -> bool:
    """Return True if a and b are close in value according to math.isclose."""
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)


__all__ = [
    "MathError",
    "NonIntegerError",
    "NegativeFactorialError",
    "add",
    "subtract",
    "multiply",
    "divide",
    "power",
    "sqrt",
    "factorial",
    "gcd",
    "lcm",
    "is_prime",
    "mean",
    "median",
    "mode",
    "variance",
    "stddev",
    "clamp",
    "approx_equal",
]