import pygame


class Player:
    def __init__(self):
        img = pygame.image.load("imgs/iKun.png")
        self.surf = pygame.transform.scale(img, (50, 50))
        self.rect = self.surf.get_rect(center=(400, 550))

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    def move(self, keys, reflection):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.rect.x > 20:
                self.rect.x -= 3
                reflection.move(-3)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.rect.x < 725:
                self.rect.x += 3
                reflection.move(3)

    def check_collision(self, bonus):
        bx = bonus.rect.x + 10
        by = bonus.rect.y + 10
        px = self.rect.x + 25
        py = self.rect.y + 25
        dx = bx - px
        dy = by - py
        if dx ** 2 + dy ** 2 < 30 ** 2:
            return True
        return False

    def receive_reward(self, bonus, ball, balls):
        balls += bonus.make_reward(ball, self)
