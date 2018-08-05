import random

class ComSim:
    def __init__(self, char_list):
        print('ComSim init')
        self.CharList = char_list
        self.chars = []

    def char_stat(self, name):
        print('Getting char_stats')
        chars = self.chars
        stat = None
        count = 0
        while count < len(chars):
            stat = chars[count].get(name)
            if stat is None:
                count = + 1
            else:
                break
        print(stat)
        return stat

    def is_dead(self):
        print('Is dead?')
        for i in range(len(self.CharList)):
            if self.CharList[i].health <= 0:
                del self.CharList[i]

    def health(self):
        print('Getting health')
        for i in self.CharList:
            print(i.name, i.health)

    def defence(self, defender, attacker):
        print('Defending')
        attack = attacker.attack + random.randrange(1, 20)
        dam = attacker.dam_dealt()
        print(attacker.name, 'damage is', dam, 'attack is', attack)
        if defender.defence <= attack:
            defender.take_dam(dam)

    def attack(self, attacker, defenders):
        print('Attack', attacker.name, end=' ')
        for i in defenders:
            print(i.name, end=' ')
        if isinstance(defenders, list):
            for i in defenders:
                self.defence(i, attacker)
        else:
            self.defence(defenders, attacker)
