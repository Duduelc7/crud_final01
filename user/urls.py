from django.urls import path
from crud_app import views
from django.contrib.auth.views import LogoutView
from user.models import *

from user.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", RegisterView.as_view(), name="register"),
    path("films/", Filmlist.as_view(), name='film-list'),
]

htmx_urlpatterns = [
    path('check_username/', check_username, name='check-username'),
    path('add-film/', add_film, name='add-film')
]

urlpatterns += htmx_urlpatterns
