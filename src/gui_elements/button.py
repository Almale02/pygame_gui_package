import pygame
window = pygame.display.set_mode((1000,800))

class Button:
    def __init__(self,window,pos,size,listeners,colour,on_press_colour,on_mouse_over_colour,txt, listener_atributes = ()):
        self.window = window
        self.pos = pos
        self.size = size
        self.listeners = listeners
        self.colour = colour
        self.on_press_colour = on_press_colour
        self.on_mouse_over_colour = on_mouse_over_colour
        self.txt = txt
        self.listener_atributes = listener_atributes

    def draw(self):
        pass

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()


