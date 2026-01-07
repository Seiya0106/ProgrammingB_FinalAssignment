import pygame as pg
import player as p

class Time:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.is_running = False
    
    def start(self):
        if not self.is_running:
            self.start_time = pg.time.get_ticks()
            self.is_running = True
    
    def stop(self):
        if self.is_running:
            self.elapsed_time = (pg.time.get_ticks() - self.start_time) / 1000.0
            self.is_running = False
            return self.elapsed_time
        return self.elapsed_time
    
    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.is_running = False
    
    def get_elapsed_time(self):
        # 経過時間を秒単位で取得する
        if self.is_running and self.start_time is not None:
            return (pg.time.get_ticks() - self.start_time) / 1000.0
        return self.elapsed_time
    
    def format_time(self, decimal_places=3):
        # 小数点以下の桁数を指定して経過時間を文字列で返す
        return f"{self.elapsed_time:.{decimal_places}f}"

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
        mouse = pg.mouse.get_pressed()
        mouse_pos = pg.mouse.get_pos()

        # 開始した時間を記録
        if not p.timer.is_running:
            p.timer.start()

        self.screen.blit(self.button, self.pos)
        
        # ボタンクリックでクリア画面に遷移
        if p.clicked(self.button_rect, mouse_pos, mouse):
            p.timer.stop()
            p.game_state = p.CLEAR

class GameClear(Game_Condition):
    def __init__(self, screen, font, large_font, WIDTH, HEIGHT):
        super().__init__(screen)
        self.font = font
        self.large_font = large_font
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
    def clear_display(self):
        clear_text = self.large_font.render("GAME CLEAR!", True, pg.Color("RED"))
        text_rect = clear_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        self.screen.blit(clear_text, text_rect)

        # クリアタイムを表示
        time_text = self.font.render(f"Clear Time: {p.timer.format_time()} sec", True, pg.Color("GREEN"))
        time_rect = time_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 40))
        self.screen.blit(time_text, time_rect)
        
        # リトライボタン（オプション）
        retry_text = self.font.render("Press R to Retry", True, pg.Color("BLUE"))
        retry_rect = retry_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 80))
        self.screen.blit(retry_text, retry_rect)
