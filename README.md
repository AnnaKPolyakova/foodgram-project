foodgram-project 

http://130.193.44.117/

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
Если запуска на сервере:

```shell
sudo docker-compose exec web python manage.py makemigrations
sudo docker-compose exec web python manage.py migrate
sudo docker-compose exec web python manage.py collectstatic --no-input
sudo docker-compose exec web python manage.py load_site test_data/flatpage.json
sudo docker-compose exec web python manage.py load_flatpage test_data/flatpage.json
sudo docker-compose exec web python manage.py load_site_fl_rel test_data/rel_site_fl.json
sudo docker-compose exec web python manage.py load_measure_ingredient test_data/ingredients.json
sudo docker-compose exec web python manage.py load_tag test_data/tag.json
sudo docker-compose exec web python manage.py load_user test_data/user.json
sudo docker-compose exec web python manage.py load_recipes test_data/recipes.json
sudo docker-compose exec web python manage.py load_rec_ing_rel test_data/rec_ing_rel.json
sudo docker-compose exec web python manage.py load_rec_tag_rel test_data/rec_tag_rel.json
sudo docker-compose exec web python manage.py load_follow test_data/follow.json
sudo docker-compose exec web python manage.py load_favorite test_data/favorite.json
sudo docker-compose exec web python manage.py fix_num
sudo docker-compose exec web python manage.py createsuperuser

```