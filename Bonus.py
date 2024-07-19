import random
import pygame
from Basketball import Basketball


class Bonus:
    def __init__(self, x, y):
        img = pygame.image.load("imgs/DefaultImage.png")
        self.surf = pygame.transform.scale(img, (20, 20))
        self.rect = self.surf.get_rect(center=(x, y))
        self.velocity_y = random.randint(1, 4)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    def move(self):
        self.rect.y += self.velocity_y

    def disappear(self, bonuses):
        bonuses.remove(self)

    def make_reward(self, ball, player):
        pass


class DoubleBonus(Bonus):
    def __init__(self, x, y):
        super().__init__(x, y)
        img = pygame.image.load("imgs/DoubleBonus.png")
        self.surf = pygame.transform.scale(img, (20, 20))
        self.rect = self.surf.get_rect(center=(x, y))

    def make_reward(self, ball, player):
        return [Basketball(ball.rect.x, ball.rect.y) for _ in range(2)]


class TripleBonus(Bonus):
    def __init__(self, x, y):
        super().__init__(x, y)
        img = pygame.image.load("imgs/TripleBonus.png")
        self.surf = pygame.transform.scale(img, (20, 20))
        self.rect = self.surf.get_rect(center=(x, y))

    def make_reward(self, ball, player):
        return [Basketball(player.rect.x + 10, player.rect.y + 10) for _ in range(2)]
