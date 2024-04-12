
from django.contrib import admin
from django.urls import path
from app.views import *
from generic.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:group_name>/',index),
    path('gen/<str:group_name>/',genericHome)
]
