# Create database
I use PostgreSQL 17.4.
```sql
CREATE USER blog_user WITH PASSWORD 'password';
CREATE DATABASE blog_db OWNER blog_user ENCODING 'UTF8' LC_COLLATE 'ru_RU.UTF8' LC_CTYPE 'ru_RU.UTF8' TEMPLATE=template0;
```

# Applying migration to a database
```shell
python manage.py migrate
```

# Create superuser
```shell
python manage.py createsuperuser
```

# Image
![Image alt](/img/1.jpg)
![Image alt](/img/2.jpg)