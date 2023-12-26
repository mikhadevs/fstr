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
    user = UsersSerializer()
    date_added = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    coords = CoordsSerializer()
    level = LevelsSerializer()
    images = PassImagesSerializer()
    class Meta:
        model = Pass
        fields = [
            'id',
            'status',
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
        read_only_fields = ['status']
        filterset_fields = ['email']
        verbose_name = 'Перевал'

    def validate(self, data):
        if self.instance is not None:
            turist = self.instance.user
            data_turist = data.get('users')
            validating_fields = [
                turist.email != data_turist['email'] ,
                turist.fam != data_turist['fam'],
                turist.name != data_turist['name'],
                turist.otc != data_turist['otc'],
                turist.phone != data_turist['phone']
            ]
            if data_turist is not None and any(validating_fields):
                raise serializers.ValidationError(
                    {'E-mail,ФИО и номер телефона изменить нельзя! '}
                )
        return data


