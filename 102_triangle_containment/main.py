"""
This script reads a list of triangles from the file '0102_triangles.txt'
and counts how many of them contain the origin point (0, 0).

Each line in the file must contain six comma-separated numbers:
x1,y1,x2,y2,x3,y3
"""

from helpers import point_in_triangle


triangles = []
with open("0102_triangles.txt", "r") as file:
    for line in file:
        coords = list(map(float, line.strip().split(",")))
        triangle = tuple((coords[i], coords[i + 1]) for i in range(0, 6, 2))
        triangles.append(triangle)

count_inside = sum(point_in_triangle(*triangle) for triangle in triangles)

print(count_inside)
