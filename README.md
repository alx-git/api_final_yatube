# API YATUBE

ОПИСАНИЕ
---

Этот проект позволяет получать и передавать данные прообраза социальной сети через API. Сделан для того, чтобы научится реализовывать API в Django с применением Вьюсетов и JWT-токенов для аутентификации. 

ЗАВИСИМОСТИ
---
Django==2.2.16

pytest==6.2.4

pytest-pythonpath==0.7.3

pytest-django==4.4.0

djangorestframework==3.12.4

djangorestframework-simplejwt==4.7.2
Pillow==8.3.1

PyJWT==2.1.0

requests==2.26.0

УСТАНОВКА
---

Клонировать репозиторий и перейти в него в командной строке:

git clone

cd api_final_yatube

Cоздать и активировать виртуальное окружение:

python -m venv venv

source venv/Scripts/activate

Установить зависимости из файла requirements.txt:

pip install -r requirements.txt

Выполнить миграции:

python manage.py migrate

Запустить проект:

python manage.py runserver

ПРИМЕРЫ
---

Запрос
http://127.0.0.1:8000/api/v1/groups/

Результат
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]

