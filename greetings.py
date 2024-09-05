import pygame

pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load('png/StartScreen.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

asis = pygame.image.load('assist/fem3.png')
asis = pygame.transform.scale(asis, (600, 600))
asis_rect = asis.get_rect(topleft=(550, 150))

mess = pygame.image.load('asset/mes.png')
mess = pygame.transform.scale(mess, (900, 200))
mess_rect = mess.get_rect(topleft=(50, 400))

fade_surface = pygame.Surface((WIDTH, HEIGHT))
fade_surface.fill((0, 0, 0))

alpha = 0
fade_in_speed = 1
fade_out_speed = 1 
max_alpha = 150  

running = True
fade_in = True 
fade_out = False 
display_images = False  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    if fade_in:
        if alpha < 255:
            alpha += fade_in_speed
        else:
            fade_in = False
            fade_out = True
    elif fade_out:
        if alpha > max_alpha:
            alpha -= fade_out_speed
        else:
            fade_out = False
            display_images = True  

    fade_surface.set_alpha(alpha)
    screen.blit(fade_surface, (0, 0))

    if display_images:
        screen.blit(asis, asis_rect)
        screen.blit(mess, mess_rect)

    pygame.display.update()

pygame.quit()