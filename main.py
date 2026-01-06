import pygame as pg
import sys
import random
import player as p
import stages as s

pg.init()
WIDTH = 800
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
font = pg.font.SysFont(None, 36)
large_font = pg.font.SysFont(None, 72)

img1 = pg.image.load("assets/button.png")
button = pg.transform.scale(img1, (150, 120))
pos = (random.randint(0, WIDTH - 150), random.randint(0, HEIGHT - 120))
button_rect = pg.Rect(pos[0], pos[1], 150, 120)

while True:
    screen.fill(pg.Color("WHITE"))
    
    if p.game_state == p.PLAYING:
        s.Playing(screen, button, button_rect, pos).button_click()
                
    elif p.game_state == p.CLEAR:
        s.GameClear(screen, font, large_font).clear_display(WIDTH, HEIGHT)

    pg.display.update()

    # イベント処理
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        # クリア画面でRキーを押すとリトライ
        if event.type == pg.KEYDOWN: 
            if event.key == pg.K_r and p.game_state == p.CLEAR: 
                p.game_state = p.PLAYING
                pos = (random.randint(0, WIDTH - 150), random.randint(0, HEIGHT - 120))
                button_rect = pg.Rect(pos[0], pos[1], 150, 120)