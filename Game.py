import math
from Paddle import *
from Player import Player
from Reflection import Reflection
from Bonus import *


class Game:
    def __init__(self, paddle_list):
        pygame.init()
        pygame.display.set_caption("爱打篮球的坤坤")
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.balls = [Basketball(400, 500)]
        self.paddles = []
        for y in range(0, 600, 25):
            for x in range(0, 800, 25):
                if paddle_list[y // 25][x // 25] == 1:
                    self.paddles.append(Block(x, y))
                elif paddle_list[y // 25][x // 25] == 2:
                    self.paddles.append(Brick(x, y))
        self.player = Player()
        self.reflection = Reflection()
        self.bonuses = []

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 点击左上角或者右上角的x关闭窗口时，停止程序
                return False
        return True

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys, self.reflection)
        for ball in self.balls:
            ball.move()
            min_distance = 10000000
            target_paddle = None
            for paddle in self.paddles:
                # 找到距离最近的paddle进行碰撞检测 一种无奈的曲线救国方式
                px = paddle.rect.x + paddle.rect.width / 2
                py = paddle.rect.y + paddle.rect.height / 2
                distance = math.sqrt((px - ball.x) ** 2 + (py - ball.y) ** 2)
                if distance < min_distance:
                    target_paddle = paddle
                    min_distance = distance
            if ball.collisionDetection(target_paddle):
                self.crate_bonus(target_paddle)
                target_paddle.disappear(self.paddles)

            self.reflection.specialCollision(ball)
            if ball.isDisappear():
                self.balls.remove(ball)

        for paddle in self.paddles:
            if paddle is Brick:
                return

        for bonus in self.bonuses:
            bonus.move()
            if self.player.check_collision(bonus):
                self.player.receive_reward(bonus, self.balls[0], self.balls)
                bonus.disappear(self.bonuses)

        if len(self.balls) == 0:
            font = pygame.font.SysFont(None, 55)
            game_over_text = font.render("Game Over", True, (0, 255, 255))
            text_rect = game_over_text.get_rect(center=(400, 300))
            self.screen.blit(game_over_text, text_rect)
            pygame.display.flip()
            pygame.time.wait(4000)  # 等待2秒以便玩家可以看到游戏结束消息
            pygame.quit()

    def draw(self):
        self.screen.fill((255, 255, 255))
        for ball in self.balls:
            ball.draw(self.screen)
        for paddle in self.paddles:
            paddle.draw(self.screen)
        for bonus in self.bonuses:
            bonus.draw(self.screen)
        self.player.draw(self.screen)
        self.reflection.draw(self.screen)
        pygame.display.flip()

    def crate_bonus(self, paddle):
        ran = random.randint(2, 10)
        if ran < 4:
            x = paddle.rect.x + paddle.rect.width / 2
            y = paddle.rect.y + paddle.rect.height / 2
            if ran == 2:
                self.bonuses.append(DoubleBonus(x, y))
            elif ran == 3:
                self.bonuses.append(TripleBonus(x, y))
