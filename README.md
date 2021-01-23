# dynaport

Dynaport serves as a python module that will enable you to dynamically import modules from anywhere on the filesystem. This module acts as a wrapper of the python import library to offer an easy to use syntax for dynamically importing modules in python.

# basic usage

```python
dp = Dynaport()
my_module = dp.get_module(name="module_name", location="/path/to/module.py")
my_module.my_func()

dp_config = Dynaport("my_config.json")
my_other_module = dp_config.get_module(name="module_name") # path is retrieved from the config file
my_other_module.my_func()
```

# config file

Dyanport is able to use a json configuration file to define filepaths to modules you want to import.

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
