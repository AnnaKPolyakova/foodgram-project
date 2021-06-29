from django.db import models

from users.models import User


class Tag(models.Model):
    ORANGE = "orange"
    GREEN = "green"
    PURPLE = "purple"

    COLOR_TYPE_CHOICES = [
        (ORANGE, "orange"),
        (GREEN, "green"),
        (PURPLE, "purple"),
    ]
    title = models.CharField(
        max_length=40,
        verbose_name="Тег",
        help_text="Не более 40 символов",
    )

    color = models.CharField(choices=COLOR_TYPE_CHOICES, max_length=20)

    slug = models.SlugField(
        unique=True,
        max_length=40,
        verbose_name="Адрес для страницы с рецептами по тегу",
        help_text="Не более 40 символов",
    )

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название",
        help_text="Не более 100 символов",
    )
    measure = models.CharField(
        max_length=40,
        verbose_name="Единицы измерения",
    )

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

    def __str__(self):
        return f"{self.title}, {self.measure}"


class Recipe(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название рецепта",
        help_text="Не более 200 символов",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recipes",
        verbose_name="Автор",
    )
    image = models.ImageField(
        upload_to="recipes/",
        verbose_name="Фото",
        help_text="Загрузите фото",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Краткое описание",
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through="RecipeIngredientRelation",
        related_name="recipes",
        verbose_name="Ингредиенты",
        help_text="Добавьте ингредиенты.",
    )
    tags = models.ManyToManyField(
        Tag,
        related_name="recipes",  #recipes
        verbose_name="Теги",
        help_text="Добавьте тег (один или несколько).",
    )

    time = models.PositiveIntegerField(
        verbose_name="Время приготовления",
    )

    pub_date = models.DateTimeField(
        verbose_name="Дата публикации",
        auto_now_add=True,
    )

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.title


class RecipeIngredientRelation(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="recipe_m2m",
        verbose_name="Рецепт",
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="ingredient_m2m",
        verbose_name="Ингредиент",
    )
    ingredient_order = models.PositiveIntegerField(blank=False, null=False)

    amount = models.PositiveIntegerField(verbose_name="Количество")

    class Meta:
        ordering = ["ingredient_order"]
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name="Подписчик",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name="Пользователь на которого подписались",
    )

    class Meta:
        verbose_name_plural = "Подписки"
        verbose_name = "Подписка"
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'user'],
                name='unique follow')
        ]

    def __str__(self):
        return f"Подписчик @{self.user} Автор @{self.author}"


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorite",
        verbose_name="Пользователь",
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="favorite",
        verbose_name="Рецепт",
    )

    class Meta:
        verbose_name_plural = "Избранное"
        verbose_name = "Рецепт"
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique favorite')
        ]

    def __str__(self):
        return f"Пользователь @{self.user} Рецепт {self.recipe}"


class Purchase(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="purchase",
        verbose_name="Пользователь",
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="purchase",
        verbose_name="Рецепт",
    )

    class Meta:
        verbose_name_plural = "Список покупок"
        verbose_name = "Рецепт"
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique purchase')
        ]

    def __str__(self):
        return f"Пользователь @{self.user} Список покупок {self.recipe}"
