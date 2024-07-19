import pygame
import math

class Reflection():
    def __init__(self, x=375, y=525, width=50, height=5):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 182, 192)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, range):
        self.rect.x += range

    def specialCollision(self, ball):
        if self.rect.x <= ball.rect.x + ball.radius <= self.rect.x + self.rect.width:
            if 0 <= self.rect.y - ball.rect.y - ball.radius <= ball.radius:
                # -25 <= dx <= 25
                dx = ball.rect.x + ball.radius - self.rect.x - 25
                if dx > 0:
                    vx = min(0.12 * dx, 2.8)
                else:
                    vx = max(0.12 * dx, -2.8)
                vy = -math.sqrt(9 - vx ** 2)
                ball.setVelocity(vx, vy)
