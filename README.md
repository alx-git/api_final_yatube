ОПИСАНИЕ

Этот проект позволяет получать и передавать данные социальной сети Yatube через API.

УСТАНОВКА

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

