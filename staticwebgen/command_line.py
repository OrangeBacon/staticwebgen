import sys
from staticwebgen import generate

def main(*args, **kwargs):
    arguments = [*sys.argv, *args]
    generate(*arguments, **kwargs)