import pygame as pg
import player as p

class Playing:
    def __init__(self, screen, button, button_rect, pos):
        self.screen = screen
        self.button = button
        self.button_rect = button_rect
        self.pos = pos
    def button_click(self):
        mouse = pg.mouse.get_pressed()
        mouse_pos = pg.mouse.get_pos()

        self.screen.blit(self.button, self.pos)
        
        # ボタンクリックでクリア画面に遷移
        if p.clicked(self.button_rect, mouse_pos, mouse):
            p.game_state = p.CLEAR

class GameClear:
    def __init__(self, screen):
        self.screen = screen
    def clear_display(self):
        WIDTH = self.screen.get_width()
        HEIGHT = self.screen.get_height()
        font = pg.font.SysFont(None, 36)
        large_font = pg.font.SysFont(None, 72)
        clear_text = large_font.render("GAME CLEAR!", True, pg.Color("RED"))
        text_rect = clear_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(clear_text, text_rect)
        
        # リトライボタン（オプション）
        retry_text = font.render("Press R to Retry", True, pg.Color("BLUE"))
        retry_rect = retry_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))
        self.screen.blit(retry_text, retry_rect)
