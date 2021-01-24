import importlib.util
import json


class Dynaport:
    def __init__(self, **options):
        self.config = options.get("config", False)
        if self.config:
            with open(self.config, "r") as f:
                self.config = json.load(f)

    def _get_module(self, name, path):
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def get_module(self, **options):
        if not options.get("name") and not options.get("path") and not self.config:
            raise AttributeError

        if options.get("name") and options.get("path"):
            return self._get_module(options.get("name"), options.get("path"))

        return self._get_module(
            options.get("name"), self.config.get("modules", {}).get(options.get("name"))
        )

    def get_modules(self, **options):
        if not self.config or not options.get("modules"):
            raise AttributeError

        if options.get("dict") is True:
            module_dict = {}

            for module in options.get("modules"):
                module_dict[module] = self._get_module(
                    module, self.config.get("modules").get(module)
                )

            return module_dict

        module_list = []

        for module in options.get("modules"):
            module_list.append(
                self._get_module(module, self.config.get("modules").get(module))
            )

        return tuple(module_list)
