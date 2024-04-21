from rest_framework.urlpatterns import format_suffix_patterns
from ms_user_social.views import *
from django.urls import path

urlpatterns = [
    path('user/', userDetails),
    path('getAllUsers/',getAllUsers),
    path('follow/',connectUaU),
    path('unfollow/',disconnectUaU),
    path('followsCount/',getFollows),
    path('followers/',getFollowers),
    path('followingCount/',getWhichFollows),
    path('following/',getWhoFollows)
]

urlpatterns = format_suffix_patterns(urlpatterns)