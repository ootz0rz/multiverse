from PCStatBase import *

class PCStatDEX(PCStatBase):

    def __init__(self, PC):
        self.PC = PC
        
        self.short = "DEX"
        PCStatBase.__init__(self, "Dexterity")