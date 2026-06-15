from turtledemo.clock import setup

import pygame
print('setup start')
pygame.init()

window = pygame.display.set_mode(size=(600,480))
print('setup end')

print('loop start')
while True:
#check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('quiting...')
            pygame.quit() #close window
            quit() #end pygame
