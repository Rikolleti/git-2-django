# Реализуем API онлайн-библиотеки

## Задание

Реализована небольшая онлайн-библиотеку. По сути, она состоит из 2 сущностей: книги и заказы.

Реализованы действия crud над объектами:

- `/api/v1/books/` - список всех товаров,
- `/api/v1/books/create/` - добавление книги,
- `/api/v1/books/<id_книги>/` - получение одной книги,
- `/api/v1/books/update/<id_книги>/` - редактирование данных о книге,
- `/api/v1/books/delete/<id_книги>/` - удаление книги.

Также реализован viewset для заказов. 

Дополнительное задание выполнено.

## Документация по проекту

Для запуска проекта необходимо:

1. Установить зависимости:
```commandline
pip install -r requirements.txt
```

2. Выполнить следующие команды:

- команда для применения миграций для базы данных:

```commandline
python manage.py migrate
```

- команда для запуска приложения:

```commandline
python manage.py runserver
```

- при создании моделей или их изменении необходимо выполнить следующие команды:

```commandline
python manage.py makemigrations
python manage.py migrate
```
