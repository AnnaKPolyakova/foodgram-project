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
python manage.py load_measure_ingredient test_data/test_data.json --settings=config.settings.dev
python manage.py load_teg test_data/teg.json --settings=config.settings.dev
python manage.py load_user test_data/user.json --settings=config.settings.dev
python manage.py load_recipes test_data/recipes.json --settings=config.settings.dev
python manage.py load_rec_ing_rel test_data/rec_ing_rel.json --settings=config.settings.dev
python manage.py load_rec_teg_rel test_data/rec_teg_rel.json --settings=config.settings.dev
python manage.py load_follow test_data/follow.json --settings=config.settings.dev


```