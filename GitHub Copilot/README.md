# math_utils

A small, robust mathematics utilities module with input validation, explicit errors, and unit tests.

Features:
- Basic arithmetic functions (add, subtract, multiply, divide)
- Safe division with optional non-raising behavior
- Power and sqrt (optionally returns complex results)
- Factorial with explicit integer and non-negative checks
- GCD / LCM for multiple integers
- Simple primality test (trial division)
- Descriptive statistics: mean, median, mode, variance, stddev
- Utility functions: clamp, approx_equal

Usage:
- Import functions directly: `from math_utils import divide, sqrt, factorial`
- Raise behavior and errors are documented in docstrings.

Running tests:
- Install pytest (pip install pytest)
- Run: `pytest -q`

License: MIT-style (adapt as needed)