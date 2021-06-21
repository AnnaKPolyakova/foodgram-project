from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from recipes.models import Follow
from users.models import User


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Follow
        read_only_fields = ['user', 'author']
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'author'],
                message='Такая подписка уже существует!'
            )
        ]

    def validate(self, data):
        """ Проверка на выполнение условия """
        if data['user'] == data['author']:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя"
            )
        return data