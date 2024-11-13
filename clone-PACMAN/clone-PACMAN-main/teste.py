import pygame

#Definições
altura = 576
largura = 544

def desenha_matriz(screen, matriz, cell_size=32):
    """
    Função para desenhar uma matriz binária na tela.

    Parâmetros:
    - screen: a tela de exibição do Pygame.
    - matriz: uma lista de listas que representa a matriz binária.
    - cell_size: o tamanho dos lados de cada célula na matriz (opcional, padrão é 20).
    """
    screen.fill((255, 255, 255))  # Limpa a tela com branco

    #cores
    preto = (0, 0, 0)
    branco = (255, 255, 255)
    azul = (100, 100, 255)

    for y, linha in enumerate(matriz):
        for x, valor in enumerate(linha):
            if valor == 1:
                pygame.draw.rect(screen, preto, (x * cell_size, y * cell_size, cell_size, cell_size))
            elif valor == 2:
                pygame.draw.rect(screen, azul, (x * cell_size, y * cell_size, cell_size, cell_size))
            else:
                pygame.draw.rect(screen, branco, (x * cell_size, y * cell_size, cell_size, cell_size))

    pygame.display.flip()  # Atualiza a tela


# Inicialização do Pygame
pygame.init()
screen_size = (largura, altura)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Matriz Binária")

# Exemplo de matriz binária
matriz = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    desenha_matriz(screen, matriz)  # Chama a função para desenhar a matriz

pygame.quit()
