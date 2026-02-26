# CRUD «Библиотека» (Django + PostgreSQL)

## Реализовано
- **Book**: HTML CRUD (List/Detail/Create/Update/Delete) через Django CBV
- **Author**: REST API (JSON) через DRF ViewSet
- PostgreSQL как основная БД (конфиг в `library/settings.py`)

## Установка
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## PostgreSQL
Создайте БД `library_db` и заполните креды в `library/settings.py`:
- USER / PASSWORD / HOST / PORT

## Миграции и запуск
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Маршруты

### HTML (книги)
- `GET /books/`
- `GET /books/<id>/`
- `GET/POST /books/new/`
- `GET/POST /books/<id>/edit/`
- `GET/POST /books/<id>/delete/`

> В браузере удаление делается через POST-форму (стандарт для Django).

### JSON API (авторы)
- `GET /authors/`
- `GET /authors/<id>/`
- `POST /authors/`
- `PUT /authors/<id>/`
- `DELETE /authors/<id>/`
