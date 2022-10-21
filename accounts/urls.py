from django.contrib import admin
from django.urls import path,include
from .views import ExampleView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path("test/",ExampleView.as_view())
]
