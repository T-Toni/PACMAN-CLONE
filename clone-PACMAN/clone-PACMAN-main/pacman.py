from botao import Botao
import pygame
import fases
from spritesheet import SpriteSheet
from obj_animado import ObjAnimado

linhas = 18
colunas = 17
class Pacman:

    def __init__(self, tamanho, tela, opc):

        self.tela = tela
        self.mapa = fases.retorna_fase(opc)
        self.tamanho = tamanho
        self.pacman = Botao(0, 0, tamanho, tamanho, None, self.tela, (243, 97, 255))
        self.invertido = False

        # backgound (obj animado)
        pacman_sheet_img = pygame.image.load("imagens/pacman-sheet.png")
        # cria um objeto "SpriteSheet" (spritesheet, numero total de frames)
        self.pacman_sheet_obj = SpriteSheet(pacman_sheet_img, 6)
        # cria um objeto "ObjAnimado" que é capaz de rodar a animação                            #codigo do rosa usado para transparencia
        self.obj = ObjAnimado(self.tela, self.pacman_sheet_obj, 16,16, 3 / 1.2, (255, 0, 0), 0.5)

        self.obj.anima(self.pacman.x, self.pacman.y)
        self.obj.loop()

        self.velocidade = 4

        self.coluna = 0
        self.linha = 0

        #Direita - Esquerda - Cima - Baixo
        self.acao = [False, False, False, False]

    def limpa_vetor(self):
        return [False, False, False, False]

    def desenha(self):
        self.obj.update(self.pacman.x, self.pacman.y)

    def update(self):

        #pega pos do pacman na matriz
        self.coluna, self.linha = self.retorna_pos_matriz()
        #print("coluna: " + str(self.coluna) + " - linha: " + str(self.linha))
        # CONTROLES - o pacman deve sempre se mover
        # horizontal
        # direita

        self.gera_comando()

        #atualiza quando o pacman estiver exatamente no centro do objeto
        if self.pacman.x % self.tamanho == 0:           #confere x
            if self.pacman.y % self.tamanho == 0:       #confere y

                #confere colisões
                self.confere_colisao()


        #move
        self.move()

        if self.acao[0]:
            self.invertido = False
        elif self.acao[1]:
            self.invertido = True

        self.obj.set_invertido(self.invertido)

    def gera_comando(self):
        teclas = pygame.key.get_pressed()

        if self.coluna != colunas - 1:
            if teclas[pygame.K_d] and not self.mapa[self.linha][self.coluna + 1] == 1:
                self.acao = self.limpa_vetor()
                self.acao[0] = True
                self.pacman.invertido = False
                self.pacman.y = self.linha * self.tamanho

        if self.coluna != 0:
            # esquerda
            if teclas[pygame.K_a] and not self.mapa[self.linha][self.coluna - 1] == 1:
                self.acao = self.limpa_vetor()
                self.acao[1] = True
                self.pacman.invertido = True
                self.pacman.y = self.linha * self.tamanho

        #Vertical
        # cima
        if self.linha != 0:
            if teclas[pygame.K_w] and not self.mapa[self.linha - 1][self.coluna] == 1:
                self.acao = self.limpa_vetor()
                self.acao[2] = True
                self.pacman.x = self.coluna * self.tamanho

        if self.linha != linhas - 1:
            #baixo
            if teclas[pygame.K_s] and not self.mapa[self.linha + 1][self.coluna] == 1:
                self.acao = self.limpa_vetor()
                self.acao[3] = True
                self.pacman.x = self.coluna * self.tamanho

    def move(self):
        # velocidade
        #move o pacman a partir da ação
        if self.acao[0]:
            self.pacman.setX(self.pacman.getX() + self.velocidade)

        if self.acao[1]:
            self.pacman.setX(self.pacman.getX() - self.velocidade)

        if self.acao[2]:
            self.pacman.setY(self.pacman.getY() - self.velocidade)

        if self.acao[3]:
            self.pacman.setY(self.pacman.getY() + self.velocidade)

    def retorna_pos_matriz(self):

        # Obtém a posição central do Pacman
        pacman_centro_x = self.pacman.getX() + self.tamanho / 2
        pacman_centro_y = self.pacman.getY() + self.tamanho / 2

        # Converte a posição para índices da matriz
        coluna = int(pacman_centro_x // self.tamanho)
        linha = int(pacman_centro_y // self.tamanho)

        return [coluna, linha]

    def confere_colisao(self):

        if self.coluna != colunas - 1:
            #direita
            if self.mapa[self.linha][self.coluna + 1] == 1: #confere se o bloco a direita é parede
                self.acao[0] = False
        else:
            if self.linha == 8 and self.acao[0]: #portal direita
                self.pacman.setX(0)
            else:
                self.acao[0] = False

        if self.coluna != 0:
            # esquerda
            if self.mapa[self.linha][self.coluna - 1] == 1: # confere se o bloco a esquerda é parede
                self.acao[1] = False
        else:
            if self.linha == 8 and self.acao[1]:  # portal direita
                self.pacman.setX(self.tamanho * (colunas - 1))
            else:
                self.acao[1] = False

        if self.linha != 0:
            # cima
            if self.mapa[self.linha - 1][self.coluna] == 1:  # confere se o bloco a cima é parede
                self.acao[2] = False
        else:
            self.acao[2] = False

        if self.linha != linhas - 1:
            # baixo
            if self.mapa[self.linha + 1][self.coluna] == 1:  # confere se o bloco a baixo é parede
                self.acao[3] = False
        else:
            self.acao[3] = False

