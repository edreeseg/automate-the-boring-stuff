# Built-in functions
print()
input()
len()

# Standard library functions
import random
random.randint(1, 10)

import sys, os, math

from random import *
randint(1, 10)

sys.exit() # Exits program early

# Third-party modules
# Installed with the pip program

import pyperclip # Needs to be installed with pip

pyperclip.copy('Hello world!')
pyperclip.paste()

# Writing functions

def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

#

def hello(name):
    print('Hello ' + name)

hello('Alice')
hello('Bob')

#

def plusOne(number):
    return number + 1

#

# None is Python's version of null

print('Hello', end='') # Will pass along final character, to replace the default \n
print('cat', 'dog', 'mouse', sep='ABC') # Will indicate what to separate arguments with in string, replacing default ' '
