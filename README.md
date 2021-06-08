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
python manage.py load_measure_ingredient ingredients/ingredients.json --settings=config.settings.dev
python manage.py load_teg ingredients/teg.json --settings=config.settings.dev
python manage.py load_user ingredients/user.json --settings=config.settings.dev
python manage.py load_recipes ingredients/recipes.json --settings=config.settings.dev
python manage.py load_rec_ing_rel ingredients/rec_ing_rel.json --settings=config.settings.dev
python manage.py load_rec_teg_rel ingredients/rec_teg_rel.json --settings=config.settings.dev
python manage.py load_follow ingredients/follow.json --settings=config.settings.dev


```