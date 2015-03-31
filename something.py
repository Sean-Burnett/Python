class Character(object):
    def __init__(self):
        self.name = name
        self.health = 100
    def printName(self):
        print self.name

class Blacksmith(Character):
    def __init__(self,blacksmith):
        self.name = blacksmith

bs = Blacksmith("blacksmith")
bs.printName()
##print bs.health
