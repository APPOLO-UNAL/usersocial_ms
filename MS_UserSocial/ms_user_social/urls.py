from rest_framework.urlpatterns import format_suffix_patterns
from ms_user_social.views import *
from django.urls import path

urlpatterns = [
    path('user/', userDetails),
    path('getAllUsers/',getAllUsers),
    path('follow/',connectUaU),
    path('unfollow/',disconnectUaU),
    path('follows/',getFollows),
    path('followers/',getFollowers)
]

urlpatterns = format_suffix_patterns(urlpatterns)