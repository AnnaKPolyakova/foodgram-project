Foodgram-project is an online service where users can publish recipes, subscribe to other users, save recipes to “Favorites,” and download a list of products needed to prepare one or more selected dishes before going to the store.

http://130.193.44.117/

To run the project locally, follow these steps:

Install dependencies:

```shell
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Create environment variables:

```shell
Add the following data to the file called .env:
SECRET_KEY=
EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

Run the project:

```shell
./manage.py runserver --settings=config.settings.local_dev
or
./manage.py runserver --settings=config.settings.local_prod
```

Load test data (if necessary):

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
