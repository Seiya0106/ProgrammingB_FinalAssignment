import pygame as pg
from game_state import GameState

# ゲーム状態の管理
game_state_manager = GameState()

# 後方互換性のため
PLAYING = 0
CLEAR = 1
game_state = game_state_manager.state
timer = game_state_manager.timer

def clicked(rect, mouse_pos, mouse_buttons):
    if mouse_buttons[0]: 
        if rect.collidepoint(mouse_pos):
            return True
    return False