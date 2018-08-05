##########################
# Project: FTW Again
# Programmer: Isaac Kerley
# Date: 08/03/2018
##########################
# imports
import yaml
from CharCreator import *
from AttackEngine import *


##########################
# Main Code


class ImportChars():
    def __init__(self):
        self.name = None
        self.health = None
        self.defence = None
        self.attack = None
        self.damage = None
        self.char = None
        self.chars = []
        self.count = 0
        self.import_chars()

    def import_chars(self):
        print('Importing chars')
        try:
            with open('chars.yml', 'r+') as chars:
                print(yaml.load(chars))
        except:
            self.export_chars()

    def export_chars(self):
        print('Exporting chars')
        with open('chars.yml', 'w+') as chars:
            for i in self.chars:
                print(yaml.dump(i, chars))

    def make_dict(self, name=None, health=None, defence=None, attack=None, damage=None, count=None):
        print('Making dictionary')
        self.name = name
        self.health = health
        self.defence = defence
        self.attack = attack
        self.damage = damage
        num = count
        self.char = {num:
            [
                {'name': name},
                {'health': health},
                {'defence': defence},
                {'attack': attack},
                {'damage': damage}
            ]
        }
        self.chars.append(self.char)
        print(self.char)

    def save_char(self, char):
        char = [char]
        self.save_char(char)

    def save_chars(self, chars):
        for i in chars:
            self.count = self.count + 1
            print(self.count)
            self.make_dict(count=self.count, name=i.name, health=i.health, defence=i.defence, attack=i.attack,
                           damage=i.damage)
            self.export_chars()


def main():
    print('Main')
    imports = ImportChars()
    bob = BaseChar(name='Bob')
    frank = BaseChar(name='Frank')
    imports.save_chars([bob, frank])


if __name__ == '__main__':
    main()

##########################
