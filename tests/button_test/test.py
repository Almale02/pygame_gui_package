import time

import pygame,sys
from src.pyg_gui.gui_elements.button import Button

def test(atr):
    print(atr[0])

def k(atr):
    print(atr[0])



pygame.init()
window = pygame.display.set_mode((1000,800))
button = Button(window,(10,300),(400,36),(130,44,111),listeners=[test,k],listener_atributes=[("1"),("2")])

buttons = [button]
def update_buttons(buttons):
    for i in buttons:
        i.update()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    update_buttons(buttons)

    pygame.display.flip()
    pygame.display.update()
    time.sleep(1 / 60)

