import pygame as pg
import random

# ゲーム状態の管理
PLAYING = 0
CLEAR = 1
game_state = PLAYING

# タイマー管理
start_time = None
elapsed_time = 0

def clicked(rect, mouse_pos, mouse_buttons):
    if mouse_buttons[0]:
        if rect.collidepoint(mouse_pos):
            return True
    return False