
from django.contrib import admin
from django.urls import path
from allusers.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home)
]
