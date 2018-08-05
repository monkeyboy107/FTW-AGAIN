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
        self.packed_chars = None
        self.count = 0
        try:
            self.import_chars()
        except TypeError:
            None

    def import_chars(self):
        print('Importing chars')
        try:
            with open('chars.yml', 'r') as data:
                self.packed_chars = yaml.load(data)
        except FileNotFoundError:
            self.export_chars()
        print(self.packed_chars)
        self.char_loader(self.packed_chars)


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
            print(self.count)
            self.make_dict(count=self.count, name=i.name, health=i.health, defence=i.defence, attack=i.attack,
                           damage=i.damage)
            self.export_chars()
            self.count += 1

    def char_loader(self, chars):
        name = None
        health = None
        defence = None
        attack = None
        damage = None
        deploy = []
        print('Loading chars')
        for i in range(len(chars)):
            print('')
            for j in chars[i]:
                print(j)
                if j.get('name') is not None:
                    name = j.get('name')
                if not j.get('health') is not None:
                     health = j.get('health')
                if not j.get('defence') is not None:
                    defence = j.get('defence')
                if not j.get('attack') is not None:
                     attack = j.get('attack')
                if not j.get('damage') is not None:
                    damage = j.get('damage')
            deploy.append(BaseChar(name=name, health=health, defence=defence, attack=attack, damage=damage))
            print(BaseChar(name=name, health=health, defence=defence, attack=attack, damage=damage))
        #self.chars = deploy
        for i in deploy:
            print(i)


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