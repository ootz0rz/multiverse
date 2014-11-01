from PCStatBase import *

class PCStatVIT(PCStatBase):

    def __init__(self, PC):
        self.PC = PC
        
        self.short = "VIT"
        PCStatBase.__init__(self, "Vitality")