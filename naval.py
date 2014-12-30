"""Naval Fate.

Usage:
    naval_fate.py ship new <name>
    naval_fate.py ship <name> move <x> <y> [--speed=<kn>]

Options:
    -h, help        Show this screen
    --speed=<kn>    Speed in knots [default: 10].

"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='naval Fate 2.0')
    print(arguments)


