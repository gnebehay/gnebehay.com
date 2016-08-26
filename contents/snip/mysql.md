# MySQL

## Grant all privileges on database to user
```
GRANT ALL PRIVILEGES ON mydb.* TO 'myuser'@'%' WITH GRANT OPTION;
```

## Change password of user
```
SET PASSWORD FOR 'jeffrey'@'localhost' = PASSWORD('cleartext password');
FLUSH PRIVILEGES;
```

