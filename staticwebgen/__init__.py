from staticwebgen.config import configure

def version():
    return "0.0.3"

def generate(*args, **kwargs):
    config = configure(*args, **kwargs)
    if config is None:
        return
    print(config)