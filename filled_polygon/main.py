import sdl2.ext
import sys

from filled_polygon.graphics import draw_line, Point, draw_polygon

def get_pixel(pixels, point):
    return pixels[point.x][point.y]


def main():
    sdl2.ext.init()
    window = sdl2.ext.Window("Filled polygon", size=(640, 480))
    window.show()

    window_surface = window.get_surface()
    pixels = sdl2.ext.PixelView(window_surface)

    draw_polygon(pixels, [
        Point(70, 0),
        Point(100, 0),
        Point(100, 100),
        Point(70, 100),
    ], sdl2.ext.Color(255, 116, 113, 255), filled=True)
    draw_polygon(pixels, [
        Point(0, 100),
        Point(100, 100),
        Point(50, 0),
    ], sdl2.ext.Color(255, 255, 113, 255), filled=True)

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        window.refresh()
    sdl2.ext.quit()
    return 0


if __name__ == "__main__":
    sys.exit(main())