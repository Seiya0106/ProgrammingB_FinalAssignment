import pygame as pg
import sys
import random

pg.init()
WIDTH = 800
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
font = pg.font.SysFont(None, 36)
img1 = pg.image.load("assets/button.png")
button = pg.transform.scale(img1, (150, 120))
pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
button_rect = pg.Rect(pos[0], pos[1], 150, 120)

while True:
    screen.fill(pg.Color("WHITE"))
    mouse = pg.mouse.get_pressed()
    mouse_pos = pg.mouse.get_pos()

    screen.blit(button, pos)
    if mouse[0]:
        if button_rect.collidepoint(mouse_pos):
            text = font.render("Clear", True, pg.Color("RED"))
            screen.blit(text, (10, 10))

    pg.display.update()

    # 閉じるボタンで終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()