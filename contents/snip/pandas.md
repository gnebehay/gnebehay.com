# Pandas

## Rename column
Rename all columns
```
df.columns = ['a', 'b']
```
Rename individual columns
```
df.rename(columns={'$a': 'a', '$b': 'b'})
```

## Delete columns

```
df.drop('column_name', axis=1, inplace=True)
```

## Sort

```
df.sort_values('column_name')
```
Reverse
```
df.sort_values('column_name', ascending=False)
```

## Show more rows/columns
```
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)
```

