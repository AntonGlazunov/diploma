# diploma

# Для формирования нового графа нужно удалить файл graph.json. Он автоматически создасться и будет обновляться при работе алгоритма для сохранения графа после перезапуска сервера.

GET по ссылке local_host:8000/content_api/ для получения рекомендаций по API 

PUT или PATCH по ссылке local_host:8000/users_api/add_preferences/<int:pk>/ для добавления предпочтений пользователю

GET по ссылке local_host:8000/users_api/preferences/<int:pk>/ для просмотра предпочтений пользователя

GET по ссылке local_host:8000/users_api/statistics/<int:pk>/ для просмотра статистики использования спервиса пользователем

Всю документацию по работе API можно посмотреть по адресу local_host:8000/redoc/ или local_host:8000/swagger/swagger-ui/

Комманда для применения миграций:

python manage.py migrate 

Команда для удаления graph.json:

python manage.py del_graph

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
