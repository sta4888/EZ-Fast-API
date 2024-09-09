# EZ-Fast-API
Самый простой пример Fast-API приложения с alembic, postgres, sqlmodel, sqladmin docker


## After clone

после клонирования репозитория вводим команду

```shell
cp .env.sample .env
```

```shell
docker-compose exec web alembic revision --autogenerate -m "init"
```
для инициализации алембика и БД

затем другую команду (эту команду нужно будет вызывать всегда, как только мы совершили какие либо изменение в моделях БД)

```shell
docker-compose exec web alembic upgrade head
```

