import sys
from staticwebgen import run

def main(*args, **kwargs):
    arguments = [*sys.argv, *args]
    run(*arguments, **kwargs)