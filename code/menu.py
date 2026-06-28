# CODIFICAÇÃO RELACIONADA AO MENU PRINCIPAL DO JOGO
import pygame.image  # IMPORTA BIBLIOTACA DO PYGAME.IMAGE PARA UTILIZAR AS IMAGENS
from pygame import Surface, Rect  # IMPORTA O COMANDO SURFACE QUE CHAMA UM RETANGULO PARA EXIBIR A APLICAÇÃO
from pygame.font import Font  # IMPORTA FONTES

from code.const import WINDOW_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE  # IMPORTA CONSTANTES DE DIMENSÃO


class Menu:  # INICIO DA CLASSE MENU
    def __init__(self, window):  # AUTO DEFINIÇÃO DE JANELA PARA RODAR A APLICAÇÃO (JOGO)
        self.window = window  # CHAMA PARA SI A FUNÇÃO DE ABRIR O TERMINAL DO JOGO (JANELA OU WINDIW)
        self.surf = pygame.image.load('./asset/Menu_background.png').convert_alpha()  # CHAMA SOBRE A JANELA UMA IMAGEM
        self.rect = self.surf.get_rect(left=0,
                                       top=0)  # ESTABELECE COMEÇO DA MARCAÇÃO DO RETANGULO CHAMADO ANTERIORMENTE

    def run(self, ):  # FAZ UMA AUTODEFINIÇÃO
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu_music.wav')  # CHAMA DA PASTA ASSET O ARQUIVO DE AUDIO INICIAL
        pygame.mixer_music.play(-1)  # CRIA UM LOOP COM O FINAL E COMEÇO DO ARQUIVO DE AUDIO

        while True:  # PARTE REFERENTE AO MENU INICIAL
            self.window.blit(source=self.surf, dest=self.rect)  # CHAMA O TITULO  DO JOGO SOBRE A IMAGEM

            # TETO DO MENU, TAMANHA, O TEXTO EM SI, COR DO TEXTO, POSICIONAMENTO DO TEXTO
            self.menu_text(text_size=50, text="Python", text_color=COLOR_ORANGE, text_center_pos=(WINDOW_WIDTH / 2, 70))
            self.menu_text(text_size=50, text="Game", text_color=COLOR_ORANGE, text_center_pos=(WINDOW_WIDTH / 2, 120))

            for i in range(len(MENU_OPTION)):  # AQUI TEMOS AS OPÇÕES DO MENU
                if i == menu_option:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_ORANGE,
                                   text_center_pos=(WINDOW_WIDTH / 2, 200 + 25 * i))
                else:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_WHITE,
                                   text_center_pos=(WINDOW_WIDTH / 2, 200 + 25 * i))

            # check for all events
            # AQUI COMECA A PARTE DE eventos,como encerrar O PROGRAMA, se mover no menu,etc...
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygamer

                if event.type == pygame.KEYDOWN:  # PRECISONA TECLA

                    if event.key == pygame.K_UP:  # REFERENTE A TECLA DE SETA PARA CIMA
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_RETURN:  # tecla enter
                        return MENU_OPTION[menu_option]

            pygame.display.flip()  # ATUALIZA CONSTANTEMENTE A TELA DO JOGO

    # CRIA AS DEFINIÇÕES DE TEXTO NO  MENU,
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
