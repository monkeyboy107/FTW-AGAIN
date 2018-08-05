##########################
# Project: FTW Again
# Programmer: Isaac Kerley
# Date: 08/03/2018
##########################
# imports
import yaml
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
            print(yaml.load(chars))

    def make_dict(self, name=None, health=None, defence=None, attack=None, damage=None):
        print('Making dictionary')
        self.name = name
        self.health = health
        self.defence = defence
        self.attack = attack
        self.damage = damage
        self.char = ({'name': name}, {'health': health}, {'defence': defence}, {'attack': attack}, {'damage': damage})
        print(self.char)



def main():
    print('Main')
    imports = ImportChars()
    imports.make_dict()


if __name__ == '__main__':
    main()

##########################