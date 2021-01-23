import pygame

WIDTH, HEIGHT = 600, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bresenham algorithm")


def draw_window():
    WIN.fill((255, 255, 255))
    pygame.display.update()


def bresenham(start, end):
    """Bresenham's Line Algorithm
    Produces a list of tuples from start to end"""

    x1, y1 = start
    x2, y2 = end
    x, y = x1, y1

    if x1 < x2:
        xi = 1
        dx = x2 - x1
    else:
        xi = -1
        dx = x1 - x2

    if y1 < y2:
        yi = 1
        dy = y2 - y1
    else:
        yi = -1
        dy = y1 - y2

    yield x, y

    if dx > dy:
        ai = (dy - dx) * 2
        bi = dy * 2
        d = bi - dx

        while x != x2:
            if d >= 0:
                x += xi
                y += yi
                d += ai
            else:
                d += bi
                x += xi

            yield x, y

    else:
        ai = (dx - dy) * 2
        bi = dx * 2
        d = bi - dy

        while y != y2:
            if d >= 0:
                x += xi
                y += yi
                d += ai
            else:
                d += bi
                y += yi

            yield x, y


def draw_line(start, end):
    pixels = bresenham(start, end)
    for pixel in pixels:
        WIN.set_at(pixel, (0, 0, 0))
    pygame.display.update()


def draw_house():
    # square
    draw_line((200, 200), (400, 200))
    draw_line((200, 200), (200, 400))
    draw_line((200, 400), (400, 400))
    draw_line((400, 400), (400, 200))

    # roof
    draw_line((200, 200), (300, 100))
    draw_line((400, 200), (300, 100))

    # door
    draw_line((280, 400), (280, 350))
    draw_line((280, 350), (320, 350))
    draw_line((320, 350), (320, 400))

    # windows
    draw_line((220, 235), (280, 235))
    draw_line((280, 235), (280, 295))
    draw_line((280, 295), (220, 295))
    draw_line((220, 295), (220, 235))
    draw_line((250, 235), (250, 295))
    draw_line((220, 265), (280, 265))

    draw_line((380, 235), (320, 235))
    draw_line((320, 235), (320, 295))
    draw_line((320, 295), (380, 295))
    draw_line((380, 295), (380, 235))
    draw_line((350, 235), (350, 295))
    draw_line((380, 265), (320, 265))


def main():
    draw_window()
    draw_house()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()
