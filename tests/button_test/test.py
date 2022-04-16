import math
import time
import pygame,sys,random


from src.pyg_gui.gui_elements.text_in import Txt_in
from src.pyg_gui.gui_elements.button import Button
from src.pyg_gui.gui_elements.text_out import Txt_out
from src.pyg_gui.helper_files.text_class import Text

pygame.init()
text_obj = Text(30, "Asd,basd",(0,0,0))

def submit_ev(arg):
    outTxt.txt_obj.txt = inTxt.txt_obj.txt

window = pygame.display.set_mode((1000,800))


objTxt_in = Text(30, "txt", (0,0,0))
objTxt_out = Text(30, "", (0,0,0))
objSub = Text(30, "submit", (0,0,0))

inTxt = Txt_in(window, [280,200], (400,50),(100,120,200),objTxt_in)
outTxt = Txt_out(window, [280,400], (300,50),(100,120,200),objTxt_out)
submit = Button(window, [280,600], (300,50),(100,120,200),objSub,[submit_ev],[()])
while True:
    for e in pygame.event.get():
        inTxt.event_update(e)
        outTxt.event_update(e)
        submit.event_update(e)

        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    submit.non_event_update()
    inTxt.non_event_update()
    outTxt.non_event_update()
    pygame.display.flip()
    pygame.display.update()

    window.fill((0,0,0))
    time.sleep(1 / 60)

