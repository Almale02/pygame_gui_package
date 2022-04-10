import math
import time
import pygame,sys


#from src.pyg_gui.gui_elements.text_out import Txt_out
#from src.pyg_gui.helper_files.text_class import Text



pygame.init()
window = pygame.display.set_mode((1000,800))


font = pygame.font.SysFont("ariel", 30)
fRenderer = font.render(f"Your score is about: {math.floor(131 - 10 / 3)}!", Text, (0,0,0))
txt_obj = Text(fRenderer)

score_output = Txt_out(window, (100,80), (81, 35), (0,100,150), txt_obj)


while True:
    for e in pygame.event.get():
        score_output.event_update(e)
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    score_output.non_event_update()
    pygame.display.flip()
    pygame.display.update()

    window.fill((0,0,0))
    time.sleep(1 / 60)

