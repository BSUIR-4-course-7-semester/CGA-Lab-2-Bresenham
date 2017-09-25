from bresenham.graphics import Point
from filled_polygon.graphics import draw_polygon, get_pixel
import sdl2.ext
import numpy as np
from math import cos, sin, radians


def move_point(point, dx, dy):
    return Point(point.x + dx, point.y + dy)


def rotate_point(point, angle):
    result_matr = np.matmul(
        [
            point.x,
            point.y
        ], [
            [cos(radians(angle)), -sin(radians(angle))],
            [sin(radians(angle)), cos(radians(angle))]
        ]
    )
    return Point(int(result_matr[0]), int(result_matr[1]))


class Figure:
    def __init__(self, points, color, pixels=None, filled=True, z_index=None):
        self._init_points = points
        self._points = points
        self.color = color
        self._filled = filled
        self.z_index = z_index
        self._pixels = pixels
        self._dx = 0
        self._dy = 0
        self._angle = 0

    def draw(self):
        self._points = list(map(lambda p: rotate_point(p, self._angle), self._init_points))
        self._points = list(map(lambda p: move_point(p, self._dx, self._dy), self._points))
        draw_polygon(self._pixels, self._points, self.color, self._filled)

    def is_point_inside(self, point):
        x = point.x
        count = 0
        target_color = self.color
        while x < 640:
            pixel_color = sdl2.ext.argb_to_color(get_pixel(self._pixels, Point(x, point.y)))
            if target_color.r == pixel_color.r and target_color.g == pixel_color.g and target_color.b == pixel_color.b:
                count += 1
            x += 1
        return True if count % 2 == 1 else False

    def move(self, dx, dy):
        self._dx += dx
        self._dy += dy

    def rotate(self, angle):
        self._angle += angle