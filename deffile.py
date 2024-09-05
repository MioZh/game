import pygame
import tkinter as tk
from tkinter import filedialog
import shutil
import os
import time

class SpriteAnimator:
    def __init__(self, sprite_list, frame_rate, flip=False, scale_factor=1.0):
        self.sprites = [pygame.transform.flip(pygame.transform.scale(sprite, 
                        (int(sprite.get_width() * scale_factor), 
                         int(sprite.get_height() * scale_factor))), 
                        flip, False) for sprite in sprite_list]
        self.frame_rate = frame_rate
        self.current_frame = 0
        self.last_update = time.time()
        self.total_frames = len(self.sprites)

    def update(self):
        now = time.time()
        if now - self.last_update > 1.0 / self.frame_rate:
            self.current_frame = (self.current_frame + 1) % self.total_frames
            self.last_update = now

    def get_current_sprite(self):
        return self.sprites[self.current_frame]

def is_english_letter(char):
    return char.isalpha() and char.isascii()

def path_avatar(path):
    avatar = pygame.image.load(path)
    avataredit = pygame.transform.scale(avatar, (110, 110))
    return avataredit
    
def draw_text_alpha(text, font, color, surface, x, y, alpha):
    text_surface = font.render(text, True, color).convert_alpha()
    text_surface.set_alpha(alpha)
    surface.blit(text_surface, (x, y))


def avasave(path):
    avatar = pygame.image.load(path)
    avatar = pygame.transform.scale(avatar, (75, 75))
    return avatar

def select_and_save_avatar():
    root = tk.Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename()

    if file_path:
        avatar_dir = os.path.join(os.getcwd(), 'avatar')
        if not os.path.exists(avatar_dir):
            os.makedirs(avatar_dir)

        filename = os.path.basename(file_path)
        destination_path = os.path.join(avatar_dir, filename)

        shutil.copy(file_path, destination_path)

        return destination_path
    return None

def lvledit(lvlhp1, lvlhp2, lvlatk1, lvlatk2, font):
    lvlhp1v = font.render("LVL "+str(lvlhp1), True, (0, 0, 0))
    lvlhp2v = font.render("LVL "+str(lvlhp2), True, (0, 0, 0))
    lvlatk1v = font.render("LVL "+str(lvlatk1), True, (0, 0, 0))
    lvlatk2v = font.render("LVL "+str(lvlatk2), True, (0, 0, 0))
    return lvlhp1v, lvlhp2v, lvlatk1v, lvlatk2v

def levelup1(lvl, up):
    for i in range(1, up+ 1):
        if lvl/240 == 0 or lvl/240 == 1:
            lvl += 240
        elif 1 < lvl/240 < 6:
            lvl += 120
        elif 5 < lvl/240 < 9:
            lvl += 80
        elif 9 == lvl/240 :
            lvl += 40
        print(lvl/240)
    return lvl

def levelup(lvl):
    if lvl/240 == 0 or lvl/240 == 1:
        lvl += 240
    elif 1 < lvl/240 < 6:
        lvl += 120
    elif 5 < lvl/240 < 9:
        lvl += 80
    elif 8 < lvl/240 < 10 :
        lvl += 40
    print(lvl/240)
    return lvl