from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MasjidSerializer
from .models import Masjid

class GetMasjidsInfo(APIView):
    def get(self, request):
        district = request.query_params.get('district').title()
        region = request.query_params.get('region').title()

        if not district or not region:
            return Response({"error": "Telegram ID is required."}, status=status.HTTP_400_BAD_REQUEST)


        masjids = Masjid.objects.filter(region=region, district=district)
        serialized_masjids = MasjidSerializer(masjids, many=True)

        return Response(serialized_masjids.data, status=status.HTTP_200_OK)