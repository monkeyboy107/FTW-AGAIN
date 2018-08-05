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


class ImportChars:
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
        self.char_loader()


    def export_chars(self):
        print('Exporting chars', self.chars)
        with open('chars.yml', 'w+') as chars:
            print(yaml.dump(self.chars, chars))

    def make_dict(self, name=None, health=None, defence=None, attack=None, damage=None):
        print('Making dictionary')
        self.chars_list.append({
            'name': name,
            'health': health,
            'defence': defence,
            'attack': attack,
            'damage': damage
        },
        )
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

    def append_chars(self, chars):
        if isinstance(chars, list):
            for i in chars:
                self.chars.append(i)
        elif isinstance(chars, str):
            self.append_chars([chars])
        else:
            raise TypeError
        self.save_chars(self.chars)

    def char_loader(self):
        print('Loading chars')
        unpacked_chars = []
        for i in self.packed_chars:
            values = self.packed_chars.get(i)
        for i in values:
            unpacked_chars.append(BaseChar(attack=i.get('attack'), name=i.get('name'), health=i.get('health'), defence=i.get('defence'), damage=i.get('damage')))
        print(unpacked_chars)


def main():
    print('Main')
    imports = ImportChars()
    bob = BaseChar(name='Bob')
    frank = BaseChar(name='Frank')
    imports.append_chars([bob, frank])
    imports.import_chars()


if __name__ == '__main__':
    main()

##########################
