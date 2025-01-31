import math

def calculate_perimeter(shape, *args):
    """Calculates the perimeter of various shapes.

    Args:
        shape: The name of the shape (e.g., "triangle", "rectangle", "square", "circle").
        *args: The dimensions of the shape (e.g., sides for a triangle, length and width for a rectangle).

    Returns:
        The perimeter of the shape, or an error message if the input is invalid.
    """
    if shape == "triangle":
        if len(args) != 3:
            return "Triangle requires 3 sides."
        a, b, c = args
        if a + b <= c or a + c <= b or b + c <= a: #triangle inequality theorem
            return "Invalid triangle sides. The sum of any two sides must be greater than the third side."
        return a + b + c
    elif shape == "rectangle":
        if len(args) != 2:
            return "Rectangle requires length and width."
        length, width = args
        return 2 * (length + width)
    elif shape == "square":
        if len(args) != 1:
            return "Square requires one side."
        side = args[0]
        return 4 * side
    elif shape == "circle":
        if len(args) != 1:
            return "Circle requires radius."
        radius = args[0]
        return 2 * math.pi * radius
    else:
        return "Invalid shape."


def calculate_area(shape, *args):
    """Calculates the area of various shapes.

    Args:
        shape: The name of the shape.
        *args: The dimensions of the shape.

    Returns:
        The area of the shape, or an error message if the input is invalid.
    """
    if shape == "triangle":
        if len(args) != 3:
            return "Triangle requires 3 sides (Heron's formula)."
        a, b, c = args
        if a + b <= c or a + c <= b or b + c <= a: #triangle inequality theorem
            return "Invalid triangle sides. The sum of any two sides must be greater than the third side."
        s = (a + b + c) / 2  # Semi-perimeter
        return math.sqrt(s * (s - a) * (s - b) * (s - c))  # Heron's formula
    elif shape == "rectangle":
        if len(args) != 2:
            return "Rectangle requires length and width."
        length, width = args
        return length * width
    elif shape == "square":
        if len(args) != 1:
            return "Square requires one side."
        side = args[0]
        return side * side
    elif shape == "circle":
        if len(args) != 1:
            return "Circle requires radius."
        radius = args[0]
        return math.pi * radius * radius
    else:
        return "Invalid shape."


# Example usage:
print(calculate_perimeter("triangle", 3, 4, 5))  # Output: 12
print(calculate_area("triangle", 3, 4, 5))  # Output: 6.0

print(calculate_perimeter("rectangle", 5, 10))  # Output: 30
print(calculate_area("rectangle", 5, 10))  # Output: 50

print(calculate_perimeter("square", 7))  # Output: 28
print(calculate_area("square", 7))  # Output: 49

print(calculate_perimeter("circle", 4))  # Output: 25.132741228718345
print(calculate_area("circle", 4))  # Output: 50.26548245743669

print(calculate_perimeter("triangle", 1, 2, 5)) # Output: Invalid triangle sides. The sum of any two sides must be greater than the third side.
print(calculate_area("triangle", 1, 2, 5)) # Output: Invalid triangle sides. The sum of any two sides must be greater than the third side.

print(calculate_perimeter("pentagon", 5))  # Output: Invalid shape.
print(calculate_area("pentagon", 5))  # Output: Invalid shape.