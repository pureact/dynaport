import sys
import json
import os

if sys.version_info[0] >= 3:
    if sys.version_info[1] == 3 or sys.version_info[1] == 4:
        from util.get_module3334 import _get_module
    else:
        from util.get_module35 import _get_module
else:
    from util.get_module2 import _get_module


class Dynaport:
    def __init__(self, **options):
        self.config = options.get("config", False)
        if self.config:
            self.set_config(config=self.config)

    def _get_module(self, name, path):
        module = _get_module(name, path)

        return module

    def get_config(self, **options):
        return self.config

    def set_config(self, **options):
        config = options.get("config", False)

        if not config:
            return

        if isinstance(config, dict):
            self.config = config
        else:
            config = os.path.expandvars(config)
            with open(config, "r") as f:
                self.config = json.load(f)

    def get_module(self, **options):
        if not options.get("name") and not options.get("path") and not self.config:
            raise AttributeError

        if options.get("name") and options.get("path"):
            return self._get_module(
                options.get("name"), os.path.expandvars(options.get("path"))
            )

        return self._get_module(
            options.get("name"),
            os.path.expandvars(self.config.get("modules", {}).get(options.get("name"))),
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
