```markdown
# math_utils

A robust, well-typed mathematics utilities module.

This project provides a compact set of numeric utilities with:
- PEP 484 type annotations (good for static analysis with mypy/pyright).
- Runtime input validation and explicit custom exceptions.
- Clear, consistent API for small numeric tasks.

Key features
- Basic arithmetic: add, subtract, multiply, divide (safe division with optional non-raising behavior).
- Power and sqrt (optionally returns complex results).
- Factorial with strict integer and non-negative checks.
- gcd and lcm for multiple integers.
- Simple deterministic primality test suitable for small-to-medium integers.
- Descriptive statistics: mean, median, mode (always returns a list), variance, stddev.
- Small helpers: clamp and approx_equal.

Exceptions
- MathError: base class for module exceptions.
- InvalidTypeError: input type mismatch (subclasses TypeError).
- EmptyDataError: operation requires a non-empty collection.
- NonIntegerError: an integer was required but not supplied.
- NegativeFactorialError: factorial requested for a negative integer.
- DivisionByZeroError: a ZeroDivisionError subclass raised by divide when requested.

Usage
- Import what you need:
  from math_utils import divide, factorial, mean

- Static typing:
  The module includes type annotations; run mypy/pyright for static checks.

Testing
- Uses pytest for unit tests.
- Install dependencies:
  pip install pytest
- Run tests:
  pytest -q

License
- MIT-style; adapt for your project.

```