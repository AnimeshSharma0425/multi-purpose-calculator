"""Calculator logic: the same formulas and checks as original_console.py.

The console version prints its answers. A web API needs the answers returned
instead, so each function here returns the value and raises CalcError with the
same message the console version prints when an input is not allowed.
"""


class CalcError(Exception):
    pass


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    raise CalcError("Cannot divide by zero")


def floor(a, b):
    if b != 0:
        return a // b
    raise CalcError("Cannot divide by zero")


def power(a, b):
    return a ** b


def area_square(s):
    return s * s


def parameter_square(s):
    return 4 * s


def area_rectangle(a, b):
    return a * b


def parameter_rectangle(a, b):
    return 2 * (a + b)


def area_circle(r):
    if r >= 0:
        return 3.14 * (r ** 2)
    raise CalcError("Radius cannot be negative")


def circumference(r):
    if r >= 0:
        return 2 * 3.14 * r
    raise CalcError("Radius cannot be negative")


def area_triangle(a, b):
    return 1 / 2 * (a * b)


def parameter_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return a + b + c
    raise CalcError("Invalid triangle sides")


def area_cone(r, l):
    if r > 0 and l >= r:
        return (3.14 * r * r) + (3.14 * r * l)
    raise CalcError("Invalid radius or slant height")


def area_cube(s):
    if s >= 0:
        return 6 * s * s
    raise CalcError("Side cannot be negative")


def area_cuboid(a, b, c):
    if a >= 0 and b >= 0 and c >= 0:
        return 2 * ((a * b) + (b * c) + (a * c))
    raise CalcError("Dimensions cannot be negative")


EXIT_MESSAGE = "Thank you for using Multi-Purpose Calculator!"
INVALID_CHOICE = "Invalid choice! Please enter a number from 1 to 18"

NUM = "Enter a number"

# (condition number, name, input labels, function) - same order as the console menu
OPERATIONS = [
    (1, "Add", [NUM, NUM], add),
    (2, "Subtract", [NUM, NUM], subtract),
    (3, "Multiply", [NUM, NUM], multiply),
    (4, "Divide", [NUM, NUM], divide),
    (5, "Floor division", [NUM, NUM], floor),
    (6, "Power", [NUM, NUM], power),
    (7, "Area of square", ["Enter the side"], area_square),
    (8, "Perimeter of square", ["Enter the side"], parameter_square),
    (9, "Area of rectangle", ["Enter the length", "Enter the breadth"], area_rectangle),
    (10, "Perimeter of rectangle", ["Enter the length", "Enter the breadth"], parameter_rectangle),
    (11, "Area of circle", ["Enter the radius"], area_circle),
    (12, "Circumference of circle", ["Enter the radius"], circumference),
    (13, "Area of triangle", ["Enter the base", "Enter the height"], area_triangle),
    (14, "Perimeter of triangle",
     ["Enter the first side", "Enter the second side", "Enter the third side"], parameter_triangle),
    (15, "Total surface area of cone", ["Enter the radius", "Enter the slant height"], area_cone),
    (16, "Surface area of cube", ["Enter the side"], area_cube),
    (17, "Surface area of cuboid",
     ["Enter the length", "Enter the breadth", "Enter the height"], area_cuboid),
    (18, "Exit", [], None),
]

BY_CONDITION = {op[0]: op for op in OPERATIONS}


def run(condition, values):
    """Run one menu option and return the answer exactly as the console prints it."""
    op = BY_CONDITION.get(condition)
    if op is None:
        raise CalcError(INVALID_CHOICE)
    _, _, labels, func = op
    if func is None:
        return EXIT_MESSAGE
    if len(values) != len(labels):
        raise CalcError(f"This option needs {len(labels)} value(s)")
    try:
        return str(func(*values))
    except CalcError:
        raise
    except ArithmeticError:
        raise CalcError("The result is too large or not defined")
