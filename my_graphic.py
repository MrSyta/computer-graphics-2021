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
    dx = x2 - x1
    dy = y2 - y1

    is_steep = abs(dy) > abs(dx)

    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    dx = x2 - x1
    dy = y2 - y1

    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1

    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    if swapped:
        points.reverse()
    return points


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
