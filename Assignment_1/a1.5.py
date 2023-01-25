import math


def area(radius):
    return math.pi * (radius ** 2)  # calculate area


def circ(radius):
    return math.pi * radius * 2  # calculate circumference


if __name__ == "__main__":
    radius = 30

    _area_of_circle_ = area(radius)  # get area
    _circum_of_circle_ = circ(radius)  # get circum

    # output
    print(f"Area of circle with radius of {radius}: {_area_of_circle_:.2f}",
          f"\nCircumference of a circle with radius of {radius}: {_circum_of_circle_:.2f}\n")

    radius = float(input("Enter new radius: "))  # get radius from user

    _area_of_circle_ = area(radius)  # get area
    _circum_of_circle_ = circ(radius)  # get circum

    # output
    print(f"Area of circle with radius of {radius}: {_area_of_circle_:.2f}",
          f"\nCircumference of a circle with radius of {radius}: {_circum_of_circle_:.2f}\n")
