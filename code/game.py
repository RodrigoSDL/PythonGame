#ABA GAME, CHAMA BIBLIOTECA PYGAME, FAZ AS IMPORTAÇÕES DA PASTA CONST E MENU


import pygame


from code.const import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu

#CRIA CLASSE JOGOS
class Game:
    def __init__(self): #FAZ UMA DEFINIÇÃO DE  INICIALIZAÇÃO BLOQUEADA PARA SI MESMO (SELF)
        pygame.init() #INICIA PYGAME
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT)) #CONFIGURA UMA JANELA DE EXECUÇÃO

    def run(self, ): #FAZ DEFINIÇÕES PARA RODAR EM SI MESMO

        while True: #ENQUANTO FOR VERDADE CHAMA CHAMA JANELA DO MENU
            menu = Menu(self.window)
            menu_return = menu.run()


            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:

                level = Level(self.window, 'Level 1', menu_return)
                level_return = level.run()





            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # close window
                quit()  # end pygamer
            else:
                pass


