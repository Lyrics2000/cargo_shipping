
from django.urls import path
from .views import PostCargo,GetHistory,AllVehicleCategory

urlpatterns = [

    path("add/cargo/",PostCargo.as_view()),
    path("update/cargo/",GetHistory.as_view()),
    path("all/category/",AllVehicleCategory.as_view())
  
]
