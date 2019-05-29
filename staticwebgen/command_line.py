import sys
from staticwebgen import generate

def main(*args, **kwargs):
    arguments = [*args, *sys.argv]
    generate(*arguments, **kwargs)