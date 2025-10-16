

def triangle_area(a, b ,c):
    """Calculates the area of a triangle given three points."""
    return abs((a[0] * (b[1] - c[1]) +
                b[0] * (c[1] - a[1]) +
                c[0] * (a[1] - b[1])) / 2)

def point_in_triangle(a, b ,c, eps=1e-9):
    """Returns True if the origin (0, 0) lies inside the triangle."""
    origin = (0, 0)
    total_area = triangle_area(a, b, c)
    sub_areas = [triangle_area(origin, b, c),
                triangle_area(a, origin, c),
                triangle_area(a, b, origin)]

    return abs(total_area - sum(sub_areas)) < eps
