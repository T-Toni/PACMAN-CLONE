from node import Node

class aEstrelaNode(Node):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.gcost = 0
        self.hcost = 0
        self.start = False
        self.goal = False
        self.open = False
        self.checked = False
        self.parent = None
        self.path = False
    
    def setGoal(self):
        self.goal = True
        
    def setStart(self):
        self.start = True
    
    def setOpen(self):
        self.open = True

    def setChecked(self):
        self.checked = True

    def setAsPath(self):
        self.path = True