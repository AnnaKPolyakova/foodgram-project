from rest_framework import serializers

from recipes.models import Follow
from users.models import User
from rest_framework.validators import UniqueTogetherValidator


class FollowSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='id',
        queryset=User.objects.all()
    )
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Follow
        fields = ['author', 'user']

    def validate(self, data):

        if data['user'] == data['author']:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя"
            )
        return data
