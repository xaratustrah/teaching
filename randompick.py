#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Choose a random name from a list on the command line, subtract each time.

Xaratustrah

November 2020

usage:

python randompick.py "Savannah Ava Scarlet Melissa Mollie"


"""

import numpy as np
import sys


def pick_someone(names):
    rnd = np.random.randint(len(names))
    print(names[rnd])
    try:
        input('Press enter for more, ctrl-d or ctrl-d to abort: ')
        names.pop(rnd)
        pick_someone(names)
    except (KeyboardInterrupt, EOFError, ValueError) as e:
        print('No names left or user cancelled. Aborting...')


def main():
    names = sys.argv[1].split()
    pick_someone(names)


# ------------------------

if __name__ == '__main__':
    main()
