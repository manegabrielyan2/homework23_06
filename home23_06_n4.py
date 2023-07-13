#area
import math
def calculate_area(r):
    p = math.pi
    area = p * r**2
    return area
r = 5
c = calculate_area(r)
print(f"Area of circle with radius {r} is {c}")
