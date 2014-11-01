from PCStatBase import *

class PCStatPERC(PCStatBase):

    def __init__(self, PC):
        self.PC = PC
        
        self.short = "PERC"
        PCStatBase.__init__(self, "Perception")