from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from masjid.models import Masjid
from .serializers import UsersSerializer, UserWithMasjidSerializer
from masjid.serializers import MasjidSerializer


class AddOrUpdateUserApiView(APIView):
    def post(self, request):
        telegram_id = request.data.get("telegram_id")
        district = request.data.get("district").title()
        region = request.data.get("region").title()
        masjid_name = request.data.get("masjid").title()

        if not (telegram_id and district and region and masjid_name):
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        masjid = Masjid.objects.filter(name=masjid_name, region=region, district=district).first()
        if not masjid:
            return Response({"error": "Masjid not found."}, status=status.HTTP_404_NOT_FOUND)

        # Update or create user
        user, created = User.objects.update_or_create(
            telegram_id=telegram_id,
            defaults={"district": district.title(), "region": region.title(), "masjid": masjid}
        )

        return Response(UsersSerializer(user).data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)


class UserExistsApiView(APIView):
    def get(self, request):
        telegram_id = request.query_params.get('telegram_id')

        if not telegram_id:
            return Response({"status": False, "error": "Telegram ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        user_exists = User.objects.filter(telegram_id=telegram_id).exists()
        return Response({"status": user_exists}, status=status.HTTP_200_OK)


class GetUserMasjidInfo(APIView):
    def get(self, request):
        telegram_id = request.query_params.get('telegram_id')
        if not telegram_id:
            return Response({"status": False, "error": "Telegram ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(telegram_id=telegram_id).first()
        if not user:
            return Response({"status": False, "error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if not user.masjid:
            return Response({"status": False, "error": "Masjid information not found."},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = MasjidSerializer(user.masjid)
        return Response({"status": True, "masjid": serializer.data}, status=status.HTTP_200_OK)


class GetAllUserInfo(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserWithMasjidSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
