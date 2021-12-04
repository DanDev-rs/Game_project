import pygame


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size


class Tile:
    def __init__(self):
        pass


class SurfaceTile(Tile):
    pass


class VoidTile(Tile):
    pass


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()