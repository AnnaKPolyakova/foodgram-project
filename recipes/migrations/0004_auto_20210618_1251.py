# Generated by Django 3.2.3 on 2021-06-18 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_purchase'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'verbose_name': 'Рецепт', 'verbose_name_plural': 'Избранное'},
        ),
        migrations.AlterModelOptions(
            name='purchase',
            options={'verbose_name': 'Рецепт', 'verbose_name_plural': 'Список покупок'},
        ),
        migrations.AlterField(
            model_name='purchase',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='recipes.recipe', verbose_name='Рецепт'),
        ),
    ]
