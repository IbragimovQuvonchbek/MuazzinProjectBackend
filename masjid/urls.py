from django.urls import path
from .views import GetMasjidsInfo

urlpatterns = [
    path('get-masjid-info/', GetMasjidsInfo.as_view(), name='get-masjid-info')
]