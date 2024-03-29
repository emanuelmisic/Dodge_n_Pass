import pygame
from sys import exit
from components.level import Level
from components.button import Button

from settings import *

pygame.init()
pygame.display.set_caption("Dodge 'n Pass")
clock = pygame.time.Clock()

# display title function
def display_title(str):
    level_font = pygame.font.Font('assets/level_font.ttf', 32)
    level_text = level_font.render(str, True, (255, 255, 255))
    level_text_rect = level_text.get_rect()
    level_text_rect.center = (WIDTH / 2, HEIGHT / 3)
    screen.blit(level_text, level_text_rect)
    
def display_advance_level_text(str):
    advance_level_font = pygame.font.Font('assets/instructions_font.ttf', 28)
    advance_level_text = advance_level_font.render(str, True, (255, 255, 255))
    advance_level_text_rect = advance_level_text.get_rect()
    advance_level_text_rect.center = (WIDTH / 2, HEIGHT / 2)
    screen.blit(advance_level_text, advance_level_text_rect)

# load button images
start_img = pygame.image.load('assets\start_game_btn.png').convert_alpha()
quit_img = pygame.image.load('assets/quit_btn.png').convert_alpha()

# create button instances:
# start
start_button = Button(0, 0, start_img)
start_button_width = start_button.get_width()
start_button_height = start_button.get_height()
start_button_draw = Button((WIDTH / 2) - (start_button_width / 2), (HEIGHT / 4) - (start_button_height / 2), start_img)
# quit
quit_button = Button(0, 0, quit_img)
quit_button_width = quit_button.get_width()
quit_button_height = quit_button.get_height()
quit_button_draw = Button((WIDTH / 2) - (quit_button_width / 2), (HEIGHT / 2) - (quit_button_height / 2), quit_img)

class Game:
    def __init__(self, level_num):
        self.level_num = level_num
        self.level = Level(level_num)

    def run(self):
        once = True
        game_state = GameState.START
        while game_state == GameState.START:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            screen.blit(BG1, (0, 0))
            self.level.run()
            pygame.display.update()
            clock.tick(FPS)
            
            if self.level.is_exit_reached():
                game_state = GameState.STOP
            
            
            while game_state == GameState.STOP:
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                
                keys = pygame.key.get_pressed()

                if keys[pygame.K_SPACE]:
                    game = Game(self.level_num + 1)
                    game.run()
                    
                if once:
                    screen.blit(pause_bg, (0, 0))
                    display_title(f'Level {self.level_num} Completed')
                    display_advance_level_text(f'Press SPACE to advance to level {self.level_num + 1}')
                    once = False
                    
                pygame.display.update()
                clock.tick(FPS)
                

class Menu:
    def run(self):
        game_state = GameState.MENU
        while game_state == GameState.MENU:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            screen.fill((0, 0, 0))
            
            if start_button_draw.draw(screen):
                game = Game(1)
                game.run()
            
            if quit_button_draw.draw(screen):
                pygame.quit()
                exit()
            
            pygame.display.update()
            clock.tick(FPS)

if __name__ == '__main__':
    menu = Menu()
    menu.run()
