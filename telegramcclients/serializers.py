from rest_framework import serializers
from .models import User
from masjid.serializers import MasjidSerializer

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserWithMasjidSerializer(serializers.ModelSerializer):
    masjid = MasjidSerializer(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

