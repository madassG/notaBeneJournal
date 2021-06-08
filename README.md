Проект notaBeneJournal - новостной сайт.

Установка приложения:\
$ virtualenv venv\
$ source venv/bin/activate\
$ pip install -r requirements.txt\
$ python manage.py makemigrations\
$ python manage.py migrate\
$ python manage.py runserver

При надобности для сборки статики:\
python manage.py collectstatic

Все странички шаблонов находятся только в директории template и во внутренних директориях.

Описание всех URL и передаваемых в их шаблон переменных по ссылке:\
https://eduhseru-my.sharepoint.com/:w:/g/personal/vvvorobinov_edu_hse_ru/EagcN02xGedFqkcxbq0hjEsB-X5Tg7CG4gGYjS2zk0rDUQ