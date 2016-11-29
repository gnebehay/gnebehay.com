# MySQL

## Grant all privileges
```
GRANT ALL PRIVILEGES ON database.* TO 'user'@'%' WITH GRANT OPTION;
```

## Change password
```
SET PASSWORD FOR 'user'@'localhost' = PASSWORD('password');
FLUSH PRIVILEGES;
```

## Export to csv
```
SELECT * FROM table INTO OUTFILE '/tmp/export.csv' FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';
```

## Export headers
```
SELECT GROUP_CONCAT(COLUMN_NAME) from INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'table' and TABLE_SCHEMA='database' order BY ORDINAL_POSITION
```



