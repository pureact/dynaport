# dynaport

Dynaport serves as a python module that will enable you to dynamically import modules from anywhere on the filesystem. This module acts as a wrapper of the python import library to offer an easy to use syntax for dynamically importing modules in python.

# installation

`pip3 install dynaport`

# functions

`Dynaport(config="/path/to/config.json")`

- instantiaton of the Dynaport class, has an optional parameter `config` to load a config file.

`Dynaport.get_module(name="module_name", path="/path/to/module.py"`

- loads and returns the module

`Dynaport.get_modules(modules=["module1", "module2", "module3"], dict=True)`

- loads and returns multiple modules as a tuple, optional `dict` param to load the modules into a dict.
- NOTE: module names need to be unique or else they will be overwritten when creating the dict

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

## future work

- expand on the ability to define configuration files to quickly import modules
- allow paths with environment variables to be passed into the program
- creating compatible versions for both python2 and python3
- uploading the package to pip for easier access to its functionality
