import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

WHITE = (255, 255, 255)
BLACK = (0,0,0)

class Snowflake:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(-height, 0)
        self.size = random.randint(2, 5)
        self.speed = random.uniform(1, 3)

    def fall(self):
        self.y += self.speed
        if self.y > height:
            self.y = random.randint(-20, -1)
            self.x = random.randint(0, width)

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, int(self.y)), self.size)

def main():
    clock = pygame.time.Clock()
    snowflakes = [Snowflake() for _ in range(100)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for snowflake in snowflakes:
            snowflake.fall()
            snowflake.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()