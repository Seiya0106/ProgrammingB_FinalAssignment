import pygame as pg
import player as p

# Timeクラスは削除（game_state. pyのTimerクラスに統合）

class Game_Condition:
    def __init__(self, screen):
        self.screen = screen

class Playing(Game_Condition):
    def __init__(self, screen, button, button_rect, pos):
        super().__init__(screen)
        self.button = button
        self.button_rect = button_rect
        self.pos = pos
    
    def button_click(self):
        mouse = pg.mouse. get_pressed()
        mouse_pos = pg.mouse.get_pos()

        # 開始した時間を記録
        if not p.timer.is_running:
            p.timer. start()

        self.screen.blit(self.button, self.pos)
        
        # ボタンクリックでクリア画面に遷移
        if p.clicked(self.button_rect, mouse_pos, mouse):
            p.timer.stop()
            p.game_state_manager.state = p.CLEAR

class GameClear(Game_Condition):
    def __init__(self, screen, font, large_font, WIDTH, HEIGHT):
        super().__init__(screen)
        self.font = font
        self.large_font = large_font
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
    
    def clear_display(self):
        clear_text = self.large_font.render("GAME CLEAR!", True, pg.Color("RED"))
        text_rect = clear_text.get_rect(center=(self. WIDTH // 2, self.HEIGHT // 2))
        self.screen.blit(clear_text, text_rect)

        # クリアタイムを表示
        time_text = self.font.render(f"Clear Time: {p.timer.format_time()} sec", True, pg.Color("GREEN"))
        time_rect = time_text.get_rect(center=(self. WIDTH // 2, self.HEIGHT // 2 + 40))
        self.screen.blit(time_text, time_rect)
        
        # リトライボタン（オプション）
        retry_text = self.font.render("Press R to Retry", True, pg.Color("BLUE"))
        retry_rect = retry_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 80))
        self.screen.blit(retry_text, retry_rect)