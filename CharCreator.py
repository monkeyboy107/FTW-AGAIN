from random import randrange

class TemplateChar:
    """
    This is just the template to make the chars available easily.
    args: name, health, defence, attack, damage
    """
    def __init__(self, name=None, health=None, defence=None, attack=None, damage=None):
        print('Char init')
        self.name = name
        self.health = health
        self.defence = defence
        self.attack = attack
        self.damage = damage

    def take_dam(self, dam):
        print(self.name, 'is taking damage')
        health = self.health
        health = health - dam
        self.health = health
        print(self.health, self.name)

    def dam_dealt(self):
        print(self.name, 'is attacking')
        return randrange(1, 20, 1)


class BaseChar(TemplateChar):
    """
    This is just the template to make the chars available easily.
    args: name, health, defence, attack, damage
    """
    def __init__(self, name=None, health=100, defence=100, attack=100, damage=100):
        self.name = name
        self.health = health
        self.defence = defence
        self.attack = attack
        self.damage = damage


