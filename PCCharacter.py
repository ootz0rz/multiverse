from PCStats import PCStatDEX, PCStatPERC, PCStatVIT, PCStatSTR, PCStatINT, \
                    PCStatSCI, PCStatWILL

class PCCharacter(object):

    def __init__(self):
        # Basic bio info
        self.name = ""
        self.classPerLevel = []
        self.race = None
        self.age = 0
        self.gender = ""
        self.height = ""
        self.weight = ""

        self.DEX = PCStatDEX.PCStatDEX(self)
        self.PERC = PCStatPERC.PCStatPERC(self)
        self.VIT = PCStatVIT.PCStatVIT(self)
        self.STR = PCStatSTR.PCStatSTR(self)
        self.INT = PCStatINT.PCStatINT(self)
        self.SCI = PCStatSCI.PCStatSCI(self)
        self.WILL = PCStatWILL.PCStatWILL(self)

    def run(self):
        '''
        Run all necessary calculations :o
        '''
        pass

    def add_class(self, type):
        pass