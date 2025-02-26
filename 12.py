def get_distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# def point_line_distance(x: int, y: int, xa: int, ya: int, xb: int, yb: int) -> float:
#     A = yb - ya
#     B = xa - xb
#     C = ya * xb - xa * yb
#     res: float = abs(A * x + B * y + C) / ((A ** 2 + B ** 2) ** 0.5)
#     return res
#
# def get_triangle_square(x1: int, y1: int, x2: int, y2: int, height: float) -> float:
#     return height * get_distance(x1, y1, x2, y2) / 2

def get_triangle_square_by_vertices(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> float:
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2


def get_square(x1: int, y1: int,x2: int, y2: int, x3: int, y3: int,x4: int, y4: int) -> float:
    return get_distance(x1, y1, x2, y2) * get_distance(x2, y2, x3, y3)

def is_inside(x: int, y: int, x1: int, y1: int,x2: int, y2: int, x3: int, y3: int,x4: int, y4: int) -> bool:
    square_by_dot_1 = get_triangle_square_by_vertices(x, y, x1, y1, x2, y2)
    square_by_dot_2 = get_triangle_square_by_vertices(x, y, x2, y2, x3, y3)
    square_by_dot_3 = get_triangle_square_by_vertices(x, y, x3, y3, x4, y4)
    square_by_dot_4 = get_triangle_square_by_vertices(x, y, x4, y4, x1, y1)
    square_by_dot = sum((square_by_dot_1, square_by_dot_2, square_by_dot_3, square_by_dot_4))
    square_by_formula = get_square(x1, y1, x2, y2, x3, y3, x4, y4)
    return abs(square_by_dot - square_by_formula) <= 0.001


counter = 0
x = int(input())
for i in range(x):
    x, y, x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    if is_inside(x, y, x1, y1, x2, y2, x3, y3, x4, y4):
        counter += 1
print(counter)
