code: true
lang: python

# Python

## Argparse
### Create parser
```
parser = argparse.ArgumentParser()
```

### Add mandatory argument
```
parser.add_argument('myargument')
```

### Add flag
```
parser.add_argument('-v', '--visualize', action='store_true')
```

### Parse arguments
```
args = parser.parse_args()
```

# Environments

* pyenv: multiple python versions
* venv: module for creating virtual package environments
* pyvenv: virtual package environments based on venv, part of Python >= 3.4
* virtualenv: virtual package environment, on PyPi

