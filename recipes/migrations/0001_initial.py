# Generated by Django 3.2.3 on 2021-06-01 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Не более 40 символов', max_length=40, verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Не более 40 символов', max_length=40, verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Единица измерения',
                'verbose_name_plural': 'Единицы измерения',
            },
        ),
        migrations.CreateModel(
            name='Teg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Не более 40 символов', max_length=40, verbose_name='Тег')),
                ('slug', models.SlugField(help_text='Не более 40 символов', max_length=40, unique=True, verbose_name='Адрес для страницы с рецептами по тегу')),
                ('description', models.TextField(help_text='Краткое описание', verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Не более 200 символов', max_length=200, verbose_name='Рецепт')),
                ('image', models.ImageField(upload_to='recipes/')),
                ('description', models.TextField(help_text='Краткое описание', verbose_name='Описание')),
                ('time', models.DurationField(verbose_name='Время приготовления')),
                ('slug', models.SlugField(help_text='Не более 40 символов', max_length=40, unique=True, verbose_name='Адрес для страницы с рецептом')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('ingredients', models.ManyToManyField(help_text='Добавьте ингредиенты.', related_name='ingredient', to='recipes.Ingredient', verbose_name='Ингредиент')),
                ('teg', models.ManyToManyField(help_text='Добавьте тег (один или несколько).', related_name='teg', to='recipes.Teg', verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
        migrations.CreateModel(
            name='IngredientMeasureRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('ingredient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.ingredient')),
                ('measure', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.measure')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='measure',
            field=models.ManyToManyField(related_name='titles', through='recipes.IngredientMeasureRelation', to='recipes.Measure', verbose_name='Жанр'),
        ),
    ]
