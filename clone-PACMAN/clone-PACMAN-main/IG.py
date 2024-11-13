import pygame
import sys
import fases
from botao import Botao
from pacman import Pacman
from fantasmas import Fantasma
from fantasmas import FantasmaRandom
from a_estrela import aEstrela
from moeda import Moeda
from guloso import Guloso
from aestrelaborda import aEstrelaBorda

#Definições
altura = 864 / 1.2      #18 linhasd
largura = 816 / 1.2     #17 colunas
tamanho_tile = 48 / 1.2

FPS = 60

class IG:

    def __init__(self, opc):

        self.tela = pygame.display.set_mode((largura, altura))
        self.opc = opc  #define a fase a ser jogada

        #self.fantasmas = [fantasma1, fantasma2, fantasma3, fantasma4]
        self.pacman = Pacman(tamanho_tile, self.tela, self.opc)

        self.fase = fases.retorna_fase(opc)

        #algoritmos
        a_estrela = aEstrela(self.fase)
        guloso = Guloso(self.fase)
        a_estrela_borda = aEstrelaBorda(self.fase)

        self.bill = Fantasma(1, a_estrela, 1, tamanho_tile, self.tela, "imagens/bill.png", 8 * tamanho_tile, 8 * tamanho_tile, self.fase)
        self.receba = Fantasma(1, guloso, 2, tamanho_tile, self.tela, "imagens/receba.png", 9 * tamanho_tile, 8 * tamanho_tile, self.fase)
        self.djabo = Fantasma(1, a_estrela_borda, 2.5, tamanho_tile, self.tela, "imagens/djabo.png", 9 * tamanho_tile, 7 * tamanho_tile, self.fase)
        self.pinky = FantasmaRandom(1, a_estrela, 2, tamanho_tile, self.tela, "imagens/pinky.png", 10 * tamanho_tile, 8 * tamanho_tile, self.fase)


        #imagens
        self.vitoria = Botao(0, 0, largura, altura, "imagens/vitoria.png", self.tela, (243, 97, 255))
        self.derrota = Botao(0, 0, largura, altura, "imagens/derrota.png", self.tela, (243, 97, 255))

        self.lista_moedas = self.cria_moedas(self.fase)

        self.perdeu = False

    def desenha_matriz(self, cell_size=tamanho_tile):
        self.tela.fill((75, 0, 130))

        # cores
        preto = (0, 0, 0)
        branco = (255, 255, 255)
        azul = (100, 100, 255)

        for y, linha in enumerate(self.fase):
            for x, valor in enumerate(linha):
                if valor == 1:
                    pygame.draw.rect(self.tela, preto, (x * cell_size, y * cell_size, cell_size, cell_size))
                elif valor == 2:
                    pygame.draw.rect(self.tela, azul, (x * cell_size, y * cell_size, cell_size, cell_size))
                """else:
                    pygame.draw.rect(screen, branco, (x * cell_size, y * cell_size, cell_size, cell_size))
                """

    def update(self):

        self.desenha_matriz()
        self.pacman.desenha()
        self.desenha_moedas()

        #fantasmas
        self.bill.fantasma.desenha()
        self.receba.fantasma.desenha()
        self.pinky.fantasma.desenha()
        self.djabo.fantasma.desenha()

        #sself.atualiza_matriz()
        self.funcionamento_moedas()

        self.clock = pygame.time.Clock()

        pygame.display.flip()  # atualiza a tela

    def desenha_derrota(self):
        self.desenha_matriz()
        self.pacman.desenha()

        # fantasmas
        self.bill.fantasma.desenha()
        self.receba.fantasma.desenha()
        self.pinky.fantasma.desenha()
        self.djabo.fantasma.desenha()
        self.derrota.desenha()
        pygame.display.flip()

    def desenha_vitoria(self):
        self.desenha_matriz()
        self.pacman.desenha()

        # fantasmas
        self.bill.fantasma.desenha()
        self.receba.fantasma.desenha()
        self.pinky.fantasma.desenha()
        self.djabo.fantasma.desenha()
        self.vitoria.desenha()
        pygame.display.flip()


    def run(self):

        pygame.init()
        pygame.display.set_caption("PAC-MAN")
        #solucao = main.algoritmo_genetico(self.n, self.tamanho_populacao, self.taxa_mutacao, self.max_geracoes)

        while True:
            # Verifica eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #self.tela.fill((0, 0, 0))

            if len(self.lista_moedas) != 0 and not self.perdeu:

                pos_pacman = self.pacman.retorna_pos_matriz()

                self.pacman.update()
                self.bill.update(pos_pacman)
                self.receba.update(pos_pacman)
                self.pinky.update(pos_pacman)
                self.djabo.update(pos_pacman)

                #print(self.pacman.retorna_pos_matriz())
                #print(self.bill.retorna_pos_matriz())

                #confere a derrota
                self.confere_derrota()

                self.update()

                # Controla a taxa de quadros
                self.clock.tick(FPS)

            elif len(self.lista_moedas) == 0:
                self.desenha_vitoria()

            else:
                self.desenha_derrota()

    def cria_moedas(self, matriz):

        lista_moedas = []

        for y, linha in enumerate(matriz):
            for x, valor in enumerate(linha):
                if valor == 0:  # Assumindo que '0' indica uma posição onde há uma moeda
                    # Calcula a posição central do tile
                    centro_x = x * tamanho_tile + tamanho_tile // 4
                    centro_y = y * tamanho_tile + tamanho_tile // 4
                    # Cria uma nova moeda e adiciona à lista
                    nova_moeda = Moeda(centro_x, centro_y, self.tela)
                    lista_moedas.append(nova_moeda)

        return lista_moedas

    def desenha_moedas(self):

        for moeda in self.lista_moedas:
            moeda.desenha()

    def funcionamento_moedas(self):

        pos_pacman = self.pacman.retorna_pos_matriz()
        for moeda in self.lista_moedas:
            if moeda.tile[0] == pos_pacman[0]:
                if moeda.tile[1] == pos_pacman[1]:
                    self.lista_moedas.remove(moeda)

    def confere_derrota(self):

        bill = self.bill.retorna_pos_matriz()
        receba = self.receba.retorna_pos_matriz()
        pinky = self.pinky.retorna_pos_matriz()
        djabo = self.djabo.retorna_pos_matriz()

        vetor = [bill, receba, pinky, djabo]
        pos_pacman = self.pacman.retorna_pos_matriz()

        for fantasma in vetor:
            if fantasma == pos_pacman:
                self.perdeu = True

##roda

projeto = IG(2)
projeto.run()