import importlib.util


def dynaport(name, location):
    spec = importlib.util.spec_from_file_location(name, location)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    test = dynaport("test", "/home/naek/projects/test_dir/test.py")
    test.my_func("hello")
