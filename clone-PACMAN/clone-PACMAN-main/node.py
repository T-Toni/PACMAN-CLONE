class Node():
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.fcost = 0
        self.solid = False
    
    def setSolid(self):
        self.solid = True