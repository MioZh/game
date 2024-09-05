import pygame
from deffile import SpriteAnimator, levelup, lvledit

pygame.init()

screen = pygame.display.set_mode((1000, 600))
background = pygame.image.load('pngmaster/backgraundmaster.png')
background = pygame.transform.scale(background, (1000, 600))
backpers = pygame.image.load('pngmaster/backpers.png')
backpers = pygame.transform.scale(backpers, (300, 500))
backup = pygame.image.load('pngmaster/backpers.png')
backup = pygame.transform.scale(backup, (600, 500))
hpatk = pygame.image.load('pngmaster/hpandatk.png')
hpatk = pygame.transform.scale(hpatk, (200, 100))

hp1 = pygame.image.load('pngmaster/hp1.png')
hp1 = pygame.transform.scale(hp1, (50, 50))
hp2 = pygame.image.load('pngmaster/hp2.png')
hp2 = pygame.transform.scale(hp2, (50, 50))
atk1 = pygame.image.load('pngmaster/atk1.png')
atk1 = pygame.transform.scale(atk1, (50, 50))
atk2 = pygame.image.load('pngmaster/atk2.png')
atk2 = pygame.transform.scale(atk2, (50, 50))

hpup = pygame.image.load('pngmaster/hpup.png')
hpup = pygame.transform.scale(hpup, (50, 50))
atkup = pygame.image.load('pngmaster/atkup.png')
atkup = pygame.transform.scale(atkup, (50, 50))

hp = 50
atk = 15
font = pygame.font.Font("otf/Brotesk.otf", 18)
hpview = font.render("HP: "+str(hp), True, (0,0,0))
atkview = font.render("ATK: "+str(atk), True, (0,0,0))

font25 = pygame.font.Font("otf/Brotesk.otf", 28)
exitbutton = font25.render("EXIT", True, (255, 255, 255))

conifbutton = font25.render("CONFIRM", True, (0, 0, 0))
resetbutton = font25.render("RESET", True, (0, 0, 0))

lvlhp1 = 0
lvlhp2 = 0
lvlatk1 = 0
lvlatk2 = 0

lvlhp1v = font.render("LVL "+str(lvlhp1), True, (0, 0, 0))
lvlhp2v = font.render("LVL "+str(lvlhp2), True, (0, 0, 0))
lvlatk1v = font.render("LVL "+str(lvlatk1), True, (0, 0, 0))
lvlatk2v = font.render("LVL "+str(lvlatk2), True, (0, 0, 0))

fontmore = pygame.font.Font("otf/Brotesk.otf", 45)
plus = fontmore.render("+", True, (0, 0, 0))
minus = fontmore.render("-", True, (0, 0, 0))

sprite_paths  = [
            "gg/idle_1.png",
            "gg/idle_2.png",
            "gg/idle_3.png",
            "gg/idle_4.png",
            "gg/idle_5.png",
            "gg/idle_6.png",
            "gg/idle_7.png",
            "gg/idle_8.png",
            "gg/idle_9.png",
            "gg/idle_10.png"
        ]
sprites = [pygame.transform.scale(pygame.image.load(path), (600, 600)) for path in sprite_paths]

animator = SpriteAnimator(sprites, frame_rate=10, flip=True, scale_factor=1.5)
running = True

uphp1 = 0
uphp2 = 0
upatk1 = 0
upatk2 = 0





while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 490<=event.pos[0]<505 and 180<event.pos[1]<195:
                uphp1+=1
                lvlhp1 = levelup(lvlhp1)
                print(lvlhp1, uphp1)
            elif 490<=event.pos[0]<505 and 250<event.pos[1]<265:
                uphp1+=1
                lvlhp2 = levelup(lvlhp2)
            elif 490<=event.pos[0]<505 and 320<event.pos[1]<335:
                upatk1+=1
                lvlatk1 = levelup(lvlatk1)
            elif 490<=event.pos[0]<505 and 390<event.pos[1]<405:
                upatk2+=1
                lvlatk2 = levelup(lvlatk2)
            elif 420<=event.pos[0]<540 and 460<event.pos[1]<480:
                lvlhp1 = levelup(lvlhp1, uphp1)
                lvlhp2 = levelup(lvlhp2, uphp2)
                lvlatk1 = levelup(lvlatk1, upatk1)
                lvlatk2 = levelup(lvlatk1, upatk1)
                uphp1, uphp2, upatk1, upatk2 = 0
                lvlhp1, lvlhp2, lvlatk1, lvlatk2 = lvledit(lvlhp1, lvlhp2, lvlatk1, lvlatk2, font)
            

            
    screen.blit(background, (0,0))
    screen.blit(exitbutton, (20, 20))

    screen.blit(backpers, (650, 50))
    screen.blit(hpatk,(700, 120))
    screen.blit(hpview, (730, 120))
    screen.blit(atkview, (730, 170))

    screen.blit(backup, (20, 50))

    screen.blit(lvlhp1v, (100, 178))
    screen.blit(hp1, (150, 160))
    screen.blit(minus, (465, 167))
    screen.blit(plus, (490, 167))

    screen.blit(lvlhp2v, (100, 248))
    screen.blit(hp2, (150, 230))
    screen.blit(minus, (465, 237))
    screen.blit(plus, (490, 237))

    screen.blit(lvlatk1v, (100, 318))
    screen.blit(atk1, (150, 300))
    screen.blit(minus, (465, 307))
    screen.blit(plus, (490, 307))

    screen.blit(lvlatk2v, (100, 388))
    screen.blit(atk2, (150, 370))
    screen.blit(minus, (465, 377))
    screen.blit(plus, (490, 377))

    pygame.draw.rect(screen, (225,225,225), pygame.Rect(210, 180, 250, 14))
    pygame.draw.rect(screen, (225,225,225), pygame.Rect(210, 250, 250, 14))
    pygame.draw.rect(screen, (225,225,225), pygame.Rect(210, 320, 250, 14))
    pygame.draw.rect(screen, (225,225,225), pygame.Rect(210, 390, 250, 14))
    
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(215, 184, lvlhp1%240, 6))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(215, 254, lvlhp2%240, 6))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(215, 324, lvlatk1%240, 6))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(215, 394, lvlatk2%240, 6))


    screen.blit(atkup, (400, 100))
    screen.blit(hpup, (500, 97))

    screen.blit(conifbutton, (420, 460))
    screen.blit(resetbutton, (290, 460))    
    animator.update()

    screen.blit(animator.get_current_sprite(), (360, -100))
    pygame.display.update()
pygame.quit()

