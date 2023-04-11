from .serializers import *
from rest_framework import viewsets


class PassUserViewSet(viewsets.ModelViewSet):
    swagger_schema = None
    queryset = PassUser.objects.all()
    serializer_class = PassUserSerializer
