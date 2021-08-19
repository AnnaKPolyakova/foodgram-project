Foodgram-project - это онлайн-сервис, где пользователи могут публиковать рецепты, подписываться на других пользователей, сохранять рецепты в «Избранное», скачивать список продуктов необходимых для приготовления одного или нескольких выбранных блюд перед походом в магазин.

http://130.193.44.117/

Для запуска проекта у себя локально выполните следующие действия:

Установите зависимости:

```shell
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Создайте переменные окружения:

```shell
В файл с названием .env доавляем следующие данные:
SECRET_KEY=
EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

Запустите проект:

```shell
./manage.py runserver --settings=config.settings.local_dev
или 
./manage.py runserver --settings=config.settings.local_prod
```

Загрузите тестовые данные (при необходимости):

```shell
python manage.py load_site test_data/flatpage.json --settings=config.settings.local_dev
python manage.py load_flatpage test_data/flatpage.json --settings=config.settings.local_dev
python manage.py load_site_fl_rel test_data/rel_site_fl.json --settings=config.settings.local_dev
python manage.py load_measure_ingredient test_data/ingredients.json --settings=config.settings.local_dev
python manage.py load_tag test_data/tag.json --settings=config.settings.local_dev
python manage.py load_user test_data/user.json --settings=config.settings.local_dev
python manage.py load_recipes test_data/recipes.json --settings=config.settings.local_dev
python manage.py load_rec_ing_rel test_data/rec_ing_rel.json --settings=config.settings.local_dev
python manage.py load_rec_tag_rel test_data/rec_tag_rel.json --settings=config.settings.local_dev
python manage.py load_follow test_data/follow.json --settings=config.settings.local_dev
python manage.py load_favorite test_data/favorite.json --settings=config.settings.local_dev
python manage.py fix_num --settings=config.settings.local_dev
```