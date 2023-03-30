from rest_framework import serializers
from .models import *


class PassUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassUser
        fields = ('lastname', 'firstname', 'surname', 'phone', 'email',)
