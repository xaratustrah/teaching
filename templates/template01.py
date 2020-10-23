#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Here comes a short description of your code

Here comes your name

Here comes the year and month (no days)

Here comes how to run your code, like:

"""

# here come the imports

import numpy as np
import matplotlib.pyplot as plt
import sys


# here come some constants all in caps, units in comments
# here you can also define small classes, but that's another story

B_RHO = 18  # [Tm]


# here comes the "model" i.e. the computational engine, all in lower letters, with underscore, no caps

def get_magnetic_field(rho):
    return B_RHO / rho


def do_something_fancy(x, y, z=3):
    return x + y - z**2


# here comes the "view", i.e. anything related to the user input/output

def print_results(result, verbose=False):
    if not verbose:
        print(result)
    else:
        print('This is the result: ', result,
              'and by the way, actually my aunti Lili likes to have her cookies with Darjeeling tea, and you know what someone in her Yoga class said....')


def read_data_file(filename):
    print('Reading file: ' + filename)
    # return data vector
    return 42


# here comes the "controller" i.e. the manager part


def main():
    # pass the data filename from command line
    data = read_data_file(sys.argv[1])
    result = do_something_fancy(data, get_magnetic_field(18))
    print_results(result, verbose=True)


# ------------------------
# Do not change this following part, later you will see why it is here:

if __name__ == '__main__':
    main()
