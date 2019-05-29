import argparse
import sys
import configparser
from pathlib import Path

import staticwebgen

def configure(*args, **kwargs):
    parser = argparse.ArgumentParser(description = "Generate a static website", prog=Path(args[0]).name)
    parser.add_argument('directory', default=".")
    parser.add_argument('--config', '-c', default="config.ini")
    parser.add_argument('--version', '-v', action='version', version=f'Staticwebgen {staticwebgen.version()}')
    
    cmd_args = parser.parse_args(args[1:])
    if not is_directory(cmd_args.directory):
        return None
    if not is_file(Path(cmd_args.directory)/Path(cmd_args.config)):
        return None

    parser = configparser.ConfigParser()
    parser.read(Path(cmd_args.directory)/Path(cmd_args.config))

    config = {s:dict(parser.items(s)) for s in parser.sections()}
    config.pop("DEFAULT", None)

    return {**config, **vars(cmd_args)}

def is_directory(path):
    if type(path) is str:
        path = Path(path)

    if not path.exists():
        print(f"Error: path {path} provided does not exist", file=sys.stderr)
        return False

    if not path.is_dir():
        print(f"Error: path {path} provided is not a directory", file=sys.stderr)
        return False

    return True

def is_file(path):
    if type(path) is str:
        path = Path(path)

    if not path.exists():
        print(f"Error: path {path} provided does not exist", file=sys.stderr)
        return False

    if not path.is_file():
        print(f"Error: path {path} provided is not a directory", file=sys.stderr)
        return False

    return True