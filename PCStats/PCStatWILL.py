from PCStatBase import *

class PCStatWILL(PCStatBase):

    def __init__(self, PC):
        self.PC = PC
        
        self.short = "WILL"
        PCStatBase.__init__(self, "Will")