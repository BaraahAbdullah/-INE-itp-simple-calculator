def add(x, y):
     """Return the sum of x and y"""
    return x + y


def subtract(x, y):
    """Return the difference between x and y."""
    return x - y


def divide(x, y):
     """Return the result of dividing x by y.
    If y is 0, return a warning message instead.
    """
    if y == 0:
        return "Invalid value for denominator, can't divide by 0!"
    return x / y


def multiply(x, y):
     """Return the product of x and y."""
    return x * y


def square(x):
     """Return the square of x."""
    return x ** 2


def power(x, y):
     """Return x raised to the power of y."""
    return x ** y


def sqrt(x):
    """Return the square root of x.
    If x is negative, return a warning message instead.
    """
    if x < 0:
        return "Invalid value for square root, can't take the square root of a negative number!"
    return math.sqrt(x)


