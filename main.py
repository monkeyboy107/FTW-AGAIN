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
        self.chars_list = []
        self.chars = []
        self.packed_chars = None
        self.count = 0
        try:
            self.import_chars()
        except TypeError:
            None
        except yaml.parser.ParserError:
            None
        except AttributeError:
            None

    def import_chars(self):
        print('Importing chars')
        try:
            with open('chars.yml', 'r') as data:
                self.packed_chars = yaml.load(data)
        except FileNotFoundError:
            self.export_chars()
        print(self.packed_chars)

    def export_chars(self):
        print('Exporting chars', self.chars)
        with open('chars.yml', 'w+') as chars:
            print(yaml.dump(self.chars, chars))

    def make_dict(self, name=None, health=None, defence=None, attack=None, damage=None):
        print('Making dictionary')
        self.name = name
        self.health = health
        self.defence = defence
        self.attack = attack
        self.damage = damage
        self.chars_list.append({
            'name': name,
            'health': health,
            'defence': defence,
            'attack': attack,
            'damage': damage
        },
        )
        # self.chars.append(self.char)
        print(self.char)

    def save_char(self, char):
        char = [char]
        self.save_char(char)

    def save_chars(self, chars):
        for i in chars:
            print(self.count)
            self.make_dict(name=i.name, health=i.health, defence=i.defence, attack=i.attack,
                           damage=i.damage)
            self.chars = {'Characters': self.chars_list}
        self.export_chars()


def main():
    print('Main')
    imports = ImportChars()
    bob = BaseChar(name='Bob')
    frank = BaseChar(name='Frank')
    imports.save_chars([bob, frank])
    imports.import_chars()


if __name__ == '__main__':
    main()

##########################
