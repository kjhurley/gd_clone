import pygame
import time

pygame.init()


class SquareOnlyLevel:
    def __init__(self, size=50):
        self.colour_of_ground = (0, 0, 100)
        self.ground_height = 5
        self.colour = (0, 128, 0)  # light green?
        self.size = size
        self.ground_y = 550
        self.x = 750
        self.y = 200

    def update(self):
        self.x += 0
        if self.y < (self.ground_y - self.ground_height - self.size):
            self.y += 1

    def draw(self, win):
        # draw the bottom of the level
        pygame.draw.rect(win, self.colour_of_ground, pygame.Rect(0, self.ground_y, win.get_width(), self.ground_height))

        # draw the square
        pygame.draw.rect(win, self.colour, pygame.Rect(self.x, self.y, self.size, self.size))


def start(real_screen, level):
    background = (0, 0, 0)
    win = pygame.display.set_mode(real_screen)

    while True:
        win.fill(background)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
        level.update()
        level.draw(win)
        pygame.display.update()

