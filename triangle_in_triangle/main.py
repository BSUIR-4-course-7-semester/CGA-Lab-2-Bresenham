import ctypes
import sys
from sdl2 import *

from bresenham.graphics import draw_line, Point


def draw_polygon(renderer, points, color):
    point_count = len(points)
    for i in range(point_count):
        draw_line(renderer, points[i], points[(i + 1) % point_count], color)


def calc_new_points(points, µ):
    point_count = len(points)
    pairs = []
    for i in range(point_count):
        pairs.append((points[i], points[(i + 1) % point_count]))

    new_points = []
    for pair in pairs:
        a = pair[0]
        b = pair[1]
        new_x = round(a.x + µ * (b.x - a.x))
        new_y = round(a.y + µ * (b.y - a.y))
        new_points.append(Point(new_x, new_y))

    return new_points


def draw_recursive_polygon(renderer, points, color, µ, depth):
    if depth > 0:
        draw_polygon(renderer, points, color)
        draw_recursive_polygon(renderer, calc_new_points(points, µ), color, µ, depth - 1)


def main():
    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(b"Recursive polygon",
                              SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                              640, 480,
                              SDL_WINDOW_SHOWN)
    window_surface = SDL_GetWindowSurface(window)
    renderer = SDL_CreateRenderer(window, -1, 0)

    draw_recursive_polygon(renderer, [
        SDL_Point(0, 200),
        SDL_Point(200, 200),
        SDL_Point(100, 0),
    ], SDL_Color(255, 255, 113, 255), 0.05, 50)

    SDL_RenderPresent(renderer)

    running = True
    event = SDL_Event()
    while running:
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_QUIT:
                running = False
                break

    SDL_DestroyWindow(window)
    SDL_Quit()
    return 0

if __name__ == "__main__":
    sys.exit(main())