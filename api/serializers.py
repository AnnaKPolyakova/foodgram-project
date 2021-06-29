from rest_framework import serializers


class FollowSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)


class PurchasesSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)


class FavoriteSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)
