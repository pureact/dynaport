import imp


def _get_module(name, location):
    module = imp.load_source(name, location)

    return module
