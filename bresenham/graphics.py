from sdl2 import *

# point - SDL_Point
# color - SDL_Color


class Point(SDL_Point):
    def __add__(self, value):
        return Point(self.x + value.x, self.y + value.y)


def put_pixel(renderer, point, color):
    SDL_SetRenderDrawColor(renderer, color.r, color.g, color.b, color.a)
    SDL_RenderDrawPoint(renderer, point.x, point.y)


# Bresenham's algorithm
def draw_line(renderer, point_a, point_b, color):
    dx = abs(point_a.x - point_b.x)
    dy = abs(point_a.y - point_b.y)

    sx = 1 if point_b.x >= point_a.x else -1
    sy = 1 if point_b.y >= point_a.y else -1

    if dy <= dx:
        d = dy * 2 - dx
        d1 = dy * 2
        d2 = (dy - dx) * 2

        put_pixel(renderer, point_a, color)
        x = point_a.x + sx
        y = point_a.y
        for i in range(1, dx + 1):
            if d > 0:
                d += d2
                y += sy
            else:
                d += d1

            put_pixel(renderer, Point(x, y), color)
            x += sx
    else:
        d = dx * 2 - dy
        d1 = dx * 2
        d2 = (dx - dy) * 2

        put_pixel(renderer, point_a, color)
        x = point_a.x
        y = point_a.y + sy
        for i in range(1, dy + 1):
            if d > 0:
                d += d2
                x += sx
            else:
                d += d1

            put_pixel(renderer, Point(x, y), color)
            y += sy


def draw_circle(renderer, point, radius, color):
    x = 0
    y = radius
    delta = 1 - 2 * radius
    err = 0

    while y >= 0:
        put_pixel(renderer, point + SDL_Point(x, y), color)
        put_pixel(renderer, point + SDL_Point(x, -y), color)
        put_pixel(renderer, point + SDL_Point(-x, y), color)
        put_pixel(renderer, point + SDL_Point(-x, -y), color)
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
