import math
import time
import pygame,sys,random
import __main__ as asa


"""
from src.pyg_gui.helper_files.text_class import Text
from src.pyg_gui.gui_elements.drop_down import Drop_down
"""

pygame.init()



def asd(arg):
    print(arg[0])




window = pygame.display.set_mode((1000,800))
box = Drop_down(window, (80, 255), [130, 40], (0,0,0), ["1", "2", "3", "4", "5", "6"],Text(30, "choose boxcrasd", (100, 0, 100)), asd, 3)



while True:
    for e in pygame.event.get():
        box.event_update(e)


        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    box.non_event_update()
    pygame.display.flip()
    pygame.display.update()

    window.fill((0,0,0))
    time.sleep(1 / 60)

