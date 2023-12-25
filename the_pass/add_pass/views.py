from rest_framework import viewsets, status
from rest_framework.response import Response

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
