#Area Calculator
import math


def paint_area(height, width, cover):
    area=height*width
    num_of_cans=math.ceil(area/cover)
    print(f"You'll need {num_of_cans} cans of paint")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_area(height=test_h, width=test_w, cover=coverage)