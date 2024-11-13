import numpy as np
from a_estrela_node import aEstrelaNode
import fases


class Guloso():
    def __init__(self, mapa):
        self.node = np.array([[aEstrelaNode(i, j) for j in range(18)] for i in range(17)])
        self.currentNode = None
        self.startNode = None
        self.goalNode = None

        self.goalReached = False

        self.set_matriz(mapa)
        self.mapa = mapa

    def setStartNode(self, x, y):
        self.node[x][y].setStart()
        self.startNode = self.node[x][y]
        self.currentNode = self.node[x][y]

    def setGoalNode(self, x, y):
        self.node[x][y].setGoal()
        self.goalNode = self.node[x][y]

    def setSolidNode(self, x, y):
        self.node[x][y].setSolid()

    def getCost(self, node):
        xDistance = abs(node.col - self.goalNode.col)
        yDistance = abs(node.row - self.goalNode.row)

        node.fcost = xDistance + yDistance

    def setCostOnNodes(self):
        for linha in self.node:
            for no in linha:
                self.getCost(no)

    def exibir_mapa(self):
        for linha in self.node:
            for no in linha:
                if no.solid:
                    print("██", end="")
                elif no.start:
                    print("ST", end="")
                elif no.goal:
                    print("GO", end="")
                else:
                    print(f"{no.fcost:02}", end="")
            print("")

    def search(self):

        if self.currentNode == self.goalNode:
            self.goalReached = True

        if self.goalReached == True:
            return

        col = self.currentNode.col
        row = self.currentNode.row

        decisionList = []

        if row - 1 >= 0:
            if not self.node[col][row - 1].solid:
                decisionList.append(self.node[col][row - 1])
        if col - 1 >= 0:
            if not self.node[col - 1][row].solid:
                decisionList.append(self.node[col - 1][row])
        if row + 1 <= len(self.node[0]) - 1:
            if not self.node[col][row + 1].solid:
                decisionList.append(self.node[col][row + 1])
        if col + 1 <= len(self.node) - 1:
            if not self.node[col + 1][row].solid:
                decisionList.append(self.node[col + 1][row])

        bestNode = min(decisionList, key=lambda x: x.fcost, default=None)

        self.currentNode = bestNode

        bestNode.path = True

    def reset(self):
        for i in self.node:
            for j in i:
                j.start = False
                j.goal = False
                j.path = False

        self.goalReached = False

    def getNextMove(self, target_position, current_position):

        self.setStartNode(current_position[0], current_position[1])
        self.setGoalNode(target_position[0], target_position[1])

        self.setCostOnNodes()
        self.search()

        col = self.startNode.col
        row = self.startNode.row

        if row - 1 >= 0:
            if self.node[col][row - 1].path == True:
                n = [False, False, True, False]
                #print(n)
                self.reset()
                return n
        if col - 1 >= 0:
            if self.node[col - 1][row].path == True:
                n = [False, True, False, False]
                #print(n)
                self.reset()
                return n
        if row + 1 <= len(self.node[0]) - 1:
            if self.node[col][row + 1].path == True:
                n = [False, False, False, True]
                #print(n)
                self.reset()
                return n
        if col + 1 <= len(self.node) - 1:
            if self.node[col + 1][row].path == True:
                n = [True, False, False, False]
                #print(n)
                self.reset()
                return n

        n = [False, False, False, False]
        print("nenhum caminho encontrado")
        self.reset()
        return n

    def set_matriz(self, mapa):  # valores = matriz

        valores = mapa

        for i in range(len(valores)):
            for j in range(len(valores[0])):
                if valores[i][j] == 1:
                    self.setSolidNode(j, i)
