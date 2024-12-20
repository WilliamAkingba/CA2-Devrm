"""A simple Python calculator module for basic math functions."""

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference between a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the quotient of a divided by b.

    Raises:
        ValueError: If the divisor (b) is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Make sure to add a newline at the end of the file.



