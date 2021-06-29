from rest_framework import serializers

from recipes.models import Follow


class FollowSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(min_value=1)
