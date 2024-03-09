# from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = [
#     path('user/', ),
# ]



#from django.conf.urls import url
from ms_user_social.views import *
from django.urls import path
urlpatterns = [
    path('user', userDetails),
    path('getAllUsers',getAllUsers),
    # path('city',cityDetails),
    # path('getAllCities',getAllCities),
    # path('connectPaC',connectPaC),
    # path('connectPaP',connectPaP)
]

urlpatterns = format_suffix_patterns(urlpatterns)