import numpy as np
from a_estrela_node import aEstrelaNode
import fases


class aEstrela():
    def __init__(self, mapa):
        self.node = np.array([[aEstrelaNode(i, j) for j in range(18)] for i in range(17)])
        self.currentNode = None
        self.startNode = None
        self.goalNode = None

        self.openList = []
        self.checkedList = []

        self.goalReached = False

        self.mapa = mapa
        self.set_matriz()

    def setStartNode(self, x, y):
        self.node[x][y].setStart()
        self.startNode = self.node[x][y]
        self.currentNode = self.node[x][y]
        self.openNode(self.currentNode)

    def setGoalNode(self, x, y):
        self.node[x][y].setGoal()
        self.goalNode = self.node[x][y]

    def setSolidNode(self, x, y):
        self.node[x][y].setSolid()

    def getCost(self, node):
        xDistance = abs(node.col - self.startNode.col)
        yDistance = abs(node.row - self.startNode.row)

        node.gcost = xDistance + yDistance

        xDistance = abs(node.col - self.goalNode.col)
        yDistance = abs(node.row - self.goalNode.row)

        node.hcost = xDistance + yDistance

        node.fcost = node.gcost + node.hcost

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
        while self.goalReached == False and self.currentNode:

            if self.currentNode == self.goalNode:
                self.goalReached = True
                self.trackPath()
                break

            col = self.currentNode.col
            row = self.currentNode.row

            self.currentNode.setChecked()
            self.checkedList.append(self.currentNode)
            self.openList.remove(self.currentNode)

            if row - 1 >= 0:
                if not self.node[col][row - 1].solid:
                    self.openNode(self.node[col][row - 1])
            if col - 1 >= 0:
                if not self.node[col - 1][row].solid:
                    self.openNode(self.node[col - 1][row])
            if row + 1 <= len(self.node[0]) - 1:
                if not self.node[col][row + 1].solid:
                    self.openNode(self.node[col][row + 1])
            if col + 1 <= len(self.node) - 1:
                if not self.node[col + 1][row].solid:
                    self.openNode(self.node[col + 1][row])

            bestNode = None
            bestNodeCost = 999

            for i in self.openList:
                if i.fcost < bestNodeCost:
                    bestNode = i
                    bestNodeCost = i.fcost
                elif i.fcost == bestNodeCost:
                    if i.gcost < bestNode.gcost:
                        bestNode = i

            self.currentNode = bestNode

    def openNode(self, node):
        if node.open == False and node.checked == False and node.solid == False:
            node.setOpen()
            node.parent = self.currentNode
            self.openList.append(node)

    def trackPath(self):
        current = self.goalNode

        while current != self.startNode:
            current.setAsPath()
            current = current.parent

    def reset(self):
        for i in self.node:
            for j in i:
                j.start = False
                j.goal = False
                j.path = False
                j.parent = None
                j.open = False
                j.checked = False

        self.openList.clear()
        self.checkedList.clear()
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

    def set_matriz(self):  # valores = matriz

        valores = self.mapa

        for i in range(len(valores)):
            for j in range(len(valores[0])):
                if valores[i][j] == 1:
                    self.setSolidNode(j, i)


