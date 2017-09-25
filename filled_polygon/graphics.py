import sdl2.ext
from sdl2 import SDL_Point
import time


class Point(SDL_Point):
    def __add__(self, value):
        return Point(self.x + value.x, self.y + value.y)


def fill(pixels, point, color):
    if point.x >= 640 or point.x < 0:
        return
    if point.y >= 480 or point.y < 0:
        return

    points = [point]

    while len(points) != 0:
        point = points.pop()
        # if get_pixel(pixels, point) != int(color):
        if get_pixel(pixels, point) == 0:
            put_pixel(pixels, point, color)
        else:
            continue
        points.append(Point(point.x + 1, point.y))
        points.append(Point(point.x - 1, point.y))
        points.append(Point(point.x, point.y + 1))
        points.append(Point(point.x, point.y - 1))


def draw_polygon(pixels, points, color, filled=False):
    point_count = len(points)
    for i in range(point_count):
        draw_line(pixels, points[i], points[(i + 1) % point_count], color)
    # if filled:
    #     center = Point(
    #         round(sum([point.x for point in points]) / len(points)),
    #         round(sum([point.y for point in points]) / len(points))
    #     )
    #     try:
    #         fill(pixels, center, color)
    #     except Exception as e:
    #         pass


def normalize_point(point):
    return Point(
        639 if point.x >= 640 else 0 if point.x < 0 else point.x,
        479 if point.y >= 480 else 0 if point.y < 0 else point.y,
    )


def get_pixel(pixels, point):
    point = normalize_point(point)
    return pixels[point.y][point.x]


def put_pixel(pixels, point, color):
    point = normalize_point(point)
    if point.y >= 480:
        print()
    pixels[point.y][point.x] = color


def draw_line(pixels, point_a, point_b, color):
    dx = abs(point_a.x - point_b.x)
    dy = abs(point_a.y - point_b.y)

    sx = 1 if point_b.x >= point_a.x else -1
    sy = 1 if point_b.y >= point_a.y else -1

    if dy <= dx:
        d = dy * 2 - dx
        d1 = dy * 2
        d2 = (dy - dx) * 2

        put_pixel(pixels, point_a, color)
        x = point_a.x + sx
        y = point_a.y
        for i in range(1, dx + 1):
            if d > 0:
                d += d2
                y += sy
            else:
                d += d1

            put_pixel(pixels, Point(x, y), color)
            x += sx
    else:
        d = dx * 2 - dy
        d1 = dx * 2
        d2 = (dx - dy) * 2

        put_pixel(pixels, point_a, color)
        x = point_a.x
        y = point_a.y + sy
        for i in range(1, dy + 1):
            if d > 0:
                d += d2
                x += sx
            else:
                d += d1

            put_pixel(pixels, Point(x, y), color)
            y += sy


def draw_circle(pixels, point, radius, color):
    x = 0
    y = radius
    delta = 1 - 2 * radius
    err = 0

    while y >= 0:
        put_pixel(pixels, point + SDL_Point(x, y), color)
        put_pixel(pixels, point + SDL_Point(x, -y), color)
        put_pixel(pixels, point + SDL_Point(-x, y), color)
        put_pixel(pixels, point + SDL_Point(-x, -y), color)
        err = 2 * (delta + y) - 1

        if delta < 0 and err <= 0:
            x += 1
            delta += 2 * x + 1
            continue
        else:
            err = 2 * (delta - x) - 1
            if delta > 0 and err > 0:
                y -= 1
                delta += 1 - 2 * y
            else:
                x += 1
                delta += 2 * (x - y)
                y -= 1
