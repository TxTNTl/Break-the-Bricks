import pygame


class Paddle:
    def __init__(self, x, y, width=25, height=25, color=(0, 0, 0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def disappear(self, paddles):
        pass


class Brick(Paddle):
    def __init__(self, x, y, width=25, height=25, color=(80, 80, 88)):
        super().__init__(x, y, width, height, color)

    def disappear(self, paddles):
        paddles.remove(self)


class Block(Paddle):
    def __init__(self, x, y, width=25, height=25, color=(0, 0, 0)):
        super().__init__(x, y, width, height, color)

    def disappear(self, paddles):
        pass