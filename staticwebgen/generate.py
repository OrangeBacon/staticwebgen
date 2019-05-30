import shutil

def generate(config):
    print(config)
    try:
        shutil.rmtree(config["general"]["sourceDir"]/config["general"]["buildDir"])
        shutil.copytree(config["general"]["sourceDir"],
            config["general"]["sourceDir"]/config["general"]["buildDir"])
    except Exception as e:
        print(e)