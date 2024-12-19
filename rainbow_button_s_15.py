import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

background_color = (255, 255, 255)

def main():
    global background_color
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                background_color = (random.randint(0, 255),
                                    random.randint(0, 255),
                                    random.randint(0, 255))
                
        screen.fill(background_color)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
