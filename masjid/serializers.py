from rest_framework.serializers import ModelSerializer
from .models import Masjid


class MasjidSerializer(ModelSerializer):
    class Meta:
        model = Masjid
        fields = '__all__'