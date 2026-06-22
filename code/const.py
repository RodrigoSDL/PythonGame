import pygame
from pygame.examples.grid import WINDOW_WIDTH, WINDOW_HEIGHT

#c
COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)


#E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Fase_A_1':0,
    'Fase_A_2':1,
    'Fase_A_3':4,
    'Fase_A_4':6,
    'Fase_A_5':10,
    'Fase_A_6':5,
    'Fase_A_7':6,
    'Player1': 4,
    'Player2': 4,
    'Enemy1': 2,
    'Enemy2': 1,
}

#M
#CRIA AS OPÇOES DO MENU NUMA DECLARAÇÃO CHAMADA MENU_OPTION
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')
#P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                'Player2': pygame.K_LCTRL}

#S
SPAWN_TIME = 4000

#w
#ESTABELECE DEFINIÇÕES DO TAMANHO DA JANELA (MESMA PROPORÇÃO DA IMAGEM DO MENU INICIAL.
WINDOW_WIDTH =526
WINDOW_HEIGHT =324
