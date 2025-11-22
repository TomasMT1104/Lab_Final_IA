"""
math_utils.py

A robust, well-typed mathematics utilities module.

Highlights
- PEP 484 type annotations throughout to aid static type checking (mypy, Pyright).
- Runtime type checks that raise explicit custom exceptions for clearer error handling.
- Clear, machine- and human-readable docstrings (Google style).
- Small set of commonly-needed numeric utilities: arithmetic, safe division, power, sqrt,
  factorial, gcd/lcm, primality test, descriptive statistics, and helpers.

Design notes
- Numeric inputs are accepted as int, float or complex (the `numbers.Number` ABC is used
  for runtime checks).
- Custom exceptions inherit from MathError so callers can catch a single base class if desired.
- Where appropriate, we preserve Python built-in exception semantics (e.g. DivisionByZeroError
  is a ZeroDivisionError subclass).
"""

from __future__ import annotations

import math
import statistics
from numbers import Number
from typing import Iterable, List, Sequence, Union

# Type alias
Numeric = Union[int, float, complex]


# Exceptions


class MathError(Exception):
    """Base class for all math_utils exceptions."""


class InvalidTypeError(TypeError, MathError):
    """Raised when a function receives an argument of an unexpected type."""


class EmptyDataError(ValueError, MathError):
    """Raised when an operation requires a non-empty collection but received an empty one."""


class NonIntegerError(InvalidTypeError):
    """Raised when an integer is required but a non-integer is provided."""


class NegativeFactorialError(MathError, ValueError):
    """Raised when factorial is requested for a negative integer."""


class DivisionByZeroError(ZeroDivisionError, MathError):
    """Raised specifically for division-by-zero when using math_utils divide routines."""


# Internal validators


def _ensure_number(x: object, name: str = "value") -> Number:
    """Runtime check: ensure x is a numeric type (int, float, complex)."""
    if not isinstance(x, Number):
        raise InvalidTypeError(f"{name} must be a number (int, float, complex); got {type(x).__name__}")
    return x  # type: ignore[return-value]


def _ensure_iterable_numbers(data: Iterable, name: str = "data") -> List[Number]:
    """
    Runtime check: ensure 'data' is an iterable of numbers and not empty.

    Returns:
        A concrete list of numeric elements for further processing.
    """
    try:
        seq = list(data)
    except TypeError:
        raise InvalidTypeError(f"{name} must be an iterable of numbers")
    if len(seq) == 0:
        raise EmptyDataError(f"{name} must not be empty")
    for i, v in enumerate(seq):
        if not isinstance(v, Number):
            raise InvalidTypeError(f"element {i} of {name} is not a number (got {type(v).__name__})")
    return seq  # type: ignore[return-value]


# Arithmetic


def add(a: Numeric, b: Numeric) -> Numeric:
    """Return a + b after validating both operands are numeric."""
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a + b


def subtract(a: Numeric, b: Numeric) -> Numeric:
    """Return a - b after validating both operands are numeric."""
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a - b


def multiply(a: Numeric, b: Numeric) -> Numeric:
    """Return a * b after validating both operands are numeric."""
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a * b


def divide(a: Numeric, b: Numeric, *, raise_on_zero: bool = True) -> float:
    """
    Divide a by b and return a floating-point result.

    Args:
        a: Dividend (numeric).
        b: Divisor (numeric).
        raise_on_zero: When True (default), a zero divisor raises DivisionByZeroError.
                       When False, returns signed infinity like math.copysign(math.inf, a).

    Raises:
        InvalidTypeError: if arguments are not numeric.
        DivisionByZeroError: if b == 0 and raise_on_zero is True.
    """
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    if b == 0:
        if raise_on_zero:
            raise DivisionByZeroError("division by zero")
        return math.copysign(math.inf, a)
    return a / b  # type: ignore[return-value]


def power(a: Numeric, b: Numeric) -> Numeric:
    """Return a ** b after validating numeric inputs. Let Python raise domain errors for invalid exponent combos."""
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a ** b


def sqrt(x: Numeric, *, allow_complex: bool = False) -> Numeric:
    """
    Compute square root.

    Args:
        x: numeric value to take square root of.
        allow_complex: if True, negative inputs produce complex result. If False, negative inputs raise ValueError.

    Raises:
        InvalidTypeError: if x is not numeric.
        ValueError: if x < 0 and allow_complex is False.
    """
    _ensure_number(x, "x")
    if isinstance(x, complex):
        return complex(x) ** 0.5
    # x is real number
    if x < 0:
        if not allow_complex:
            raise ValueError("cannot compute real square root of negative number")
        return complex(x) ** 0.5
    return math.sqrt(x)


# Integer / number-theoretic utilities


def factorial(n: int) -> int:
    """
    Compute factorial of a non-negative integer n.

    Args:
        n: integer >= 0

    Returns:
        n!

    Raises:
        NonIntegerError: if n is not an int.
        NegativeFactorialError: if n < 0.
    """
    if not isinstance(n, int):
        raise NonIntegerError("factorial requires an integer input")
    if n < 0:
        raise NegativeFactorialError("factorial is not defined for negative integers")
    return math.factorial(n)


def gcd(*args: int) -> int:
    """
    Compute greatest common divisor (GCD) of one or more integers.

    Raises:
        InvalidTypeError: if any argument is not an int.
        ValueError: if no arguments provided.
    """
    if not args:
        raise ValueError("gcd requires at least one integer argument")
    for x in args:
        if not isinstance(x, int):
            raise InvalidTypeError("gcd requires integer arguments")
    result = abs(args[0])
    for x in args[1:]:
        result = math.gcd(result, abs(x))
    return result


def lcm(*args: int) -> int:
    """
    Compute least common multiple (LCM) of one or more integers.

    Raises:
        InvalidTypeError: if any argument is not an int.
        ValueError: if no arguments provided.
    """
    if not args:
        raise ValueError("lcm requires at least one integer argument")
    for x in args:
        if not isinstance(x, int):
            raise InvalidTypeError("lcm requires integer arguments")

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
    Determine primality of an integer n.

    Args:
        n: integer to test

    Returns:
        True if n is prime, False otherwise.

    Raises:
        InvalidTypeError: if n is not an int.
    """
    if not isinstance(n, int):
        raise InvalidTypeError("is_prime requires an integer input")
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    i = 3
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True


# Statistics


def mean(data: Iterable[Number]) -> float:
    """
    Arithmetic mean of numeric data.

    Raises:
        InvalidTypeError: if data is not iterable or contains non-numeric items.
        EmptyDataError: if data is empty.
    """
    seq = _ensure_iterable_numbers(data, "data")
    return statistics.mean(seq)


def median(data: Iterable[Number]) -> float:
    """Median of numeric data."""
    seq = _ensure_iterable_numbers(data, "data")
    return statistics.median(seq)


def mode(data: Iterable[Number]) -> List[Number]:
    """
    Return the mode(s) of the data.

    Always returns a list of one or more modes (sorted ascending). This explicit list-based
    result makes the API uniform and easier to type-check.

    Raises:
        InvalidTypeError, EmptyDataError as for other statistics functions.
    """
    seq = _ensure_iterable_numbers(data, "data")
    try:
        modes = statistics.multimode(seq)
    except AttributeError:
        # Fallback for older Python: manual multimode
        freq = {}
        for x in seq:
            freq[x] = freq.get(x, 0) + 1
        max_count = max(freq.values())
        modes = sorted([k for k, v in freq.items() if v == max_count])
    # Ensure a deterministic sorted list is returned
    return sorted(modes)


def variance(data: Iterable[Number], *, population: bool = False) -> float:
    """
    Variance of numeric data.

    Args:
        population: if True compute population variance; otherwise sample variance (requires >= 2 items).
    """
    seq = _ensure_iterable_numbers(data, "data")
    if population:
        return statistics.pvariance(seq)
    return statistics.variance(seq)


def stddev(data: Iterable[Number], *, population: bool = False) -> float:
    """
    Standard deviation of numeric data.

    Args:
        population: if True compute population stddev; otherwise sample stddev.
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
        InvalidTypeError: if any argument is not numeric.
        ValueError: if low > high.
    """
    _ensure_number(x, "x")
    _ensure_number(low, "low")
    _ensure_number(high, "high")
    if low > high:
        raise ValueError("low must be <= high")
    return max(low, min(high, x))


def approx_equal(a: Number, b: Number, *, rel_tol: float = 1e-9, abs_tol: float = 0.0) -> bool:
    """Return True if a and b are close per math.isclose (with runtime type validation)."""
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)


__all__ = [
    "MathError",
    "InvalidTypeError",
    "EmptyDataError",
    "NonIntegerError",
    "NegativeFactorialError",
    "DivisionByZeroError",
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