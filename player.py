import pygame as pg
from game_state import GameState

# ゲーム状態の管理
game_state_manager = GameState()
COUNTDOWN = 0
PLAYING = 1
CLEAR = 2
game_state = game_state_manager.state
timer = game_state_manager.timer
# 前フレームの値を保持
prev_mouse_buttons = (False, False, False)

def clicked(rect, mouse_pos, mouse_buttons):
    global prev_mouse_buttons
    # 前フレームとマウスの位置が違うか検知
    is_just_clicked = not prev_mouse_buttons[0] and mouse_buttons[0]
    prev_mouse_buttons = mouse_buttons
    # 左クリックを押した瞬間の位置がボタンと同じ位置ならクリア
    if is_just_clicked and rect.collidepoint(mouse_pos):
            return True
    return False