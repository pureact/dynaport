from importlib.machinery import SourceFileLoader


def _get_module(name, location):
    module = SourceFileLoader(name, location).load_module()

    return module
