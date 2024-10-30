# diploma

команда для выгрузки фикстур на Windows:

python -Xutf8 manage.py dumpdata --indent=2 -o db.json

команда для загрузки фикстур:

python manage.py loaddata db.json
