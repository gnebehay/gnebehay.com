code: true

# Pandas

## Rename columns

```{.python}
df.columns = ['a', 'b'] # Rename all columns
df.rename(columns={'$a': 'a', '$b': 'b'}) # Rename individual columns
```

## Delete columns

```{.python}
df.drop('column_name', axis=1, inplace=True)
```

## Sort

```{.python}
# Ascending
df.sort_values('column_name')
# Descending
df.sort_values('column_name', ascending=False)
```

## Show more rows/columns
```{.python}
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)
```

