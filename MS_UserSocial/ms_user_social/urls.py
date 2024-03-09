from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ms_user_social.views import UserList, UserDetail, UserArtistIDs

urlpatterns = [
    path('user/', UserList.as_view()),
    path('user/<str:pk>', UserDetail.as_view()),
    path('users/<str:pk>/artists/', UserArtistIDs.as_view(), name='user_artists'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
