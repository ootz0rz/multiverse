from PCStats import PCStatDEX, PCStatPERC, PCStatVIT, PCStatSTR, PCStatINT, \
                    PCStatSCI, PCStatWILL

from PCClass import PCClassBase
from PCRace import PCRaceBase

from Loader import Loader

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

        # init races
        self._race_loader = Loader(PCRaceBase.PCRaceBase, "./PCRace")

        # init classes
        self._class_loader = Loader(PCClassBase.PCClassBase, "./PCClass")

    def run(self):
        '''
        Run all necessary calculations :o
        '''
        pass

    def get_class_types(self):
        '''
        Return a list of all valid classes.
        '''
        return [(c.name, c.short) for c in self._class_loader.get_classes()]

    def get_race_types(self):
        '''
        Return a list of all valid races.
        '''
        return [(c.name, c.short) for c in self._race_loader.get_classes()]

    def add_level(self, class_):
        print "Adding level:", class_
        pass