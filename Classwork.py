class BaseCharacter(object):
    def __init__(self,name):
        self.name = name
    def printName(self):
        print self.name

class NonPlayable(BaseCharacter):
    def __init__(self,name):
        super(NonPlayable,self).__init__(name)
        self.friendly = Friendly
        self.enemy = Enemy

class Friendly(NonPlayable):
    def __init__(self,friendly):
        self.name = friendly
        
class Enemy(NonPlayable):
    def __init__(self,enemy):
        self.name = enemy
        self.dmg = 5

    
class Playable(BaseCharacter):
    def __init__(self,name,archer,mage,warrior):
        super(Playable,self).__init__(name)
        self.arhcer = archer
        self.mage = mage
        self.warrior = warrior

class Archer(Playable):
    def __init__(self,name,weapon):
        super(Archer,self).__init__(name)
        self.weapon = Weapon(weaponName)
        
        
class Mage(Playable):
    def __init__(self,mage):
        self.name = mage

class Warrior(Playable):
    def __init__(self,warrior):
        self.name = warrior

class Weapon:
    def __init__(self,weaponName):
        self.name = weaponName

fd = Friendly("Clerk")
em = Enemy("Deku Knight")
ar = Archer("Archer","Bow")
ma = Mage("Mage")
wa = Warrior("Warrior")
##fd.printName()
##em.printName()
##print em.dmg
ar.printName()
print ar.weapon.name
##ma.printName()
##wa.printName()

