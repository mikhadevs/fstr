from rest_framework import serializers
from .models import Users, Coords, Levels, PassImages, Pass
from drf_writable_nested import WritableNestedModelSerializer

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'email',
            'fam',
            'name',
            'otc',
            'phone'
        ]
        verbose_name = 'Турист'


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = [
            'latitude',
            'longitude',
            'height'
        ]
        verbose_name = 'Координаты'

class LevelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Levels
        fields = [
            'spring',
            'summer',
            'autumn',
            'winter'
        ]
        verbose_name = 'Уровень сложности'

class PassImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PassImages
        fields = [
            'image_id',
            #'pass_id'

        ]
        verbose_name = 'Фотография(и)'

class PassSerializer(WritableNestedModelSerializer):
    status = 'new'
    user = UsersSerializer()
    date_added = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    coords = CoordsSerializer()
    level = LevelsSerializer()
    images = PassImagesSerializer()
    class Meta:
        model = Pass
        fields = [
            'id',
            'user',
            'date_added',
            'coords',
            'level',
            'beauty_title',
            'title',
            'other_titles',
            'connect',
            'images'
        ]

        verbose_name = 'Перевал'

