from rest_framework import serializers
from users.serializers import PassUserSerializer
from .models import *


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height',)


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('winter', 'summer', 'autumn', 'spring',)


class ImagesSerializer(serializers.ModelSerializer):
    data = serializers.URLField()

    class Meta:
        model = Images
        fields = ('data', 'title',)


class PerevalSerializer(serializers.ModelSerializer):
    user = PassUserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        fields = ('id', 'user', 'beauty_title', 'title', 'other_titles', 'connect', 'coords', 'level', 'images', 'status')

    def create(self, validated_data, **kwargs):
        user = validated_data.pop('user')
        coords = validated_data.pop('coords')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        user = PassUser.objects.create(**user)
        coords = Coords.objects.create(**coords)
        level = Level.objects.create(**level)
        pereval = Pereval.objects.create(**validated_data, user=user, coords=coords, level=level, status='new')

        for image in images:
            data = image.pop('data')
            title = image.pop('title')
            Images.objects.create(pereval=pereval, data=data, title=title)

        return pereval
