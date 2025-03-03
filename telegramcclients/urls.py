from django.urls import path
from .views import AddOrUpdateUserApiView, UserExistsApiView, GetUserMasjidInfo, GetAllUserInfo

urlpatterns = [
    path('check-user/', UserExistsApiView.as_view(), name='check-user'),
    path('add-or-update/', AddOrUpdateUserApiView.as_view(), name='add-or-update'),
    path('get-user-masjid/', GetUserMasjidInfo.as_view(), name='get-user-masjid'),
    path('get-all-user-info/', GetAllUserInfo.as_view(), name='get-all-user-info'),
]
