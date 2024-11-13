from botao import Botao
import random

linhas = 18
colunas = 17

class Fantasma:

    def __init__(self, index, algoritmo, velocidade, tamanho, tela, imagem, x, y, mapa):

        self.index = index
        self.algoritmo = algoritmo
        self.velocidade = velocidade
        self.tamanho = tamanho
        self.tela = tela
        self.mapa = mapa

        self.fantasma = Botao(x, y, tamanho, tamanho, imagem, self.tela, (243, 97, 255))
        self.acao = self.algoritmo.getNextMove([0,0], self.retorna_pos_matriz())

    #def limpa_vetor(self):
    #    return [False, False, False, False]

    def retorna_pos_matriz(self):

        # Obtém a posição central do fantasma
        pacman_centro_x = self.fantasma.getX() + self.tamanho / 2
        pacman_centro_y = self.fantasma.getY() + self.tamanho / 2

        # Converte a posição para índices da matriz
        coluna = int(pacman_centro_x // self.tamanho)
        linha = int(pacman_centro_y // self.tamanho)

        return [coluna, linha]

    def update(self, pos_pacman):

        #pega pos do fantasma na matriz
        self.coluna, self.linha = self.retorna_pos_matriz()
        #print("coluna: " + str(self.coluna) + " - linha: " + str(self.linha))


        #atualiza quando o fantasma estiver exatamente no centro do objeto
        if self.fantasma.x % self.tamanho == 0:           #confere x
            if self.fantasma.y % self.tamanho == 0:       #confere y

                #confere colisões
                #if self.algoritmo.goalReached == False:
                self.acao = self.algoritmo.getNextMove(pos_pacman, self.retorna_pos_matriz())
                #self.algoritmo.exibir_mapa()
                self.confere_colisao()
                #pega movimentacao
                #print(self.acao)


        #move
        self.move()

    def move(self):
        # velocidade
        if self.acao[0]:
            self.fantasma.setX(self.fantasma.getX() + self.velocidade)

        if self.acao[1]:
            self.fantasma.setX(self.fantasma.getX() - self.velocidade)

        if self.acao[2]:
            self.fantasma.setY(self.fantasma.getY() - self.velocidade)

        if self.acao[3]:
            self.fantasma.setY(self.fantasma.getY() + self.velocidade)

    def confere_colisao(self):

        if self.coluna != colunas - 1:
            #direita
            if self.mapa[self.linha][self.coluna + 1] == 1: #confere se o bloco a direita é parede
                self.acao[0] = False
        else:
            if self.linha == 8 and self.acao[0]: #portal direita
                self.fantasma.setX(0)
            else:
                self.acao[0] = False

        if self.coluna != 0:
            # esquerda
            if self.mapa[self.linha][self.coluna - 1] == 1: # confere se o bloco a esquerda é parede
                self.acao[1] = False
        else:
            if self.linha == 8 and self.acao[1]:  # portal direita
                self.fantasma.setX(self.tamanho * (colunas - 1))
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


class FantasmaRandom:

    def __init__(self, index, algoritmo, velocidade, tamanho, tela, imagem, x, y, mapa):

        self.index = index
        self.algoritmo = algoritmo
        self.velocidade = velocidade
        self.tamanho = tamanho
        self.tela = tela
        self.mapa = mapa

        self.fantasma = Botao(x, y, tamanho, tamanho, imagem, self.tela, (243, 97, 255))
        self.acao = self.algoritmo.getNextMove([0, 0], self.retorna_pos_matriz())

    # def limpa_vetor(self):
    #    return [False, False, False, False]

    def retorna_pos_matriz(self):

        # Obtém a posição central do fantasma
        pacman_centro_x = self.fantasma.getX() + self.tamanho / 2
        pacman_centro_y = self.fantasma.getY() + self.tamanho / 2

        # Converte a posição para índices da matriz
        coluna = int(pacman_centro_x // self.tamanho)
        linha = int(pacman_centro_y // self.tamanho)

        return [coluna, linha]

    def update(self, pos_pacman):

        # pega pos do fantasma na matriz
        self.coluna, self.linha = self.retorna_pos_matriz()
        # print("coluna: " + str(self.coluna) + " - linha: " + str(self.linha))

        predict = self.updatePredict(pos_pacman)

        # atualiza quando o fantasma estiver exatamente no centro do objeto
        if self.fantasma.x % self.tamanho == 0:  # confere x
            if self.fantasma.y % self.tamanho == 0:  # confere y

                # confere colisões
                # if self.algoritmo.goalReached == False:
                self.acao = self.algoritmo.getNextMove(predict, self.retorna_pos_matriz())
                # self.algoritmo.exibir_mapa()
                #self.confere_colisao()
                # pega movimentacao
                # print(self.acao)

        # move
        # print(self.algoritmo)
        self.move()

    def updatePredict(self, pos_pacman):
        # Gera uma posição inicial de previsão com deslocamento aleatório de -3 a 3 em cada eixo
        predict = [pos_pacman[0] + random.randint(-3, 3), pos_pacman[1] + random.randint(-3, 3)]

        # Verifica se a posição está fora dos limites ou se é sólida
        while not (1 <= predict[0] <= 16 and 1 <= predict[1] <= 17) or self.algoritmo.node[predict[0]][
            predict[1]].solid:
            # Gera uma nova posição aleatória se estiver fora dos limites ou sólida
            predict = [pos_pacman[0] + random.randint(-3, 3), pos_pacman[1] + random.randint(-3, 3)]

        return predict

    def get_random_node(matrix):
        while True:

            col = random.randint(0, 16)  # 17 colunas, índices de 0 a 16
            row = random.randint(0, 17)  # 18 linhas, índices de 0 a 17

            if not matrix[col][row].solid:
                return matrix[col][row]

    def move(self):
        # velocidade
        if self.acao[0]:
            self.fantasma.setX(self.fantasma.getX() + self.velocidade)

        if self.acao[1]:
            self.fantasma.setX(self.fantasma.getX() - self.velocidade)

        if self.acao[2]:
            self.fantasma.setY(self.fantasma.getY() - self.velocidade)

        if self.acao[3]:
            self.fantasma.setY(self.fantasma.getY() + self.velocidade)

    def confere_colisao(self):

        if self.coluna != colunas - 1:
            # direita
            if self.mapa[self.linha][self.coluna + 1] == 1:  # confere se o bloco a direita é parede
                self.acao[0] = False
        else:
            if self.linha == 8 and self.acao[0]:  # portal direita
                self.fantasma.setX(0)
            else:
                self.acao[0] = False

        if self.coluna != 0:
            # esquerda
            if self.mapa[self.linha][self.coluna - 1] == 1:  # confere se o bloco a esquerda é parede
                self.acao[1] = False
        else:
            if self.linha == 8 and self.acao[1]:  # portal direita
                self.fantasma.setX(self.tamanho * (colunas - 1))
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


