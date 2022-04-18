import math
import time
import pygame,sys,random


from src.pyg_gui.gui_elements.drop_down import Drop_down
from src.pyg_gui.helper_files.text_class import Text

pygame.init()


def submit_ev(arg):
    print(arg[0])






window = pygame.display.set_mode((1000,800))

drop_box = Drop_down(window, (130,13), (120,36), (100,100,100), ["lesson_1","lesson_2","lesson_3", "lesson_4", "lesson_5"], Text(30, "choice_box", (0,0,0)),submit_ev, 2)

while True:
    for e in pygame.event.get():
        drop_box.event_update(e)

        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    drop_box.non_event_update()
    pygame.display.flip()
    pygame.display.update()

    window.fill((0,0,0))
    time.sleep(1 / 60)

