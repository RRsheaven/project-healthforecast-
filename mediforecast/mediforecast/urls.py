
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('App.urls')),

    path('admin/', admin.site.urls),
]
