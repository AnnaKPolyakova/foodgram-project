foodgram-project

Настройка локального окружения:

```shell
python -m pip install --upgrade pip
pip install -r requirements/local.txt
```

Запуск проекта:

```shell
./manage.py runserver --settings=config.settings.dev
```

Загрузка тестовых данных

```shell
python manage.py load_data ingredients/ingredients.json --settings=config.settings.dev
```