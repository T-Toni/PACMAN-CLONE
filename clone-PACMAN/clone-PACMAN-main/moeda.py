from botao import Botao
from pygame import draw

class Moeda():
    
    def __init__(self, x, y, tela):

        imagem = "imagens/moeda.png"
        tamanho = 48 / 1.2 / 2

        self.tamanho = tamanho / 6
        self.moeda = Botao(x, y, tamanho, tamanho, None, tela, (0, 0, 0))
        self.tela = tela

        # Obtém a posição central da moeda
        self.centro_x = x + tamanho / 2
        self.centro_y = y + tamanho / 2

        # Converte a posição para índices da matriz
        coluna = int(self.centro_x // tamanho / 2)
        linha = int(self.centro_y // tamanho / 2)

        self.tile = [coluna, linha]



    def desenha(self):

        dourado = (255, 215, 0)

        draw.circle(self.tela, dourado, (self.centro_x, self.centro_y), self.tamanho)

