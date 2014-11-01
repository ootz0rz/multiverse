from PCStatBase import *

class PCStat(PCStatBase):

    def __init__(self, name, short):
        self.short = short

        PCStatBase.__init__(self, name)