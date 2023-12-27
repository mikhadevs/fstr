import django_filters
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from django.http import JsonResponse

from .serializers import *
from .models import *

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer

class LevelsViewSet(viewsets.ModelViewSet):
    queryset = Levels.objects.all()
    serializer_class = LevelsSerializer

class PassImageViewSet(viewsets.ModelViewSet):
    queryset = PassImages.objects.all()
    serializer_class = PassImagesSerializer

class PassViewSet(viewsets.ModelViewSet):
    queryset = Pass.objects.all()
    serializer_class = PassSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('user__email',)


    def create(self, request, *args, **kwargs):
        serializer = PassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': status.HTTP_200_OK,
                    'message': 'Успех',
                    'id': serializer.data['id']
                }
            )
        if status.HTTP_400_BAD_REQUEST:
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Сервер не смог обработать некоторые поля',
                    'id': None
                }
            )
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response(
                {
                    'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'message': 'Ошибка при выполнении операции',
                    'id': None
                }
            )

    def update(self, request, *args, **kwargs):
        Pass = self.get_object()
        if Pass.status == 'NW':
            serializer = PassSerializer(
                Pass,
                data=request.data,
                partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {   'state': '1',
                        'message':'Данные изменены'
                     }
                )
            else:
                return Response(
                    {
                        'state': '0',
                        'message': serializer.errors
                    }
                )
        else:
            return Response(
                {
                    'state': '0',
                    'message':f'При статусе: {Pass.get_status_display()}, редактирование невозможно.'
                }
            )


class EmailView(generics.ListAPIView):
    serializer_class = PassSerializer

    def get(self, request, *args, **kwargs):
        email = kwargs.get('email', None)
        if Pass.objects.filter(user__email=email):
            data = PassSerializer(
                Pass.objects.filter
                (
                    user__email=email
                ),
                many=True
            ).data
        else:
            data = {'message': f'Пользователь с {email} не найден'}
        return JsonResponse(data, safe=False)