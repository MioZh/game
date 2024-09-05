import pygame
from video_page import StartVideo

pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_icon(pygame.image.load("png/icons.jpg"))
pygame.display.set_caption("The Legend of the Summoned Hero")

background = pygame.image.load('png/startimg.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

font = pygame.font.Font("otf/Brotesk.otf", 18)
fontq = pygame.font.Font("otf/Brotesk.otf", 23)


textgame = fontq.render('The Legend of the Summoned Hero', True, (0,0,0))
textgame = textgame.convert_alpha()
textgame_rect = textgame.get_rect(center=(WIDTH // 2, HEIGHT - 280))

text = font.render('start the journey', True, (0,0,0))
text = text.convert_alpha()
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 250))

clock = pygame.time.Clock()
running = True
alpha = 255  
fade_out = True  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 0 <= event.pos[0] <= WIDTH and 0 <= event.pos[1] <= HEIGHT:
                StartVideo()

    screen.blit(background, (0, 0))

    if fade_out:
        alpha -= 5
        if alpha <= 0:
            alpha = 0
            fade_out = False
    else:
        alpha += 5
        if alpha >= 255:
            alpha = 255
            fade_out = True

    # Применение альфа-канала к тексту
    text.set_alpha(alpha)
    screen.blit(text, text_rect)
    screen.blit(textgame, textgame_rect)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
