import pygame as pg

PLAYING = 0
CLEAR = 1

class GameState:
    def __init__(self):
        self.state = PLAYING
        self.timer = Timer()
    
    def reset(self):
        self.state = PLAYING
        self.timer.reset()

class Timer:
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
    
    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.is_running = False
    
    def get_elapsed_time(self):
        if self.is_running and self.start_time is not None:
            return (pg.time.get_ticks() - self.start_time) / 1000.0
        return self.elapsed_time
    
    def format_time(self, decimal_places=3):
        time = self.get_elapsed_time()
        return f"{time:.{decimal_places}f}"