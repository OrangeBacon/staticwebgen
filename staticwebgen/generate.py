import shutil
import time
import datetime
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def generate(config):
    if config["general"]["mode"] == "build":
        createSite(config)
    elif config["general"]["mode"] == "watch":
        createSite(config)
        obs = Observer()
        handler = SiteGeneratorWatcher(config)
        path = config["general"]["sourceDir"]
        obs.schedule(handler, str(path), recursive=True, )
        obs.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            obs.stop()
            obs.join()

def createSite(config):
    try:
        shutil.rmtree(config["general"]["sourceDir"]/config["general"]["buildDir"])
        shutil.copytree(config["general"]["sourceDir"],
            config["general"]["sourceDir"]/config["general"]["buildDir"])
        print(f"[{datetime.datetime.now()}] Built site")
    except Exception as e:
        print(e)

class SiteGeneratorWatcher(FileSystemEventHandler):
    def __init__(self, config):
        self.config = config

    def on_any_event(self, e):
        if not path_in_or_is_path(Path(e.src_path),
            self.config["general"]["sourceDir"]/self.config["general"]["buildDir"]):
            createSite(self.config)

def path_in_or_is_path(test, location):
    if test == location:
        return True
    for p in test.parents:
        if p == location:
            return True
    return False