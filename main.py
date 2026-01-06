import pygame as pg
import sys
import random

pg.init()
WIDTH = 800
HEIGHT = 600
screen = pg. display.set_mode((WIDTH, HEIGHT))
font = pg.font.SysFont(None, 36)
large_font = pg.font.SysFont(None, 72)

# ゲーム状態の管理
PLAYING = 0
CLEAR = 1
game_state = PLAYING

img1 = pg.image.load("assets/button.png")
button = pg.transform.scale(img1, (150, 120))
pos = (random.randint(0, WIDTH - 150), random.randint(0, HEIGHT - 120))
button_rect = pg.Rect(pos[0], pos[1], 150, 120)

while True:
    screen.fill(pg.Color("WHITE"))
    
    if game_state == PLAYING:
        mouse = pg.mouse.get_pressed()
        mouse_pos = pg.mouse.get_pos()

        screen.blit(button, pos)
        
        # ボタンクリックでクリア画面に遷移
        if mouse[0]:
            if button_rect.collidepoint(mouse_pos):
                game_state = CLEAR
                
    elif game_state == CLEAR:
        clear_text = large_font.render("GAME CLEAR!", True, pg.Color("RED"))
        text_rect = clear_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(clear_text, text_rect)
        
        # リトライボタン（オプション）
        retry_text = font.render("Press R to Retry", True, pg.Color("BLUE"))
        retry_rect = retry_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))
        screen.blit(retry_text, retry_rect)

    pg.display.update()

    # イベント処理
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        # クリア画面でRキーを押すとリトライ
        if event.type == pg.KEYDOWN: 
            if event.key == pg.K_r and game_state == CLEAR: 
                game_state = PLAYING
                pos = (random.randint(0, WIDTH - 150), random.randint(0, HEIGHT - 120))
                button_rect = pg.Rect(pos[0], pos[1], 150, 120)