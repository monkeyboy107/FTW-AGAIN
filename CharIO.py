from CharCreator import *
from atexit import register
import yaml


class ImportChars:
    def __init__(self):
        print('Init ImportChars')
        self.name = None
        self.health = None
        self.defence = None
        self.attack = None
        self.damage = None
        self.char = None
        self.chars_list = []
        self.chars = []
        self.packed_chars = None
        self.loaded_chars = []
        self.count = 0
        try:
            self.import_chars()
        except TypeError:
            None
        except yaml.parser.ParserError:
            None
        except AttributeError:
            None
        register(self.save_chars, self.loaded_chars)

    def import_chars(self):
        print('Importing chars')
        file = 'chars.yml'
        try:
            with open(file, 'r') as data:
                self.packed_chars = yaml.load(data)
                self.char_loader()
        except FileNotFoundError:
            self.export_chars()
        print(self.packed_chars)

    def export_chars(self):
        print('Exporting chars')
        with open('chars.yml', 'w+') as chars:
            yaml.dump(self.chars, chars)

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

    def save_chars(self, chars):
        print('Saving Chars')
        if isinstance(chars, list):
            print(len(chars))
            for i in chars:
                print(self.count)
                self.make_dict(name=i.name, health=i.health, defence=i.defence, attack=i.attack,
                               damage=i.damage)
                self.chars = {'Characters': self.chars_list}
            self.export_chars()
        else:
            print("Expecting object or list ", end='')
            raise TypeError

    def append_chars(self, chars):
        print('Appending chars')
        if isinstance(chars, list):
            for i in chars:
                self.loaded_chars.append(i)
        elif isinstance(chars, object):
            self.append_chars([chars])
        else:
            raise TypeError

    def char_loader(self):
        print('Loading chars')
        unpacked_chars = []
        for i in self.packed_chars:
            values = self.packed_chars.get(i)
        for i in values:
            unpacked_chars.append(BaseChar(attack=i.get('attack'), name=i.get('name'), health=i.get('health'),
                                           defence=i.get('defence'), damage=i.get('damage')))
        self.append_chars(unpacked_chars)
