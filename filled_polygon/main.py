import ctypes

import sdl2.ext
import sys
from sdl2 import *
from sdl2.examples.pixelaccess import BLACK

from filled_polygon.figure import Figure
from filled_polygon.graphics import draw_line, Point, draw_polygon

selected_figure_index = None


def clear(surface):
    sdl2.ext.fill(surface, BLACK)


def main():
    global selected_figure_index

    sdl2.ext.init()
    window = sdl2.ext.Window("Filled polygon", size=(640, 480))
    window.show()

    window_surface = window.get_surface()
    pixels = sdl2.ext.PixelView(window_surface)

    figures = [
        Figure([
            Point(100, 0),
            Point(200, 0),
            Point(200, 100),
            Point(100, 100)
        ], sdl2.ext.Color(255, 116, 113, 255), pixels, z_index=2),
        Figure([
            Point(0, 200),
            Point(200, 200),
            Point(100, 0)
        ], sdl2.ext.Color(120, 116, 113, 255), pixels, z_index=1)
    ]
    figures.sort(key=lambda f: f.z_index)

    running = True
    old_x = ctypes.c_int32(0)
    old_y = ctypes.c_int32(0)

    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                selected_figure_index = 0
                SDL_GetMouseState(ctypes.byref(old_x), ctypes.byref(old_y))
                for i in range(len(figures)):
                    if figures[i].is_point_inside(Point(old_x.value, old_y.value)):
                        selected_figure_index = i
                        break

            if event.type == sdl2.SDL_MOUSEBUTTONUP:
                selected_figure_index = None

            if event.type == sdl2.SDL_MOUSEMOTION:
                if selected_figure_index is not None:
                    x = ctypes.c_int32(0)
                    y = ctypes.c_int32(0)
                    SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))
                    dx = x.value - old_x.value
                    dy = y.value - old_y.value
                    old_x = x
                    old_y = y
                    figures[selected_figure_index].move(dx, dy)

        clear(window_surface)

        for figure in figures:
            figure.draw()

        window.refresh()
    sdl2.ext.quit()
    return 0


if __name__ == "__main__":
    sys.exit(main())