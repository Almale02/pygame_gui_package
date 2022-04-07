import time
import pygame,sys
from src.pyg_gui.helper_files.text_class import Text


pygame.init()
window = pygame.display.set_mode((1000,800))

font = pygame.font.SysFont("arial",30)
font_render = font.render("test",True,(0,0,0))
text_obj = Text((100,100), font_render.get_size(),font_render, "auto_XY")

text_pos = text_obj.caclulate_pos()

test_sur = pygame.Surface((100,100))
test_sur.fill((30,255,10))

while True:
    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    window.blit(test_sur,(20,20))
    test_sur.blit(font_render, (text_pos))
    pygame.display.flip()
    pygame.display.update()
    time.sleep(1 / 60)

