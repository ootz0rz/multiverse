class PCStatBase(object):

    def __init__(self, PC, name, short):
        self.PC = PC
        self.name = name
        self.short = short

        # defaults
        self.base = 10
        self.bonus = 0
        self.equip = 0

    @property
    def base(self):
        return self._base
    @base.setter
    def base(self, value):
        self._base = value
    
    @property
    def bonus(self):
        return self._bonus
    @bonus.setter
    def bonus(self, value):
        self._bonus = value

    @property
    def equip(self):
        return self._equip
    @equip.setter
    def equip(self, value):
        self._equip = value

    @property
    def total(self):
        return self.base + self.bonus + self.equip