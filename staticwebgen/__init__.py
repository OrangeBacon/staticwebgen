from staticwebgen.config import configure, format_config
from staticwebgen.generate import generate

def version():
    return "0.0.3"

def run(*args, **kwargs):
    config = format_config(configure(*args, **kwargs))
    if config is None:
        return

    generate(config)

if __name__ == "__main__":
    import staticwebgen.command_line
    staticwebgen.command_line.main("./example")