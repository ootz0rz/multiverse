from PCStatBase import *

class PCStatINT(PCStatBase):

    def __init__(self, PC):
        self.PC = PC
        
        self.short = "INT"
        PCStatBase.__init__(self, "Intelligence")