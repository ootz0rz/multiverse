from PCStatBase import *

class PCStatSTR(PCStatBase):

    def __init__(self, PC):
        self.PC = PC
        
        self.short = "STR"
        PCStatBase.__init__(self, "Strength")