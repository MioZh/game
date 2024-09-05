import pygame

from deffile import select_and_save_avatar, avasave, path_avatar, is_english_letter, draw_text_alpha, SpriteAnimator
from box import open_Box


pygame.init()



sprite_paths1 = [
        "boxpng/b1.png",
        "boxpng/b2.png",
        "boxpng/b3.png",
        "boxpng/b4.png",
        "boxpng/b5.png",
        "boxpng/b6.png",
        "boxpng/b7.png",
        "boxpng/b8.png",
        "boxpng/b9.png",
        "boxpng/b10.png"
    ]

sprite_paths2 = [
        "boxpng/a1.png",
        "boxpng/a2.png",
        "boxpng/a3.png",
        "boxpng/a4.png",
        "boxpng/a5.png",
        "boxpng/a6.png",
        "boxpng/a7.png",
        "boxpng/a8.png",
        "boxpng/a9.png",
        "boxpng/a10.png"
    ]

sprite_paths3 = [
        "boxpng/c1.png",
        "boxpng/c2.png",
        "boxpng/c3.png",
        "boxpng/c4.png",
        "boxpng/c5.png",
        "boxpng/c6.png",
        "boxpng/c7.png",
        "boxpng/c8.png",
        "boxpng/c9.png",
        "boxpng/c10.png"
    ]






WIDTH, HEIGHT = 1000, 600   
screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.Font("otf/Brotesk.otf", 18)

font25 = pygame.font.Font("otf/Brotesk.otf", 25)

coinbox = 0
coinboxview = font25.render(str(coinbox), True, (0,0,0))
coin = 1000
coinview = font25.render(str(coin), True, (0,0,0))

input_text = ""
name = "Azamat"
username = name
namepers = font.render(name, True, (0,0,0))

namepers_rect = namepers.get_rect(center=(895, 400))


path = 'png/ava4.jpg'

avatar, avataredit = avasave(path), path_avatar(path)

rect_color = (255, 255, 255)  

workshop = font.render('Workshop', True, (0,0,0))
quests = font.render('Quests', True, (0,0,0))
chests = font.render('Chests', True, (0,0,0))

back = font25.render('Back', True, (0,0,0))
open = font25.render('Open', True, (255,255,255))
save = font25.render('Save', True, (0,0,0))
namep = font25.render('user name: '+ username, True, (0,0,0))

o100 = font25.render('100', True, (255,255,255))
o50 = font25.render('50', True, (255,255,255))
o10 = font25.render('10', True, (255,255,255))

background = pygame.image.load('pngmenu/menuu.jpg')
master = pygame.image.load('pngmenu/master.png')
arena = pygame.image.load('pngmenu/arena.png')

background = pygame.transform.scale(background, (WIDTH, HEIGHT))
arena = pygame.transform.scale(arena, (50, 50))
master = pygame.transform.scale(master, (50, 50))

money = pygame.image.load('pngmenu/money.png')
moneyq = pygame.image.load('pngmenu/moneyq.png')
money = pygame.transform.scale(money, (45, 45))
moneyq = pygame.transform.scale(moneyq, (250, 70))

moneymaster = pygame.image.load('pngmenu/moneymaster.png')
moneymaster = pygame.transform.scale(moneymaster, (45, 45))
mastermon = pygame.transform.scale(moneymaster, (30, 30))

ava = pygame.image.load('pngmenu/ava.png')
ava = pygame.transform.scale(ava, (100, 100))


box = pygame.image.load('pngmenu/box.png')
box = pygame.transform.scale(box, (50, 50))

edit = pygame.image.load('pngmenu/editprofil.png')
edit = pygame.transform.scale(edit, (700, 300))
edit_rect = edit.get_rect(center=(500, 300))

abox = pygame.image.load('boxpng/a1.png')
abox = pygame.transform.scale(abox, (150, 100))

bbox = pygame.image.load('boxpng/b1.png')
bbox = pygame.transform.scale(bbox, (120, 106))

cbox = pygame.image.load('boxpng/c1.png')
cbox = pygame.transform.scale(cbox, (150, 100))

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

sprites = [pygame.image.load(path) for path in sprite_paths]

animator = SpriteAnimator(sprites, frame_rate=10, flip=True, scale_factor=1.5)


running = True
editview = False
winbox = False
nameedit = False

show_text = False
text_alpha = 0
fade_in = True
start_time = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos[0], event.pos[1])
            if((865<=event.pos[0]<925 and 390<event.pos[1]<470) or (20<=event.pos[0]<105 and 15<event.pos[1]<100)) and not winbox:
                editview = True
            elif(325<=event.pos[0]<380 and 360<event.pos[1]<380) and editview:
                editview = False
            elif(260<=event.pos[0]<360 and 315<event.pos[1]<380) and winbox:
                winbox = False
            elif(700<=event.pos[0]<865 and 215<event.pos[1]<385 and not editview) and not winbox:
                pass
            elif(375<=event.pos[0]<490 and 240<event.pos[1]<355 and not editview) and not winbox:
                pass
            elif(195<=event.pos[0]<300 and 425<event.pos[1]<525 and not editview) and not winbox:
                winbox = True
            elif (290<=event.pos[0]<410 and 225<event.pos[1]<345 and editview):
                path = select_and_save_avatar() 
                avataredit = path_avatar(path)
            elif(605<=event.pos[0]<660 and 360<event.pos[1]<380 and editview):
                avatar = avasave(path)
                editview = False
                nameedit = False
                if input_text != "":
                    username = input_text
                    name = username
                input_text = ""
                namepers = font.render(name, True, (0,0,0))
                namep = font25.render('user name: '+ username, True, (0,0,0))
                namepers_rect = namepers.get_rect(center=(895, 400))
            elif(465<=event.pos[0]<695 and 255<event.pos[1]<270 and editview):
                nameedit = True
            if(370<=event.pos[0]<445 and 325<event.pos[1]<345 and winbox):
                if coinbox>=10:
                    open_Box(sprite_paths3)
                    coinbox -= 10
                    coinboxview = font25.render(str(coinbox), True, (0,0,0))
                else:
                    show_text = True
                    fade_in = True
                    text_alpha = 0
                    start_time = pygame.time.get_ticks()
            elif(515<=event.pos[0]<580 and 325<event.pos[1]<345 and winbox):
                if coinbox>=50:
                    open_Box(sprite_paths3)
                    coinbox -= 50
                    coinboxview = font25.render(str(coinbox), True, (0,0,0))
                else:
                    show_text = True
                    fade_in = True
                    text_alpha = 0
                    start_time = pygame.time.get_ticks()
            elif(655<=event.pos[0]<720 and 325<event.pos[1]<345 and winbox):
                if coinbox>=100:
                    open_Box(sprite_paths3)
                    coinbox -= 100
                    coinboxview = font25.render(str(coinbox), True, (0,0,0))
                else:
                    show_text = True
                    fade_in = True
                    text_alpha = 0
                    start_time = pygame.time.get_ticks()

        if event.type == pygame.KEYDOWN and nameedit:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif is_english_letter(event.unicode) and len(input_text) <= 10:
                input_text += event.unicode
    screen.blit(background, (0, 0))

    screen.blit(ava, (10, 10))
    screen.blit(avatar, (25, 23))

    animator.update()
    screen.blit(animator.get_current_sprite(), (800, 340))

    pygame.draw.rect(screen, (225,225,225), pygame.Rect(713, 258, 87, 18))
    screen.blit(workshop, (715, 260))
    screen.blit(master, (725, 210))

    pygame.draw.rect(screen, (225,225,225), pygame.Rect(408, 283, 62, 18))
    screen.blit(quests, (410, 285))
    screen.blit(arena, (415, 240))

    pygame.draw.rect(screen, rect_color, namepers_rect)
    screen.blit(namepers, namepers_rect)


    pygame.draw.rect(screen, (225,225,225), pygame.Rect(218, 473, 60, 18))
    screen.blit(chests, (220, 475))
    screen.blit(box, (225, 425))

    

    screen.blit(moneyq, (750,10))
    screen.blit(money, (940,22))
    screen.blit(moneyq, (500,10))
    screen.blit(moneymaster, (690,22))

    screen.blit(coinboxview,(620, 33))
    screen.blit(coinview, (870, 33))
    if editview:
        screen.blit(edit, edit_rect)
        screen.blit(back, (325, 360))
        screen.blit(save, (605, 360))
        screen.blit(namep, (465, 250))

        if nameedit:
            input_n = font25.render("new name: " + input_text, True, (0,0,0))
            screen.blit(input_n, (465, 300))
        pygame.draw.rect(screen, (225,225,225), pygame.Rect(290, 225, 120, 120))
        screen.blit(avataredit, (295, 230))

    if winbox:
        screen.blit(edit, edit_rect)
        screen.blit(back, (260, 360))

        screen.blit(o10, (385, 210))
        screen.blit(mastermon, (410,205))
        screen.blit(bbox, (350, 220))  
        screen.blit(open, (375, 325))

        screen.blit(o50, (525, 210))
        screen.blit(mastermon, (555,205))
        screen.blit(abox, (490, 220))
        screen.blit(open, (515, 325))

        screen.blit(o100, (665, 210))
        screen.blit(mastermon, (700,205))
        screen.blit(cbox, (630, 220))
        screen.blit(open, (655, 325))

    if show_text:
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) / 1000

        if fade_in:
            text_alpha += 5  # Скорость плавного появления
            if text_alpha >= 255:
                text_alpha = 255
                fade_in = False

        else:
            text_alpha -= 5  # Скорость плавного исчезновения
            if text_alpha <= 0:
                text_alpha = 0
                show_text = False

        draw_text_alpha('INSUFFICIENT FUNDS', font, (255, 255, 255), screen, 420, 170, text_alpha)

    pygame.display.update()
pygame.quit()
