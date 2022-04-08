import time
import pygame,sys
from src.pyg_gui.helper_files.text_class import Text
from src.pyg_gui.gui_elements.button import Button

def move_left(arg):
    button.size[1] += arg[0]
def move_Y(arg):
    button.size[0] += arg[0]




pygame.init()
window = pygame.display.set_mode((1000,800))

font = pygame.font.SysFont("ariel",30)
font_renderer = font.render("move_left", True, (100,100,100))


text_object = Text(font_renderer)
button = Button(window, [0,0], [200,70], (42,111,55), text_object,[move_left,move_Y],[[1,3],[1],[6]])



while True:
    for e in pygame.event.get():
        button.event_update(e)
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    button.non_event_update()

    pygame.display.flip()
    pygame.display.update()
    window.fill((0,0,0))
    time.sleep(1 / 60)

