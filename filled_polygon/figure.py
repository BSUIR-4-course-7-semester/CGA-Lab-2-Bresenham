from bresenham.graphics import Point
from filled_polygon.graphics import draw_polygon, get_pixel
import sdl2.ext


class Figure:
    def __init__(self, points, color, pixels=None, filled=True, z_index=None):
        self._points = points
        self.color = color
        self._filled = filled
        self.z_index = z_index
        self._pixels = pixels

    def draw(self):
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
        self._points = list(map(lambda p: Point(p.x + dx, p.y + dy), self._points))