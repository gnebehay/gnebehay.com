code: true

# Python

## Argparse
### Create parser
```{.python}
parser = argparse.ArgumentParser()
```

### Add mandatory argument
```{.python}
parser.add_argument('myargument')
```

### Add flag
```{.python}
parser.add_argument('-v', '--visualize', action='store_true')
```

### Parse arguments
```{.python}
args = parser.parse_args()
``` 
