from PCStatBase import *

class PCStatSCI(PCStatBase):

    def __init__(self, PC):
        self.PC = PC
        
        self.short = "SCI"
        PCStatBase.__init__(self, "Science")