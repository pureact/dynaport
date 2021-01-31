import sys
import json
import os

if sys.version_info[0] >= 3:
    if sys.version_info[1] == 3 or sys.version_info[1] == 4:
        from importlib.machinery import SourceFileLoader

        def _get_module(name, location):
            module = SourceFileLoader(name, location).load_module()

            return module

    else:
        import importlib.util

        def _get_module(name, path):
            spec = importlib.util.spec_from_file_location(name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            return module


else:
    import imp

    def _get_module(name, location):
        module = imp.load_source(name, location)

        return module


class Dynaport:
    def __init__(self, **options):
        self.config = options.get("config", False)
        self.set_config(config=self.config)

    def _get_path(self, path):
        return os.path.expandvars(path)

    def _get_module(self, name, path):
        module = _get_module(name, self._get_path(path))
        return module

    def get_config(self, **options):
        return self.config

    def set_config(self, **options):
        if options.get("config", False) is False:
            return False

        if isinstance(options.get("config"), dict):
            self.config = config
        else:
            with open(self._get_path(options.get("config")), "r") as f:
                self.config = json.load(f)

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
