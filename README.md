# diploma

# Для формирования нового графа нужно удалить файл graph.json. Он автоматически создасться и будет обновляться при работе алгоритма для сохранения графа после перезапуска сервера.

команда для выгрузки фикстур на Windows:

python -Xutf8 manage.py dumpdata --indent=2 -o db.json

команда для загрузки фикстур:

python manage.py loaddata db.json

Команда для создания суперпользователя:

python manage.py csu

Команда для создания тестовых пользователей:

python manage.py aut

Команда для запуска проекта:

python manage.py runserver
