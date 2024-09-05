import pygame
import sys

def open_Box(sprite_paths):
    pygame.init()

    screen = pygame.display.set_mode((1000, 600))
    new_size = (200, 200)
    sprites = [pygame.transform.scale(pygame.image.load(path), new_size) for path in sprite_paths]

    clock = pygame.time.Clock()
    sprite_count = len(sprites)
    animation_speed = 5

    background = pygame.image.load('boxpng/backgraundbox.png')
    background = pygame.transform.scale(background, (1000, 600))
    moneybox = pygame.image.load('boxpng/moneybox.png')
    moneybox = pygame.transform.scale(moneybox, (1000, 600))

    def play_animation():
        current_sprite = 0
        while current_sprite < sprite_count * animation_speed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            current_sprite += 1
            sprite_index = current_sprite // animation_speed

            if sprite_index >= sprite_count:
                sprite_index = sprite_count - 1

            screen.fill((0, 0, 0))
            sprite = sprites[sprite_index]
            sprite_rect = sprite.get_rect(center=(500, 300))
            screen.blit(background, (0, 0))
            screen.blit(moneybox, (0, 0))
            screen.blit(sprite, sprite_rect)

            pygame.display.flip()
            clock.tick(30)

        return

    def start_animation():
        play_animation()

    start_animation()

    return
