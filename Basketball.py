import pygame
from pygame import Vector2
import math
import random
from Paddle import Brick


class Basketball:
    def __init__(self, x, y):
        img = pygame.image.load("imgs/Basketball.png")
        # 篮球的半径为10
        self.radius = 10
        self.surf = pygame.transform.scale(img, (self.radius * 2, self.radius * 2))
        self.rect = self.surf.get_rect(center=(x, y))
        velocity_x = random.random() * 3.0
        velocity_y = -math.sqrt(9 - velocity_x ** 2)
        self.velocity = Vector2(velocity_x, velocity_y)
        self.x = self.rect.x + self.radius
        self.y = self.rect.y + self.radius

    def collisionDetection(self, paddle):
        if paddle is None:
            return False
        rx = self.rect.x + self.radius
        ry = self.rect.y + self.radius
        # self.rect.x + self.radius是因为尽管创建时是根据中心点创建的，但是rect.x仍然是左上角的坐标而非中心点
        x = max(paddle.rect.x, min(rx, paddle.rect.x + paddle.rect.width))
        y = max(paddle.rect.y, min(ry, paddle.rect.y + paddle.rect.height))
        dx = self.rect.x + self.radius - x
        dy = self.rect.y + self.radius - y
        if dx ** 2 + dy ** 2 <= self.radius ** 2:
            if abs(dx) > abs(dy):
                self.velocity.x = -self.velocity.x
            else:
                self.velocity.y = -self.velocity.y
            if type(paddle) is Brick:
                return True
        return False

    def move(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        self.x = self.rect.x + self.radius
        self.y = self.rect.y + self.radius

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    def setVelocity(self, vx, vy):
        self.velocity.x = vx
        self.velocity.y = vy

    def isDisappear(self):
        x = self.rect.x + self.radius
        y = self.rect.y + self.radius
        if y >= 600 or y < 0 or x >= 800 or x < 0:
            return True
        else:
            return False
