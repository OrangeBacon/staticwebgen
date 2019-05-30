import argparse
import sys
import configparser
from pathlib import Path

import staticwebgen

def default_config():
    return {
        "general": {
            "sourceDir": (Path, Path(".")),
            "configFile": (Path, Path("config.ini")),
            "buildDir": (Path, Path("build")),
            "mode": (Mode, "build")
        },
        "sections": {
            "default": (Path, Path("./layout"))
        }
    }

def Mode(string):
    if not(string == "build" or string == "watch"):
        raise ValueError(f"{string} is not a valid mode")
    return string

def configure(*args, **kwargs):
    parser = argparse.ArgumentParser(description="Generate a static website", prog=Path(args[0]).name)

    parser.add_argument("sourceDir", nargs="?", default=".",
        help="where is the static site located (default = .)")
    parser.add_argument("--config", "-c", default="config.ini", dest="configFile",
        help="file name of the configuration within the site directory (default = 'config.ini')")
    parser.add_argument("--mode", "-m", default="build",
        help="Runtime mode ('watch' or 'build'")
    parser.add_argument("--version", "-v",
        action="version", version=f"Staticwebgen {staticwebgen.version()}")
    
    cmd_args = parser.parse_args(args[1:])

    if not is_directory(cmd_args.sourceDir):
        return None
    if not is_file(Path(cmd_args.sourceDir)/Path(cmd_args.configFile)):
        return None
    
    parser = configparser.ConfigParser(strict=True, delimiters=("="), comment_prefixes=("#"))
    parser.BOOLEAN_STATES = {"True": True, "true": True, "False": False, "false": False}
    try:
        parser.read(Path(cmd_args.sourceDir)/Path(cmd_args.configFile))
    except configparser.Error as e:
        print(e.message, file=sys.stderr)
        return None

    config = {s:dict(parser.items(s)) for s in parser.sections()}
    config.pop("DEFAULT", None)

    return {**config, "general": vars(cmd_args), **kwargs}

def format_config(config):
    if config is None:
        return
    
    default = default_config()
    config = check_dictionary(config, default)
    return config

def check_dictionary(config, default):
    if config is None:
        return None
    
    errored = False
    for key, value in default.items():
        if key in config:
            if type(default[key]) is dict:
                if type(config[key]) is dict:
                    update = check_dictionary(config[key], default[key])
                    if update is None:
                        errored = True
                    else:
                        config[key] = update
                else:
                    print("Error: key '", key, "' should be a dictionary, got '",
                        str(type(config[key])), "'",sep="", file=sys.stderr)
                    errored = True
            else: 
                try:
                    config[key] = value[0](config[key])
                except Exception as e:
                    print("Error: ", str(e),  " for key '", key, "'", file=sys.stderr, sep="")
                    errored = True
        else:
            if type(default[key]) is dict:
                config[key] = check_dictionary({}, value)
            else:
                config[key] = value[1]


    for key, _ in config.items():
        if key not in default:
            print("Error: key '", key, "' not recognised", file=sys.stderr, sep="")
            errored = True

    return config if not errored else None

def is_directory(path):
    if type(path) is str:
        path = Path(path)

    if not path.exists():
        print(f"Error: path {path} does not exist", file=sys.stderr)
        return False

    if not path.is_dir():
        print(f"Error: path {path} is not a directory", file=sys.stderr)
        return False

    return True

def is_file(path):
    if type(path) is str:
        path = Path(path)

    if not path.exists():
        print(f"Error: path {path} does not exist", file=sys.stderr)
        return False

    if not path.is_file():
        print(f"Error: path {path} is not a directory", file=sys.stderr)
        return False

    return True