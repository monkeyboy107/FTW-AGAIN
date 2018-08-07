##########################
# Project: FTW Again
# Programmer: Isaac Kerley
# Date: 08/03/2018
##########################
# imports
import yaml
from CharCreator import *
from AttackEngine import *
from CharIO import *

##########################
# Main Code


def main():
    print('Main')
    imports = ImportChars()
    bob = BaseChar(name='Bob')
    frank = BaseChar(name='Frank')
    imports.append_chars([bob, frank])


if __name__ == '__main__':
    main()

##########################
