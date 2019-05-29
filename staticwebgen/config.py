import argparse
import staticwebgen
from pathlib import Path

def configure(*args, **kwargs):
    parser = argparse.ArgumentParser(description = "Generate a static website", prog=Path(args[0]).name)
    parser.add_argument('directory', default=".")
    parser.add_argument('--config', '-c', default="config.ini")
    parser.add_argument('--version', '-v', action='version', version=f'Staticwebgen {staticwebgen.version()}')
    
    cmd_args = parser.parse_args(args[1:])

    return cmd_args