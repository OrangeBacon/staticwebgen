from staticwebgen.config import configure, format_config

def version():
    return "0.0.3"

def generate(*args, **kwargs):
    config = format_config(configure(*args, **kwargs))
    if config is None:
        return
    print(config)

if __name__ == "__main__":
    import staticwebgen.command_line
    staticwebgen.command_line.main("./example")