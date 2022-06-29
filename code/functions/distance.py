import math

def distance(a, b):
    """
    Calculate distance between two points with Pythagorean theorem.
    """
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)
