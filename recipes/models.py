from django.db import models

from users.models import User


class Teg(models.Model):
    title = models.CharField(
        max_length=40,
        verbose_name='Тег',
        help_text='Не более 40 символов',
    )
    slug = models.SlugField(
        unique=True,
        max_length=40,
        verbose_name='Адрес для страницы с рецептами по тегу',
        help_text='Не более 40 символов',
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Краткое описание',
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title


class Measure(models.Model):
    title = models.CharField(
        max_length=40,
        verbose_name='Тег',
        help_text='Не более 40 символов',
    )

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    title = models.CharField(
        max_length=40,
        verbose_name='Тег',
        help_text='Не более 40 символов',
    )
    measure = models.ManyToManyField(
        Measure,
        through='IngredientMeasureRelation',
        related_name='titles',
        verbose_name="Жанр",
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.title


class IngredientMeasureRelation(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        null=True,
        on_delete=models.SET_NULL
    )
    measure = models.ForeignKey(
        Measure,
        null=True,
        on_delete=models.SET_NULL
    )
    quantity = models.IntegerField(
        verbose_name="Количество",
    )


class Recipe(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Рецепт',
        help_text='Не более 200 символов',
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name="Автор",
    )
    image = models.ImageField(
        upload_to='recipes/',
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Краткое описание',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='ingredient',
        verbose_name='Ингредиент',
        help_text='Добавьте ингредиенты.',
    )
    teg = models.ManyToManyField(
        Teg,
        related_name='teg',
        verbose_name='Тег',
        help_text='Добавьте тег (один или несколько).',
    )
    time = models.DurationField(
        verbose_name="Время приготовления",
    )
    slug = models.SlugField(
        unique=True,
        max_length=40,
        verbose_name='Адрес для страницы с рецептом',
        help_text='Не более 40 символов',
    )

    pub_date = models.DateTimeField(
        verbose_name="Дата публикации",
        auto_now_add=True,
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title


class Follow (models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='follower',
        verbose_name="Подписчик",
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='following',
        verbose_name="Пользователь на которого подписались",
    )

    class Meta:
        verbose_name_plural = 'Подписки'
        verbose_name = 'Подписка'

    def __str__(self):
        return f'@Подписчик {self.user} @Автор {self.author}'