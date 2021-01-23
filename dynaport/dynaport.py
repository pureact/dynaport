import importlib.util
import json


class Dynaport:
    def __init__(self, config=False):
        self.config = config
        if self.config:
            with open(self.config, "r") as f:
                self.config = json.load(f)

    def _get_module(self, name, location):
        spec = importlib.util.spec_from_file_location(name, location)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def get_module(self, **options):
        if not options.get("name") and not options.get("location") and not self.config:
            raise AttributeError

        if options.get("name") and options.get("location"):
            return self._get_module(options.get("name"), options.get("location"))

        return self._get_module(
            options.get("name"), self.config.get("modules", {}).get(options.get("name"))
        )
