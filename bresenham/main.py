import sys
import ctypes
from sdl2 import *

from bresenham.graphics import put_pixel, draw_line, draw_circle, Point


def main():
    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(b"Hello World",
                              SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                              640, 480,
                              SDL_WINDOW_SHOWN)
    window_surface = SDL_GetWindowSurface(window)
    renderer = SDL_CreateRenderer(window, -1, 0)

    draw_line(renderer, Point(370, 450), Point(5, 5), SDL_Color(255, 255, 255, 255))
    draw_line(renderer, Point(5, 5), Point(370, 450), SDL_Color(255, 255, 255, 255))
    draw_circle(renderer, Point(250, 250), 40, SDL_Color(255, 255, 21, 255))

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