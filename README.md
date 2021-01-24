# dynaport

Dynaport serves as a python module that will enable you to dynamically import modules from anywhere on the filesystem. This module acts as a wrapper of the python import library to offer an easy to use syntax for dynamically importing modules in python. Dynaport is able to support Python2, Python3.3, Python3.4, and Python3.5+ automatically.

# installation

`pip3 install dynaport`

# importing

`from dynaport.dynaport import Dynaport`

# functions

`Dynaport(config="/path/to/config.json")`

- instantiation of the Dynaport class, has an optional parameter `config` to load a config file. The config parameter can also take a dict as input. Needs to follow the same structure as the config file.

`Dynaport.get_module(name="module_name", path="/path/to/module.py")`

- loads and returns the module

`Dynaport.get_modules(modules=["module1", "module2", "module3"], dict=True)`

- loads and returns multiple modules as a tuple, optional `dict` param to load the modules into a dict.
- NOTE: module names need to be unique or else they will be overwritten when creating the dict

`Dynaport.get_config()`

- returns the loaded config file

`Dynaport.set_config(config=/path/to/config.json")`

- same behavior as loading a config on instantiation

# config file

Dynaport is able to use a json configuration file to define filepaths to modules you want to import.

The current format of the configuration file is as follows:

```json
{
    "modules": {
        "module_name": "/path/to/module.py"
    }
}
```

## features

- all paths can have environment variables put in the path names. Windows can have %name% and Linux can have $name

## future work

- add support for yaml files (but not require the dependency to be installed)
